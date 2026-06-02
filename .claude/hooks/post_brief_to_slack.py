#!/usr/bin/env python3
"""
Post today's Daily Brief to Slack #news_from_ai.

Required env var: SLACK_WEBHOOK_URL
Guard: only posts if today's brief was modified today (JST) and
       the sentinel file for today doesn't exist yet.
"""

import json
import os
import re
import subprocess
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

JST = timezone(timedelta(hours=9))
NOW_JST = datetime.now(JST)

# Allow GitHub Actions to override the target date via BRIEF_DATE env var
# (GHA checks out fresh, so file mtime != original commit time)
_DATE_OVERRIDE = os.environ.get("BRIEF_DATE", "")
TODAY = _DATE_OVERRIDE if _DATE_OVERRIDE else NOW_JST.strftime("%Y-%m-%d")
YEAR_MONTH = TODAY[:7]

WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")

REPO_ROOT = Path(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip()
)
BRIEF_PATH = REPO_ROOT / f"01_Daily-Briefs/{YEAR_MONTH}/{TODAY}.md"
SENTINEL = Path(f"/tmp/stablecoin_slack_posted_{TODAY}.lock")
GITHUB_BASE = (
    "https://github.com/rianlien/stablecoin_payment_knowledge-/blob/main"
)

# ── Parsing ───────────────────────────────────────────────────────────────────

def _section(text: str, header: str) -> str:
    """Return concatenated content of ALL ## sections whose header starts with 'header'."""
    pat = rf"## {re.escape(header)}[^\n]*\n(.*?)(?=\n## |\Z)"
    parts = [m.group(1).strip() for m in re.finditer(pat, text, re.DOTALL)]
    return "\n\n".join(parts) if parts else ""


def parse_note_links(text: str) -> dict[str, str]:
    """
    Parse ## 新規追加ノート → {entity_keyword: url}.
    Slug format: YYYY-MM-DD_Entity_topic  (entity may contain hyphens).
    Each keyword from the entity part (length >= 4) maps to the first link URL.
    """
    section = _section(text, "新規追加ノート")
    links: dict[str, str] = {}
    for block in re.split(r"\n(?=- \[\[)", "\n" + section):
        slug_m = re.search(r"\[\[(.*?)\]\]", block)
        if not slug_m:
            continue
        slug = slug_m.group(1)
        parts = slug.split("_")
        entity = parts[1].lower() if len(parts) >= 2 else ""
        url_m = re.search(r"\]\((https?://[^)]+)\)", block)
        if not url_m:
            continue
        url = url_m.group(1)
        for kw in entity.split("-"):
            if len(kw) >= 4:
                links.setdefault(kw, url)
    return links


def parse_topics(section: str, note_links: dict[str, str]) -> list[tuple[str, str, str]]:
    """
    Parse 今日の要点 bullets → [(title, first_sentence, url), ...].
    URL is looked up from note_links by matching entity keywords against the title.
    Handles both:
      - **Title（date）**：desc   (date inside bold)
      - **Title**（date）：desc   (date outside bold)
    """
    items = []
    for m in re.finditer(
        r"-\s+\*\*(.*?)\*\*[^：:]*[：:]\s*(.*?)(?=\n-\s+\*\*|\Z)", section, re.DOTALL
    ):
        title = m.group(1).strip()
        desc = m.group(2).strip().replace("\n", " ")
        first = re.split(r"。|\.(?=\s)", desc)[0]
        desc_out = first + "。" if "。" in desc else first
        # Find matching URL by scanning note_links keywords against the title
        url = ""
        title_lower = title.lower()
        for kw, link in note_links.items():
            if kw in title_lower:
                url = link
                break
        items.append((title, desc_out, url))
    return items


def parse_implications(section: str) -> list[str]:
    """Parse 今日の重要論点 numbered items → [bold-title, ...]."""
    items = []
    for m in re.finditer(
        r"\d+\.\s+\*\*(.*?)\*\*[：:]", section, re.DOTALL
    ):
        items.append(m.group(1).strip())
    return items


