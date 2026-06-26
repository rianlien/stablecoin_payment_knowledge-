# stablecoin_payment_knowledge-

ステーブルコイン決済 / agentic commerce 関連のニュースと示唆を、チームで再利用可能な
Markdown 資産として蓄積するナレッジベース。Obsidian vault として閲覧・編集でき、
Claude のクラウド routine が収集・整理・メンテナンスを自動化し、Slack 通知と
公開サイト（GitHub Pages / MkDocs）まで自動で流れる。

> **引き継ぎ向けメモ**: 運用の「中身」を最短で把握したい場合は、まず
> [`CLAUDE.md`](CLAUDE.md)（運用ルールの本体）と `.claude/skills/` の各スキルを読むこと。
> 引き継ぎ時にやることは §9 のチェックリストに集約した。
>
> **設計思想**（なぜこの構造なのか / Intent → Contract → Mechanism と非対称ルール）は
> [`_meta/PHILOSOPHY.md`](_meta/PHILOSOPHY.md)、配線図・CODEMAP は
> [`_meta/ARCHITECTURE.md`](_meta/ARCHITECTURE.md) に集約している（公開サイトには載せない内部ドキュメント）。

---

## 1. 全体の流れ

```
収集（Claude routine）→ /00_Inbox にニュースノート → 概念ページへ相互リンク
   → /01_Daily-Briefs に Daily Brief → main に push
       → GitHub Actions が Slack 投稿 & GitHub Pages にサイト公開

週次:  /02_Weekly に Weekly Digest（同様に Slack & 公開）
夜間1: リンク整合性チェック・補完 → 不足ページを auto-todo Issue として起票
夜間2: auto-todo Issue を読んで概念ページを新規作成（PR）
夜間3: スキル/プロンプト自体を自己改善（PR）
```

すべての自動 routine について、**「作法（rulebook）」は `.claude/skills/`、「実行プロンプト」は
`.claude/prompts/`、「実体スクリプト」は `.claude/hooks/`** に分かれている。
routine → prompt → skill → hook の対応表（配線図）は [`_meta/ARCHITECTURE.md`](_meta/ARCHITECTURE.md) を単一ソースとする。

---

## 2. ディレクトリ構成

| パス | 役割 |
|---|---|
| `00_Inbox/` | ニュースノート（1ニュース1ファイル）。160件以上 |
| `01_Daily-Briefs/YYYY-MM/` | 日次まとめ（月別フォルダ） |
| `02_Weekly/` | 週次まとめ（Weekly Digest） |
| `03_Topics/` | テーマ別の論点整理（概念ページ） |
| `04_Protocols/` | x402 / AP2 / ERC など仕様・技術論点の深掘り |
| `05_MOCs/` | Map of Content（規制・企業・プロトコルの横断マップ） |
| `06_Entities/Companies/` `Networks/` `Organizations/` | 企業・ネットワーク・標準化団体の概要ページ |
| `90_Templates/` | ノート・Brief・Weekly・Protocol のテンプレート |
| `docs/` `mkdocs.yml` `overrides/` | 公開サイト（MkDocs Material）の設定 |
| `.claude/` | 運用自動化（skills / prompts / hooks / settings） |
| `.github/workflows/` | GitHub Actions（Slack 投稿・サイト公開・auto-merge） |
| `CLAUDE.md` | **運用ルールの本体**（routine の採用基準・リンク規則など） |

---

## 3. 運用ルールの本体: `CLAUDE.md`

routine の判断基準（採用 / 除外、日付の扱い、概念ページへのリンク規則、Daily Brief /
Weekly の書き方など）はすべて [`CLAUDE.md`](CLAUDE.md) に集約している。
スキルやプロンプトは `CLAUDE.md` を参照する前提で書かれているため、**ルールを変えるときは
まず `CLAUDE.md` を更新する**。

---

## 4. 自動 routine

routine は **Claude のクラウド routine（claude.ai/code の scheduled agent）** が、
`.claude/prompts/*.txt` を実行プロンプトとして起動する。スケジュール定義そのものは
リポジトリ外（クラウド側、旧オーナーのアカウント）にあるため、**引き継ぎ時は新オーナーが
自分のアカウントで routine を登録し直す必要がある**（→ §9）。

