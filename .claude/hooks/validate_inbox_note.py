#!/usr/bin/env python3
"""PostToolUse hook: 00_Inbox/ ニュースノートの Contract を決定論的に検証する。

Write / Edit 後に発火し、`00_Inbox/` 配下の .md だけを対象に frontmatter と
ファイル名形式を機械チェックする。客観的に明白な違反のみブロックし（exit 2 + stdout JSON）、
曖昧な内容（事実の正確さ等）は判断しない（人間 / Claude の領域）。

Contract の正は `.claude/rules/inbox-notes.md`。
stdin は Claude Code が渡す JSON（tool_input.file_path 等）。
対象外パス・解析不能時は安全側に倒して exit 0（誤検知で作業を止めない）。
"""
import json
import os
import re
import sys

REQUIRED_KEYS = [
    "title", "date", "source_url",
    "entity", "category", "primary_category",
    "article_published_date", "underlying_event_date", "primary_source_date",
    "importance", "confidence", "tags",
]
LEVELS = {"High", "Medium", "Low"}
FILENAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_.+\.md$")


def allow():
    sys.exit(0)


def block(reasons):
    msg = "Inbox ノートの Contract 違反（.claude/rules/inbox-notes.md）:\n- " + "\n- ".join(reasons)
    print(json.dumps({"decision": "block", "reason": msg}, ensure_ascii=False))
    sys.exit(2)


def extract_frontmatter(text):
    """先頭の --- ... --- ブロックを取り出して {key: raw_value} と tags 行リストを返す。"""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None, None
    body = m.group(1)
    lines = body.split("\n")
    fields = {}
    tags_items = []
    i = 0
    while i < len(lines):
        line = lines[i]
        km = re.match(r"^([A-Za-z_][\w-]*):(.*)$", line)
        if km:
            key = km.group(1)
            val = km.group(2).strip()
            if key == "tags":
                if val.startswith("[") and val.endswith("]"):
                    inner = val[1:-1].strip()
                    tags_items = [t.strip() for t in inner.split(",") if t.strip()] if inner else []
                else:
                    j = i + 1
                    while j < len(lines) and re.match(r"^\s+-\s+", lines[j]):
                        tags_items.append(lines[j].strip()[1:].strip())
                        j += 1
                fields["tags"] = "list"
                i = j
                continue
            fields[key] = val
        i += 1
    return fields, tags_items


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except Exception:
        allow()  # JSON でなければ何もしない

    path = (data.get("tool_input") or {}).get("file_path") or ""
    if not path:
        allow()

    norm = path.replace("\\", "/")
    base = os.path.basename(norm)
    # 対象: 00_Inbox 配下の .md（index.md は除外）
    if "/00_Inbox/" not in norm and not norm.startswith("00_Inbox/"):
        allow()
    if not base.endswith(".md") or base == "index.md":
        allow()

    reasons = []

    if not FILENAME_RE.match(base):
        reasons.append(f"ファイル名が `YYYY-MM-DD_<entity>_<slug>.md` 形式でない: {base}")

    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except Exception:
        allow()  # 読めない（削除直後等）なら止めない

    fields, tags_items = extract_frontmatter(text)
    if fields is None:
        block(["frontmatter（--- で囲む YAML）が見つからない"] + reasons)

    for key in REQUIRED_KEYS:
        if key not in fields:
            reasons.append(f"必須 frontmatter が無い: `{key}`")
        elif key != "tags" and fields[key] == "":
            reasons.append(f"必須 frontmatter が空: `{key}`")

    for key in ("importance", "confidence"):
        v = fields.get(key, "")
        if v and v not in LEVELS:
            reasons.append(f"`{key}` は High / Medium / Low のいずれか（現在: {v}）")

    if "tags" in fields:
        n = len(tags_items)
        if n < 3 or n > 5:
            reasons.append(f"`tags` は 3〜5 個（現在: {n} 個）")

    if reasons:
        block(reasons)
    allow()


if __name__ == "__main__":
    main()
