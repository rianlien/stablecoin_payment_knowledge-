#!/usr/bin/env python3
"""
check_note_links.py

/00_Inbox/ の全ノートをスキャンして、各概念ページ（Companies / Protocols / MOCs / Topics）
にリンクされているかを確認し、未リンク情報と TODO 候補を JSON で出力する。
スクリプト自体は読み取り専用 — 修正は Claude へのプロンプト経由で行う。

Usage:
    python3 check_note_links.py [--output PATH] [--since N_DAYS]

    --output  出力先 JSON (default: /tmp/unlinked.json)
    --since   直近 N 日以内のノートのみ対象 (省略時: 全件)
"""

import argparse
import json
import os
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ── Config ─────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(os.environ.get(
    "REPO_ROOT",
    subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                            text=True).strip()
))

INBOX     = REPO_ROOT / "00_Inbox"
COMPANIES = REPO_ROOT / "06_Entities" / "Companies"
PROTOCOLS = REPO_ROOT / "04_Protocols"
MOCS      = REPO_ROOT / "05_MOCs"
TOPICS    = REPO_ROOT / "03_Topics"

JST = timezone(timedelta(hours=9))

# ── タグマッピング（概念ページ stem → 一致するタグ／カテゴリ）
# 新しい概念ページを追加したときはここを更新する
#
# 保守的にする: 広すぎる tag（"agentic-commerce" など）はマップしない。
# 「このノートは確実にこの概念ページに属する」という強い信号のみ使う。

TOPIC_TAG_MAP = {
    # x402 専用タグを持つノートのみ
    "x402-ecosystem": ["x402"],
    # 決済認可に特化したタグのみ
    "agent-payment-authorization": ["payment-authorization"],
    # ウォレット専用タグのみ
    "agent-wallets": ["agent-wallet", "agentic-wallet"],
    # PSP・マーチャント向けに明示されたタグのみ
    "psp-merchant-readiness": ["merchant-readiness", "merchant-psp-readiness"],
    # クロスボーダー専用
    "stablecoin-b2b-crossborder": ["crossborder", "b2b-payments"],
    # ペイアウト専用
    "stablecoin-payouts-platforms": ["payouts", "payout"],
    # トークン化預金専用
    "tokenized-deposits": ["tokenized-deposits", "tokenized-deposit"],
    # 法案名が直接タグになっている場合のみ
    "GENIUS-Act": ["genius-act"],
    "CLARITY-Act": ["clarity-act"],
    # MOC_agent-payments-stack は意図的に除外（"agentic-commerce" との組み合わせが広すぎる）
}

PROTOCOL_TAG_MAP = {
    # 各プロトコルの識別子が直接タグになっている場合のみ
    "circle-cpn": ["circle-cpn", "cpn"],
    "ucp-universal-cart-protocol": ["ucp", "universal-cart-protocol"],
    # ERC/EIP は「erc-XXXX」という識別子タグがある場合のみ
    "ERC-8183_Agentic-Commerce": ["erc-8183"],
    "ERC-8004_Trustless-Agents": ["erc-8004"],
    "ERC-5564_Stealth-Addresses": ["erc-5564"],
    "EIP-7503_ZK-Wormholes": ["eip-7503"],
    "EIP-8182_Private-ETH-ERC20-Transfers": ["eip-8182"],
}

MOC_TAG_MAP = {
    # stablecoin-payments 専用タグのみ（"stablecoin" 単体は広すぎるため除外）
    "MOC_Stablecoin_Payments": ["stablecoin-payments"],
    # regulation タグが明示されている場合のみ
    "MOC_Regulation": ["regulation"],
    # MOC_Protocols / MOC_Companies は広すぎるため除外
}