| routine | 想定頻度 | 実行プロンプト | 作法（skill） | 主な処理 |
|---|---|---|---|---|
| 日次収集 | 毎日 | `daily_routine_prompt.txt` | `daily-news/SKILL.md` | 直近7日のニュース収集 → `00_Inbox` ノート作成 → 概念ページへリンク → `01_Daily-Briefs` 作成 |
| 週次まとめ | 毎週月曜 | `weekly_digest_prompt.txt` | `weekly-digest/SKILL.md` | 直前の暦週を統合 → `02_Weekly` に Weekly Digest |
| リンク整合性 | 毎晩 | `nightly_link_check_prompt.txt` | `nightly-link-check/SKILL.md` | リンク漏れ補完 → 不足ページを `auto-todo` Issue として起票（Web検索なし） |
| 概念ページ生成 | 毎晩 | `auto_todo_executor_prompt.txt` | （prompt 内に作法を内包） | `auto-todo` Issue を読み、不足概念ページを新規作成して PR |
| スキル自己改善 | 毎晩 | `skill_improver_prompt.txt` | `skill-improver/SKILL.md` | git履歴・ノート品質からルールの曖昧さを検出し、ルール/スキル/プロンプトの改善 PR を作成 |

`auto-todo` ラベルの Issue を「リンク整合性 routine が起票 → 概念ページ生成 routine が消化」する
2段構成になっている点に注意。

プロンプト内の `${TODAY}` `${WEEK}` `${START_DATE}` などはクラウド routine 実行時に差し込まれる。
**手動実行**する場合は、これらを当日 / 対象週の値に置き換えて Claude Code に渡せばよい。

> **REPO_ROOT について**: `skill_improver_prompt.txt` と `auto_todo_executor_prompt.txt` は
> リポジトリのルートを `${REPO_ROOT}` placeholder で参照する（`${TODAY}` と同じ規約）。
> routine 登録時に `${TODAY}` 等と同様 `${REPO_ROOT}` を渡す（routine は repo ルートを
> cwd として実行されるため、未指定でも本文は相対パスで動く）。

---

## 5. スキル（`.claude/skills/`）

各 routine の「作法（rulebook）」を定義したドキュメント。クラウド routine と
手動実行のどちらでも、この内容に従って作業する。

各スキルは `.claude/skills/<name>/SKILL.md`（frontmatter で `/command`・自動マッチ可。`skill-improver` は unattended 専用で自動起動しない）。

- `daily-news/SKILL.md` — 日次ニュース収集の採用基準・ノート形式・タグ規則・Daily Brief 規則
- `weekly-digest/SKILL.md` — 週次まとめの対象期間・出力形式・概念ページ軽微更新
- `nightly-link-check/SKILL.md` — リンク整合性補完と `auto-todo` Issue 化の手順
- `skill-improver/SKILL.md` — ルール/スキル/プロンプトの夜間自己改善ループ（signal収集 → 改善 → quality gate → PR）

**path 固有のルール**は `.claude/rules/*.md`（`paths:` でスコープ。該当ファイル編集時に自動ロード）に分離: `inbox-notes` / `daily-briefs` / `concept-pages`。**決定論的検証**は `.claude/settings.json` の PostToolUse hook ＋ `.claude/hooks/validate_inbox_note.py`（Inbox ノートの frontmatter・ファイル名を作成時に検証）。手段の使い分けは [`_meta/ARCHITECTURE.md`](_meta/ARCHITECTURE.md) §5。

> 概念ページ生成 routine（auto-todo-executor）は、作法を
> `.claude/prompts/auto_todo_executor_prompt.txt` 内に内包しているため、独立した skill ファイルは持たない。

---

## 6. hooks（`.claude/hooks/` のスクリプト）

| スクリプト | 役割 | 呼び出し元 |
|---|---|---|
| `check_note_links.py` | ノートと概念ページのリンク漏れ検出・TODO 抽出（JSON 出力） | 日次 / リンク整合性 routine が `python3` で実行 |
| `post_brief_to_slack.py` | Daily Brief を整形して Slack に投稿 | GitHub Actions（push 時） |
| `post_weekly_to_slack.py` | Weekly Digest を整形して Slack に投稿 | GitHub Actions（push 時） |

`check_note_links.py` の主な使い方:
```bash
python3 .claude/hooks/check_note_links.py --output /tmp/unlinked.json --since 30
# --since なしでフルスキャン（todo_suggestions を含む）
```

---

