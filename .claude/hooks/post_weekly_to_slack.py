#!/usr/bin/env python3
"""
Post a Weekly Digest to Slack.

Required env vars:
  SLACK_WEBHOOK_URL
  WEEKLY_FILE   — repo-relative path, e.g. 02_Weekly/2026-W23.md
"""

import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
WEEKLY_FILE = os.environ.get("WEEKLY_FILE", "")
SITE_URL    = os.environ.get("SITE_URL", "").rstrip("/")

REPO_ROOT = Path(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip()
)

GITHUB_BASE = (
    "https://github.com/rianlien/stablecoin_payment_knowledge-/blob/main"
)

IMPORTANCE_ORDER = {"high": 0, "medium": 1, "low": 2}

# ── Parsing ───────────────────────────────────────────────────────────────────


def _section(text: str, header: str) -> str:
    """Return content of the first ## section whose heading starts with header."""
    pat = rf"## {re.escape(header)}[^\n]*\n(.*?)(?=\n## |\Z)"
    m = re.search(pat, text, re.DOTALL)
    return m.group(1).strip() if m else ""


def parse_frontmatter(text: str) -> dict:
    fm = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not fm:
        return {}
    raw = fm.group(1)
    result = {}
    for key in ("week", "period_start", "period_end", "notes_count"):
        m = re.search(rf"^{key}:\s*(.+)$", raw, re.MULTILINE)
        if m:
            result[key] = m.group(1).strip().strip('"')
    return result


def _extract_field(block: str, name: str) -> str:
    """Extract a `- name: value` field from a markdown block (may be multi-line)."""
    m = re.search(
        rf"^- {re.escape(name)}:\s*(.+?)(?=\n- |\n\n|\Z)",
        block,
        re.DOTALL | re.MULTILINE,
    )
    return m.group(1).strip() if m else ""


def _first_url(s: str) -> str:
    """Return the first Markdown-linked URL in s, or ''."""
    m = re.search(r"\]\((https?://[^)]+)\)", s)
    return m.group(1) if m else ""


def _clean(s: str) -> str:
    """Convert Markdown **bold** → Slack *bold*; strip [[wikilinks]]."""
    s = re.sub(r"\*\*(.*?)\*\*", r"*\1*", s)
    s = re.sub(r"\[\[.*?\]\]", "", s)
    return s.strip()


def parse_news_items(text: str) -> list[dict]:
    """
    Parse ## 今週の主要ニュース → list of dicts, sorted High → Medium → Low.
    Each dict: title, subtitle, overview, importance, link_url
    """
    section = _section(text, "今週の主要ニュース")
    items = []

    for block in re.split(r"\n(?=### )", "\n" + section):
        if not block.strip().startswith("###"):
            continue

        first_line = block.splitlines()[0]
        title_m = re.match(r"###\s+(?:\d+\.\s+)?(.+)", first_line)
        if not title_m:
            continue
        title = title_m.group(1).strip()

        sub_m = re.search(r"\*\*【(.+?)】\*\*", block)
        subtitle = sub_m.group(1).strip() if sub_m else ""

        overview_raw = _extract_field(block, "概要")
        imp_raw = _extract_field(block, "重要度")
        link_url = _first_url(_extract_field(block, "リンク"))

        imp_word_m = re.match(r"(\w+)", imp_raw)
        importance = imp_word_m.group(1).lower() if imp_word_m else ""

        items.append(
            {
                "title": title,
                "subtitle": subtitle,
                "overview": _clean(overview_raw),
                "importance": importance,
                "link_url": link_url,
            }
        )

    items.sort(key=lambda x: IMPORTANCE_ORDER.get(x["importance"], 9))
    return items


def parse_key_points(text: str) -> list[str]:
    """今週の要点 → bold titles only (4 items max)."""
    section = _section(text, "今週の要点")
    points = []
    for m in re.finditer(
        r"-\s+\*\*(.*?)\*\*[^：:]*[：:]", section, re.DOTALL
    ):
        points.append(m.group(1).strip())
    # Fallback: plain bullets
    if not points:
        for line in section.splitlines():
            line = line.strip().lstrip("- ").strip()
            if line:
                points.append(_trunc(line, 120))
    return points[:4]


def parse_themes(text: str) -> list[str]:
    """今週の重要テーマ → bold titles (4 items max)."""
    section = _section(text, "今週の重要テーマ")
    themes = []
    for m in re.finditer(r"\d+\.\s+\*\*(.*?)\*\*", section):
        themes.append(m.group(1).strip())
    return themes[:4]