def parse_monitoring(text: str) -> list[str]:
    """Extract 継続監視すべきこと sub-list items."""
    m = re.search(
        r"- 継続監視すべきこと:\n(.*?)(?=\n- (?![ \t])|\Z)", text, re.DOTALL
    )
    if not m:
        return []
    return [
        line.strip().lstrip("- ").strip()
        for line in m.group(1).splitlines()
        if line.strip().startswith("- ")
    ]


def parse_brief(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    # Front matter
    fm = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
    fm_text = fm.group(1) if fm else ""
    count = re.search(r"new_notes_count:\s*(\d+)", fm_text)

    topics_section = _section(text, "今日の要点")
    impl_section = _section(text, "今日の重要論点")
    note_links = parse_note_links(text)

    return {
        "date": TODAY,
        "new_notes_count": count.group(1) if count else "?",
        "topics": parse_topics(topics_section, note_links),
        "implications": parse_implications(impl_section),
        "monitoring": parse_monitoring(text),
    }

# ── Slack formatting ──────────────────────────────────────────────────────────

def _trunc(s: str, n: int = 280) -> str:
    return s if len(s) <= n else s[:n - 1] + "…"


def build_payload(data: dict) -> dict:
    rel = str(BRIEF_PATH.relative_to(REPO_ROOT))
    github_url = f"{GITHUB_BASE}/{rel}"

    # 主要トピック
    topic_lines = []
    for title, desc, url in data["topics"]:
        title_md = f"<{url}|{title}>" if url else title
        topic_lines.append(f"• *{title_md}*\n  {_trunc(desc)}")
    topics_text = "\n".join(topic_lines) or "（記載なし）"

    # 示唆
    impl_lines = [f"• {s}" for s in data["implications"]]
    impl_text = "\n".join(impl_lines)

    # 継続監視
    mon_text = " / ".join(data["monitoring"]) if data["monitoring"] else ""

    blocks: list[dict] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Stablecoin / Agentic Payments — {data['date']} Daily Brief",
                "emoji": True,
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"*主要トピック*　新規ノート {data['new_notes_count']} 件\n\n"
                    + topics_text
                ),
            },
        },
    ]

    if impl_text:
        blocks += [
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*示唆*\n\n{impl_text}"},
            },
        ]

    if mon_text:
        blocks += [
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*継続監視*\n{_trunc(mon_text, 500)}",
                },
            },
        ]

    blocks += [
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"詳細 → <{github_url}|GitHub で開く>",
            },
        },
    ]

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

# ── Guards ────────────────────────────────────────────────────────────────────

def brief_modified_today() -> bool:
    """True if the brief file's mtime is today (JST), or SKIP_MTIME_CHECK is set."""
    if os.environ.get("SKIP_MTIME_CHECK"):
        return True
    mtime = datetime.fromtimestamp(BRIEF_PATH.stat().st_mtime, tz=JST)
    return mtime.date() == NOW_JST.date()

# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    if not WEBHOOK_URL:
        print("[slack] SLACK_WEBHOOK_URL not set — skipping")
        return

    if not BRIEF_PATH.exists():
        print(f"[slack] brief not found: {BRIEF_PATH} — skipping")
        return

    if not brief_modified_today():
        print(f"[slack] brief not modified today — skipping")
        return

    if SENTINEL.exists():
        print(f"[slack] already posted today ({TODAY}) — skipping")
        return

    try:
        data = parse_brief(BRIEF_PATH)
        payload = build_payload(data)
        post(payload)
        SENTINEL.touch()
        print(f"[slack] posted Daily Brief {TODAY} to #news_from_ai ✓")
    except Exception as exc:
        print(f"[slack] ERROR: {exc}")
        raise


if __name__ == "__main__":
    main()
