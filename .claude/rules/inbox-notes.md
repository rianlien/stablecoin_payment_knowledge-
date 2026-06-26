---
paths:
  - "00_Inbox/**/*.md"
---

# Inbox ニュースノートの Contract

`00_Inbox/` 配下のニュースノートが満たすべき形。層 = Mechanism（再収集可能な事実）。
作り方の手順は `.claude/skills/daily-news/SKILL.md`、思想は `_meta/PHILOSOPHY.md`。
横断ルール（事実と解釈の分離 / importance≠confidence / tags 既存優先 / 1ニュース1ファイル）は `CLAUDE.md` を正とする。

## ファイル名
- `YYYY-MM-DD_<entity>_<short-slug>.md`
- 例: `2026-05-11_Cryptorefills_x402-agent-checkout-mcp.md`

## 必須 frontmatter
- `title` / `date` / `source` / `source_url`
- `entity` / `category` / `primary_category`
- 来歴3日付: `article_published_date` / `underlying_event_date` / `primary_source_date`
- `tags`（配列・3〜5個）
- `importance`（High / Medium / Low）
- `confidence`（High / Medium / Low）

> これらは `.claude/hooks/validate_inbox_note.py`（PostToolUse hook）が機械的に検証する。欠落・形式違反は作成時にブロックされる。

## 来歴（トレーサビリティ）
- `source_url` ＋ 上記3日付で一次情報まで遡れるようにする。

## 作成後（同じ run 内で）
- テンプレート `90_Templates/news_note_template.md` に従う。
- 対応する概念ページにリンクを追記する（詳細は `.claude/rules/concept-pages.md`）。
