---
name: run-stablecoin-knowledge-base
description: Run, test, and verify the stablecoin knowledge base CLI tools — check_note_links.py (link integrity scan), Slack posting scripts, and routine prompts. Use when asked to run, test, smoke-test, or screenshot this project.
---

# run-stablecoin-knowledge-base

このリポジトリの実行可能コンポーネントは GUI ではなく Python CLI スクリプト群。
メインドライバーは `smoke.sh` — 全スクリプトを実行してゼロエラーを確認する。

```
.claude/skills/run-stablecoin-knowledge-base/smoke.sh
```

## Prerequisites

Python 3.11 以上、標準ライブラリのみ（追加 pip install 不要）。

```bash
python3 --version   # 3.11.15 で確認済み
```

## Run (agent path) — smoke test

```bash
bash .claude/skills/run-stablecoin-knowledge-base/smoke.sh
```

正常出力例:

```
=== check_note_links.py ===
  ✓ full scan: runs and prints summary
  ✓ full scan: JSON has required keys and scanned_count > 0
  ✓ --since 7: runs
  ✓ --since 7: scanned_count <= full; todo_suggestions empty

=== post_brief_to_slack.py (dry-run, no webhook) ===
  ✓ exits cleanly when SLACK_WEBHOOK_URL is unset

=== post_weekly_to_slack.py (dry-run, no webhook) ===
  ✓ exits cleanly when SLACK_WEBHOOK_URL is unset

=== prompt files present ===
  ✓ daily_routine_prompt.txt exists
  ✓ nightly_link_check_prompt.txt exists
  ✓ weekly_digest_prompt.txt exists

ALL 9 checks passed.
```

終了コードが 0 なら全 OK。非 0 なら `✗` 行を見てどのスクリプトが壊れているか確認する。

## Individual script usage

### check_note_links.py — リンク整合性チェック

```bash
# 全件スキャン（nightly routine で使う）
python3 .claude/hooks/check_note_links.py --output /tmp/unlinked.json

# 直近 7 日だけ（高速確認用）
python3 .claude/hooks/check_note_links.py --since 7 --output /tmp/unlinked_7d.json

# 結果を人間が読む形で確認
python3 -c "
import json
d = json.load(open('/tmp/unlinked.json'))
print(f\"scanned={d['scanned_count']} unlinked={d['total_unlinked']} todos={len(d['todo_suggestions'])}\")
for n in d['notes']:
    print(' -', n['note'], '|', {k:v for k,v in n['missing_links'].items() if v})
"
```

出力 JSON のキー:
- `scanned_count` — スキャンしたノート数
- `total_unlinked` — リンク漏れが1件以上あるノートの数
- `notes[]` — 各リンク漏れノートの詳細（`missing_links.companies/topics/mocs/protocols/products`）
- `todo_suggestions[]` — GitHub Issue 化の候補（`--since` なし時のみ生成）

### post_brief_to_slack.py — Daily Brief を Slack に投稿

```bash
# 本番実行（SLACK_WEBHOOK_URL が必要）
SLACK_WEBHOOK_URL="https://hooks.slack.com/..." python3 .claude/hooks/post_brief_to_slack.py

# 日付を上書きしてテスト（mtime チェックをバイパス）
SLACK_WEBHOOK_URL="..." BRIEF_DATE="2026-06-18" SKIP_MTIME_CHECK=1 \
  python3 .claude/hooks/post_brief_to_slack.py
```

ガード条件（全て満たさないとスキップ）:
- `SLACK_WEBHOOK_URL` がセットされている
- 対象 Daily Brief ファイルが当日（JST）に更新されている（`SKIP_MTIME_CHECK=1` でバイパス可）
- `/tmp/stablecoin_slack_posted_YYYY-MM-DD.lock` が存在しない（二重投稿防止）

### post_weekly_to_slack.py — Weekly Digest を Slack に投稿

`post_brief_to_slack.py` と同様のガード構造。`SLACK_WEBHOOK_URL` 未設定時はスキップ。

## Routine prompts

| ファイル | 用途 | 実行タイミング |
|---|---|---|
| `.claude/prompts/daily_routine_prompt.txt` | Web 検索→ノート作成→Daily Brief 更新 | 毎日（変数 `TODAY`, `YEAR_MONTH`, `START_DATE` を置換して使う） |
| `.claude/prompts/nightly_link_check_prompt.txt` | リンク整合性チェック・概念ページ更新 | 毎晩（Web 検索なし） |
| `.claude/prompts/weekly_digest_prompt.txt` | 週次まとめ作成 | 毎週月曜 |

これらはエージェントへの指示文。`check_note_links.py` を内部で呼ぶ構造になっている。

## Gotchas

- `--since` を付けると `todo_suggestions` が空配列になる（全件スキャン時のみ生成する設計）。nightly routine では `--since` を使わないこと。
- `post_brief_to_slack.py` は GitHub Actions 環境では `mtime` が clone 時刻になるため `SKIP_MTIME_CHECK=1` と `BRIEF_DATE` の上書きが必要。
- Products ディレクトリ（`/06_Entities/Products/`）への wikilink 検出は **ニュースノート本文に `[[product-page-stem]]` が明示的に書かれている場合のみ** 動作する。タグや entity 名からの自動マッチは行わない（誤検知防止）。

## Troubleshooting

| 症状 | 原因・対処 |
|---|---|
| `scanned_count=0` | `REPO_ROOT` 環境変数が誤っているか `git rev-parse` が失敗している。リポジトリルートで実行しているか確認 |
| `unlinked` が想定より少ない | `--since` フラグが付いている可能性。全件は `--since` なしで実行 |
| `todo_suggestions` が空 | `--since` フラグが付いている。nightly routine は引数なしで実行する |
| Slack スクリプトが `already posted today` と言って止まる | `/tmp/stablecoin_slack_posted_YYYY-MM-DD.lock` を削除して再実行 |