# ── Frontmatter 解析 ─────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    m = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    raw = m.group(1)
    result: dict = {}

    for key in ("entity", "primary_category", "category", "date",
                "underlying_event_date"):
        vm = re.search(rf"^{key}:\s*(.+)$", raw, re.MULTILINE)
        if vm:
            result[key] = vm.group(1).strip().strip('"\'')

    # tags: inline 形式 or ブロック形式
    inline_tm = re.search(r"^tags:\s*\[(.*?)\]", raw, re.MULTILINE)
    if inline_tm:
        result["tags"] = [t.strip().strip('"\'') for t in inline_tm.group(1).split(",") if t.strip()]
    else:
        block_tm = re.search(r"^tags:\n((?:[ \t]*- .+\n?)+)", raw, re.MULTILINE)
        if block_tm:
            result["tags"] = [
                line.strip().lstrip("- ").strip()
                for line in block_tm.group(1).splitlines()
                if line.strip()
            ]

    if "tags" not in result:
        result["tags"] = []

    return result

# ── 概念ページの wikilink インデックスを構築 ──────────────────────────────────

def build_link_index(dirs: list[Path]) -> dict[str, set[str]]:
    """各概念ページに含まれる [[wikilink]] stem を収集して返す。"""
    index: dict[str, set[str]] = {}
    for d in dirs:
        if not d.is_dir():
            continue
        for f in d.rglob("*.md"):
            if f.name == "index.md":
                continue
            text = f.read_text(encoding="utf-8")
            stems = set(re.findall(r"\[\[([^\]|#]+)\]\]", text))
            index[str(f)] = stems
    return index

def is_linked_in(note_stem: str, concept_path: Path, link_index: dict[str, set[str]]) -> bool:
    return note_stem in link_index.get(str(concept_path), set())

# ── Companies ファイル名マップ ────────────────────────────────────────────────

def build_company_map() -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for f in COMPANIES.glob("*.md"):
        if f.name == "index.md":
            continue
        key = f.stem.lower()
        mapping[key] = f
        mapping[key.replace("-", "")] = f
        mapping[key.replace("-", " ")] = f
    return mapping

def candidate_companies(entity_str: str, company_map: dict[str, Path]) -> list[Path]:
    parts = re.split(r"[/,×]", entity_str)
    result: list[Path] = []
    for part in parts:
        raw = re.sub(r"[（(].*?[）)]", "", part).strip().lower()
        if raw in company_map:
            cp = company_map[raw]
            if cp not in result:
                result.append(cp)
            continue
        no_space = raw.replace(" ", "").replace("-", "")
        if no_space in company_map:
            cp = company_map[no_space]
            if cp not in result:
                result.append(cp)
    return result

def missing_companies_for(entity_str: str, company_map: dict[str, Path]) -> list[str]:
    """entity_str に含まれる企業のうち、Companies ページが存在しないものの名称を返す。"""
    SKIP_KEYWORDS = [
        # 規制機関・政府
        "senate", "congress", "committee", "government", "ministry",
        "agency", "authority", "court", "treasury", "parliament",
        "bafin", "sec", "cftc", "occ", "fca", "esma", "finma",
        "white house", "federal reserve",
        # 政治家（姓のみ・名前パターン）
        "senator", "representative", "governor", "minister",
        "tillis", "scott", "lummis", "gillibrand", "mchenry",
        "warren", "hagerty", "moreno", "gallego",
        # 汎用組織
        "council", "association", "coalition", "alliance",
        "group", "working group", "task force", "forum",
        # プロトコル・ブロックチェーン（企業ではない）
        "ethereum", "solana", "polygon", "bitcoin",
    ]
    parts = re.split(r"[/,×]", entity_str)
    missing = []
    for part in parts:
        raw = re.sub(r"[（(].*?[）)]", "", part).strip()
        if not raw or len(raw) < 4:
            continue
        key = raw.lower()
        no_space = key.replace(" ", "").replace("-", "")
        if key not in company_map and no_space not in company_map:
            if not any(sk in key for sk in SKIP_KEYWORDS):
                # 姓名パターン（単語2つ、各単語が大文字始まり）の人名を除外
                words = raw.split()
                is_person_name = (
                    len(words) == 2
                    and all(w[0].isupper() for w in words if w)
                    and all(w.isalpha() for w in words if w)
                )
                if not is_person_name:
                    missing.append(raw)
    return missing

