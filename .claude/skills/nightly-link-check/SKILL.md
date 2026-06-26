---
name: nightly-link-check
description: 既存ノートと概念ページのリンク整合性を保ち、不足は auto-todo Issue 化する手順（Web 検索なし）。
when_to_use: 夜間のリンク整合性メンテナンス routine、またはリンク漏れを点検したいとき。
---

# Nightly Link Check Skill

> **層: Mechanism（OS層）。** CLAUDE.md の Contract「Concept page linking」「来歴」を満たす手段。ルールを変えるときは先に CLAUDE.md / `_meta/` を更新する（非対称ルール）。

## Purpose
既存ノートと概念ページの間のリンク整合性を保つ。Web 検索は行わず、
リンク漏れの補完と、対応すべき TODO の GitHub Issue 化のみを行う。

## When to use
- 夜間のリンク整合性メンテナンスを行うとき
- ニュースノートと概念ページ（Companies / Topics / MOCs / Protocols）の
  相互リンク漏れをまとめて補完したいとき

## How it runs
- このスキルは作法（rulebook）を定義する。実際の起動は Claude のクラウド routine が
  `.claude/prompts/nightly_link_check_prompt.txt` を実行する形で行う
- 手動実行する場合は、同 prompt を Claude Code に渡す
- 運用ルールの本体は repo ルートの `CLAUDE.md`「Contract — Concept page linking」「Contract — 来歴」に従う

## Scope
- Web 検索はしない（新規ニュースノートは作らない）
- 既存ノートと概念ページのリンク整合性チェックと修正のみ
- 対応する概念ページが実在しない場合はスキップ（新規作成しない）

## Task 1: リンク漏れの補完（直近 30 日）
1. リンク漏れを検出する
   ```
   python3 .claude/hooks/check_note_links.py --output /tmp/unlinked.json --since 30
   ```
2. `/tmp/unlinked.json` の `notes` 配列を処理し、`missing_links` を補完する
   - `companies` → `/06_Entities/Companies/` の "Inbox との紐付け" テーブル
   - `topics` → `/03_Topics/` の "主要ノート" テーブル
   - `mocs` → `/05_MOCs/` の関連テーブル
   - `protocols` → `/04_Protocols/` の "関連ニュース" テーブル
3. テーブル追記ルール
   - 形式は `| 日付 | [[ノート名]] | 位置づけ一行 |` を維持
   - 日付順で適切な位置に挿入
   - 位置づけ一行は、ノートのタイトルと frontmatter の `summary` / `implications` から簡潔に要約

## Task 2: TODO の GitHub Issue 化
1. フルスキャン結果を取得する（`--since` なし）
   ```
   python3 .claude/hooks/check_note_links.py --output /tmp/unlinked_full.json
   ```
2. `todo_suggestions` を確認し、各 TODO について重複を避けて Issue 化する
   - `gh issue list --label auto-todo --search "<title>"` で既存 open Issue を確認
   - 同一タイトルが open なら作成しない
   - 無ければ `gh issue create --title "<title>" --body "<body>" --label auto-todo`
3. ここで起票した `auto-todo` Issue は、後段の auto-todo-executor routine
   （`.claude/prompts/auto_todo_executor_prompt.txt`）が拾って概念ページを新規作成する

## Output
- リンク修正した概念ページ一覧（何件追記したか）
- 作成した GitHub Issue 一覧（タイトル）
- スキップ件数（ファイルなし等の理由）