def parse_monitoring(text: str) -> list[str]:
    """継続監視すべきこと sub-list (6 items max). Handles optional **bold** markers."""
    m = re.search(
        r"- \*{0,2}継続監視すべきこと[：:]\*{0,2}\s*\n(.*?)(?=\n- (?![ \t])|\Z)",
        text,
        re.DOTALL,
    )
    if not m:
        return []
    return [
        line.strip().lstrip("- ").strip()
        for line in m.group(1).splitlines()
        if line.strip().startswith("- ")
    ][:6]


def parse_digest(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    return {
        "week": fm.get("week", path.stem),
        "period_start": fm.get("period_start", ""),
        "period_end": fm.get("period_end", ""),
        "notes_count": fm.get("notes_count", "?"),
        "key_points": parse_key_points(text),
        "news_items": parse_news_items(text),
        "themes": parse_themes(text),
        "monitoring": parse_monitoring(text),
    }


# ── Slack formatting ──────────────────────────────────────────────────────────


def _trunc(s: str, n: int = 280) -> str:
    return s if len(s) <= n else s[:n - 1] + "…"


def _badge(importance: str) -> str:
    return {"high": "🔴 High", "medium": "🟡 Medium", "low": "⚪ Low"}.get(
        importance, ""
    )


def _news_block(item: dict) -> str:
    title_md = (
        f"<{item['link_url']}|{item['title']}>"
        if item["link_url"]
        else item["title"]
    )
    lines = [f"*{title_md}*  {_badge(item['importance'])}"]
    if item["subtitle"]:
        lines.append(f"  _{item['subtitle']}_")
    lines.append(f"  {_trunc(item['overview'], 220)}")
    return "\n".join(lines)


def build_payload(data: dict, github_url: str) -> dict:
    week = data["week"]
    period = (
        f"{data['period_start']} 〜 {data['period_end']}"
        if data["period_start"]
        else ""
    )

    blocks: list[dict] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Stablecoin / Agentic Payments — {week} Weekly Digest",
                "emoji": True,
            },
        },
    ]
    if period:
        blocks.append(
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"対象期間: {period}　ニュース {data['notes_count']} 件",
                    }
                ],
            }
        )
    blocks.append({"type": "divider"})

    # 今週の要点
    if data["key_points"]:
        pts = "\n".join(f"• {p}" for p in data["key_points"])
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*今週の要点*\n\n{pts}"},
            }
        )
        blocks.append({"type": "divider"})

    # 主要ニュース — split into chunks of 3 to stay under Slack's 3000-char limit
    news = data["news_items"]
    if news:
        chunks = [news[i : i + 3] for i in range(0, len(news), 3)]
        for idx, chunk in enumerate(chunks):
            text = "\n\n".join(_news_block(item) for item in chunk)
            if idx == 0:
                text = f"*主要ニュース*　{len(news)} 件\n\n" + text
            blocks.append(
                {"type": "section", "text": {"type": "mrkdwn", "text": text}}
            )
        blocks.append({"type": "divider"})

    # 今週のテーマ
    if data["themes"]:
        theme_text = "\n".join(
            f"{i + 1}. {t}" for i, t in enumerate(data["themes"])
        )
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*今週のテーマ*\n\n{theme_text}",
                },
            }
        )
        blocks.append({"type": "divider"})

    # 継続監視
    if data["monitoring"]:
        mon = "\n".join(f"• {m}" for m in data["monitoring"])
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*継続監視*\n\n{mon}",
                },
            }
        )
        blocks.append({"type": "divider"})

    # Footer
    if SITE_URL:
        site_weekly_url = f"{SITE_URL}/02_Weekly/{data['week']}/"
        footer_text = f"詳細 → <{site_weekly_url}|サイトで開く>　　<{github_url}|GitHub>"
    else:
        footer_text = f"詳細 → <{github_url}|GitHub で開く>"
    blocks.append(
        {"type": "section", "text": {"type": "mrkdwn", "text": footer_text}}
    )

    return {"blocks": blocks}


# ── Post ──────────────────────────────────────────────────────────────────────


def post(payload: dict) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = resp.read().decode()
        if body != "ok":
            raise RuntimeError(f"Slack responded: {body!r}")


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    if not WEBHOOK_URL:
        print("[slack] SLACK_WEBHOOK_URL not set — skipping")
        return

    if not WEEKLY_FILE:
        print("[slack] WEEKLY_FILE not set — skipping")
        return

    path = REPO_ROOT / WEEKLY_FILE
    if not path.exists():
        print(f"[slack] weekly digest not found: {path} — skipping")
        return

    rel = str(path.relative_to(REPO_ROOT))
    github_url = f"{GITHUB_BASE}/{rel}"

    try:
        data = parse_digest(path)
        payload = build_payload(data, github_url)
        post(payload)
        print(f"[slack] posted Weekly Digest {data['week']} to Slack ✓")
    except Exception as exc:
        print(f"[slack] ERROR: {exc}")
        raise


if __name__ == "__main__":
    main()