# ── 概念ページ候補（Topics / Protocols / MOCs）────────────────────────────────

def candidate_pages(fm: dict, base_dir: Path, tag_map: dict[str, list[str]]) -> list[Path]:
    note_tags = set(t.lower() for t in fm.get("tags", []))
    category  = (fm.get("primary_category") or fm.get("category") or "").lower()
    candidates = []
    for stem, map_tags in tag_map.items():
        if any(t in note_tags or t in category for t in map_tags):
            candidate = base_dir / f"{stem}.md"
            if not candidate.exists():
                # x402 のようにサブディレクトリの場合
                candidate = base_dir / stem / f"{stem}.md"
            if candidate.exists() and candidate not in candidates:
                candidates.append(candidate)
    return candidates

# ── TODO 候補検出 ──────────────────────────────────────────────────────────────

def detect_missing_company_todos(
    inbox_files: list[Path], company_map: dict[str, Path]
) -> list[dict]:
    entity_to_notes: dict[str, list[str]] = defaultdict(list)
    for f in inbox_files:
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        entity = fm.get("entity", "")
        if not entity:
            continue
        for missing in missing_companies_for(entity, company_map):
            entity_to_notes[missing].append(f.stem)

    todos = []
    for entity, notes in entity_to_notes.items():
        # 2件以上のノートで参照されている場合のみ TODO 化
        if len(notes) >= 2:
            note_list = "\n".join(f"- {n}" for n in sorted(notes)[:10])
            todos.append({
                "type": "missing_company_page",
                "title": f"{entity} の Companies ページを作成",
                "body": (
                    f"`{entity}` の企業ページが `/06_Entities/Companies/` に存在しない。\n\n"
                    f"以下のノートで参照されている:\n{note_list}"
                ),
                "label": "auto-todo",
            })
    return todos


def detect_missing_protocol_todos(inbox_files: list[Path]) -> list[dict]:
    erc_counter: Counter = Counter()
    erc_to_notes: dict[str, list[str]] = defaultdict(list)

    protocol_stems = set()
    if PROTOCOLS.is_dir():
        for f in PROTOCOLS.rglob("*.md"):
            if f.name != "index.md":
                protocol_stems.add(f.stem.lower())

    for f in inbox_files:
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        for tag in fm.get("tags", []):
            low = tag.lower()
            if re.match(r"^(erc|eip)-\d+", low):
                erc_counter[tag] += 1
                erc_to_notes[tag].append(f.stem)

    todos = []
    for tag, count in erc_counter.items():
        tag_key = tag.lower().replace("-", "_")
        already_exists = any(
            tag.lower().replace("-", "_") in s or tag.lower() in s
            for s in protocol_stems
        )
        if count >= 2 and not already_exists:
            note_list = "\n".join(f"- {n}" for n in erc_to_notes[tag][:5])
            todos.append({
                "type": "missing_protocol_page",
                "title": f"{tag} のプロトコルページを作成",
                "body": (
                    f"`{tag}` に対応するプロトコルページが `/04_Protocols/` に存在しない。\n\n"
                    f"以下のノートで参照されている:\n{note_list}"
                ),
                "label": "auto-todo",
            })
    return todos


def detect_missing_topic_todos(inbox_files: list[Path]) -> list[dict]:
    cat_counter: Counter = Counter()
    cat_to_notes: dict[str, list[str]] = defaultdict(list)

    # Topics + MOCs の両方をチェック（MOC でカバーされている場合は除外）
    covered_stems = set()
    for d in [TOPICS, MOCS]:
        if d.is_dir():
            for f in d.rglob("*.md"):
                if f.name != "index.md":
                    covered_stems.add(f.stem.lower())

    # 日本語カテゴリや汎用すぎるカテゴリはスキップ
    SKIP_CATS = {
        "agentic-commerce", "agentic-payments", "machine-payments",
        "stablecoin-payments", "regulation", "企業発表", "規制",
    }

    for f in inbox_files:
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        cat = (fm.get("primary_category") or fm.get("category") or "").strip()
        if cat and cat not in SKIP_CATS:
            cat_counter[cat] += 1
            cat_to_notes[cat].append(f.stem)

    todos = []
    for cat, count in cat_counter.items():
        cat_key = cat.lower().replace("-", "_").replace(" ", "_").replace("/", "_")
        already_exists = any(cat_key in s or cat.lower() in s for s in covered_stems)
        if count >= 5 and not already_exists:
            note_list = "\n".join(f"- {n}" for n in cat_to_notes[cat][:5])
            todos.append({
                "type": "missing_topic_page",
                "title": f"`{cat}` の Topics ページを作成",
                "body": (
                    f"カテゴリ `{cat}` のノートが {count} 件あるが、Topics/MOC ページが存在しない。\n\n"
                    f"ノート例:\n{note_list}"
                ),
                "label": "auto-todo",
            })
    return todos

