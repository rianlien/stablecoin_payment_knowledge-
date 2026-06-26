---
name: weekly-digest
description: 直前の暦週のニュースと Daily Brief を統合し、変化の方向性・示唆・監視ポイント中心の週次まとめを作る手順。
when_to_use: 毎週月曜の週次まとめ routine を実行するとき、または週次ダイジェストを作るとき。
---

# Weekly Digest Skill

> **層: Mechanism（OS層）。** CLAUDE.md の Contract「Weekly 出力」を満たす手段。ルールを変えるときは先に CLAUDE.md / `_meta/` を更新する（非対称ルール）。

## Purpose
直前の暦週（月曜〜日曜）に蓄積したニュースノートと Daily Brief を統合し、
事実の羅列ではなく「変化の方向性・示唆・監視ポイント」を中心に週次まとめを作る。

## When to use
- 毎週月曜に、直前の暦週を対象に週次ダイジェストを作るとき
- `/02_Weekly/` に週次まとめを新規作成または更新するとき

## How it runs
- このスキルは作法（rulebook）を定義する。実際の起動は Claude のクラウド routine が
  `.claude/prompts/weekly_digest_prompt.txt` を実行する形で行う
- 手動実行する場合は、同 prompt の `${WEEK}` / `${PERIOD_START}` / `${PERIOD_END}` を
  対象週の値に置き換えて Claude Code に渡す
- 運用ルールの本体は repo ルートの `CLAUDE.md`「Contract — Weekly 出力」に従う

## Time window
- 対象は直前の暦週（月曜 00:00 〜 日曜 23:59、JST）
- 実行頻度は毎週月曜を想定する
- 採用基準はノートの作成日（`/00_Inbox/` のファイル日付）と対応 Daily Brief

## Source data
- `/00_Inbox/` — 対象期間に作成されたニュースノート全件
- `/01_Daily-Briefs/` — 対象期間に対応する Daily Brief

## Output
- `/90_Templates/weekly_digest_template.md` に従う
- 保存先は `/02_Weekly/`、ファイル名は対象週の識別子（例: `2026-W26.md`）
- frontmatter に以下を正確に記入する
  - `week`
  - `period_start`
  - `period_end`
  - `notes_count`
  - `key_themes`（週全体を貫くテーマ）
- 既に同じ週のファイルが存在する場合は、内容を確認した上で更新する

## Working style
- 事実の羅列より、変化の方向性・示唆・監視ポイントを優先する
- 重複話題は統合する
- 推測は推測と明記し、事実と解釈を分ける
- 後で MOC やトピック概念ページに反映しやすい粒度で書く

## Optional: concept page touch-up
今週の新着ノートで言及された概念について、軽微な更新のみ行ってよい。

- `/03_Topics/` — 「監視ポイント」「現状の論点」が古い場合に新情報を反映
- `/04_Protocols/` — 採用状況・最新動向が大きく変化した場合のみ更新
- `/06_Entities/Companies/` — 今週の主要企業ページにノートのリンク漏れがあれば追記

**制約**: 大幅な構造変更は行わない。既存テーブルへの行追加と短いコメント修正に留める。

## Slack / publishing
- `/02_Weekly/**/*.md` を main に push すると、GitHub Actions
  `post-weekly-to-slack.yml` が `.claude/hooks/post_weekly_to_slack.py` を実行し
  Slack に投稿する（`SLACK_WEBHOOK_URL` secret が必要）
- 同じ push で MkDocs サイト（GitHub Pages）も再デプロイされる