## 7. GitHub Actions（`.github/workflows/`）

| ワークフロー | トリガー | 処理 |
|---|---|---|
| `post-to-slack.yml` | `01_Daily-Briefs/**/*.md` を main に push | 追加された Daily Brief を Slack 投稿 |
| `post-weekly-to-slack.yml` | `02_Weekly/**/*.md` を main に push | 追加された Weekly Digest を Slack 投稿 |
| `deploy-docs.yml` | main への push / 手動 / auto-merge 完了 | MkDocs をビルドし GitHub Pages へ公開 |
| `auto-merge.yml` | PR の open / 更新 | コンフリクトの無い PR を自動マージ |

### 必要なシークレット / 設定

| 名前 | 必須 | 用途 |
|---|---|---|
| `SLACK_WEBHOOK_URL` | 必須 | Slack 投稿先 Incoming Webhook |
| `SITE_URL` | 任意 | Slack 投稿に公開サイトへのリンクを付ける場合に設定（未設定でも投稿は動く） |
| `GITHUB_TOKEN` | 自動 | Actions 既定トークン（auto-merge / Pages で使用） |

Slack 投稿が動くには、**リポジトリの Settings → Secrets に `SLACK_WEBHOOK_URL` が
設定されていること**が前提。Daily Brief のリンクは `[Source Name（YYYY-MM-DD）](URL)`
形式でないとスクリプトがリンクとして認識しないため、ノート作成時はこの形式を厳守する
（詳細は `CLAUDE.md`）。

---

## 8. 公開サイト（GitHub Pages / MkDocs）

- 公開 URL: https://rianlien.github.io/stablecoin_payment_knowledge-/
- main に push されると `deploy-docs.yml` が自動でビルド・公開する
- 各セクションフォルダを `docs/` にコピーし、`00_Inbox` と `01_Daily-Briefs` の
  index ページを自動生成してから `mkdocs build` する
- 依存: `mkdocs-material`, `mkdocs-roamlinks-plugin`, `mkdocs-awesome-pages-plugin`

ローカルでプレビューする場合:
```bash
pip install mkdocs-material mkdocs-roamlinks-plugin mkdocs-awesome-pages-plugin
mkdocs serve
```

---

## 9. 引き継ぎチェックリスト（新オーナー向け）

1. **リポジトリを clone する**
   ```bash
   git clone https://github.com/rianlien/stablecoin_payment_knowledge-.git
   ```
2. **`CLAUDE.md` と `.claude/skills/` のスキルを読む**（運用の中身を把握）
3. **Obsidian で vault を開く**（§10）
4. **GitHub Secrets を引き継ぐ**: `SLACK_WEBHOOK_URL`（必要なら `SITE_URL`）を
   新オーナー管理下で再設定する
5. **クラウド routine を再登録する**: 日次 / 週次 / リンク整合性 / 概念ページ生成 / スキル改善 の
   5 routine を、各 `.claude/prompts/*.txt` を実行プロンプトとして自分のアカウントの
   scheduled agent に登録する（旧オーナーのアカウントに紐づく routine は引き継がれない）。
   `skill_improver` / `auto_todo_executor` の登録時は `${REPO_ROOT}` を repo ルートのパスに
   割り当てる（`${TODAY}` 等と同じ要領）
6. **`auto-todo` ラベルが GitHub に存在するか確認する**（リンク整合性 / 概念ページ生成 routine が使う）
7. **Slack 投稿先チャンネルと Webhook の所有者を確認する**
8. **GitHub Pages が有効か確認する**（Settings → Pages）

---

## 10. ローカルでの閲覧・編集（Obsidian）

1. PC に Obsidian をインストールする
2. `Open folder as vault` から clone したフォルダを選択する
3. `Settings` → `Community plugins` で `Git` プラグインを有効化・インストールする
4. コマンドパレットから `Git: Pull` を実行して最新を取り込む

---

## 11. 編集ルール（要約）

詳細は `CLAUDE.md`。最低限、以下を守る。

- 1ニュース1ファイル。新規作成前に `00_Inbox` / `01_Daily-Briefs` で重複確認
- 事実と解釈を分け、推測は推測と明記し、出典リンクを残す
- 重要度（importance）と確からしさ（confidence）を分けて評価する
- 既存タグを優先し、tags は 3〜5 個
- 変更は review しやすい形を優先し、原則 direct commit しない（PR 経由）