# ── メイン ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Check note-to-concept-page link integrity")
    parser.add_argument("--output", default="/tmp/unlinked.json",
                        help="出力先 JSON (default: /tmp/unlinked.json)")
    parser.add_argument("--since", type=int, default=None,
                        help="直近 N 日以内のノートのみ対象")
    args = parser.parse_args()

    link_index  = build_link_index([COMPANIES, PROTOCOLS, MOCS, TOPICS])
    company_map = build_company_map()

    cutoff = None
    if args.since:
        cutoff = (datetime.now(JST) - timedelta(days=args.since)).date()

    inbox_files: list[Path] = []
    for f in sorted(INBOX.glob("*.md")):
        if f.name == "index.md":
            continue
        if cutoff:
            m = re.match(r"^(\d{4}-\d{2}-\d{2})", f.stem)
            if m:
                note_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
                if note_date < cutoff:
                    continue
        inbox_files.append(f)

    unlinked = []
    for inbox_file in inbox_files:
        text = inbox_file.read_text(encoding="utf-8")
        fm   = parse_frontmatter(text)
        stem = inbox_file.stem

        missing: dict[str, list[str]] = {
            "companies": [], "protocols": [], "mocs": [], "topics": []
        }

        for cp in candidate_companies(fm.get("entity", ""), company_map):
            if not is_linked_in(stem, cp, link_index):
                missing["companies"].append(cp.stem)

        for pp in candidate_pages(fm, PROTOCOLS, PROTOCOL_TAG_MAP):
            if not is_linked_in(stem, pp, link_index):
                missing["protocols"].append(pp.stem)

        for mp in candidate_pages(fm, MOCS, MOC_TAG_MAP):
            if not is_linked_in(stem, mp, link_index):
                missing["mocs"].append(mp.stem)

        for tp in candidate_pages(fm, TOPICS, TOPIC_TAG_MAP):
            if not is_linked_in(stem, tp, link_index):
                missing["topics"].append(tp.stem)

        if any(missing.values()):
            unlinked.append({
                "note":     stem,
                "date":     fm.get("date", "") or fm.get("underlying_event_date", ""),
                "entity":   fm.get("entity", ""),
                "category": fm.get("primary_category") or fm.get("category", ""),
                "tags":     fm.get("tags", []),
                "missing_links": missing,
            })

    # TODO 候補（--since なしの全件スキャン時のみ）
    todo_suggestions: list[dict] = []
    all_inbox = list(INBOX.glob("*.md"))
    all_inbox = [f for f in all_inbox if f.name != "index.md"]
    if not args.since:
        todo_suggestions += detect_missing_company_todos(all_inbox, company_map)
        todo_suggestions += detect_missing_protocol_todos(all_inbox)
        todo_suggestions += detect_missing_topic_todos(all_inbox)

    output = {
        "generated_at": datetime.now(JST).isoformat(),
        "scanned_count": len(inbox_files),
        "total_unlinked": len(unlinked),
        "notes": unlinked,
        "todo_suggestions": todo_suggestions,
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(
        f"[check_note_links] scanned={len(inbox_files)}"
        f"  unlinked={len(unlinked)}"
        f"  todos={len(todo_suggestions)}"
        f"  → {args.output}"
    )


if __name__ == "__main__":
    main()
