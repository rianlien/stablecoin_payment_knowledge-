# ARCHITECTURE / CODEMAP

「情報 → ファイル」のマッピングと、自動化の配線図を一箇所に集約する内部ドキュメント。
公開サイトには載せない。思想の定義は [`PHILOSOPHY.md`](PHILOSOPHY.md)、実務ルールは [`CLAUDE.md`](../CLAUDE.md)。

---

## 1. OS 層の配線図（routine → prompt → skill → hook）

すべての自動 routine は「作法（skill）」「実行プロンプト（prompt）」「実体スクリプト（hook）」に分かれる。
これがこの表の単一ソース（README はここを指す）。

| routine | 頻度 | 実行プロンプト（Mechanism） | 作法 / skill（Contract 参照） | 呼ぶ hook（Mechanism） |
| --- | --- | --- | --- | --- |
| 日次収集 | 毎日 | `.claude/prompts/daily_routine_prompt.txt` | `.claude/skills/daily-news/SKILL.md` | `check_note_links.py` |
| 週次まとめ | 毎週月曜 | `.claude/prompts/weekly_digest_prompt.txt` | `.claude/skills/weekly-digest/SKILL.md` | — |
| リンク整合性 | 毎晩 | `.claude/prompts/nightly_link_check_prompt.txt` | `.claude/skills/nightly-link-check/SKILL.md` | `check_note_links.py` |
| 概念ページ生成 | 毎晩 | `.claude/prompts/auto_todo_executor_prompt.txt` | （prompt 内に内包） | — |
| スキル自己改善 | 毎晩 | `.claude/prompts/skill_improver_prompt.txt` | `.claude/skills/skill-improver/SKILL.md` | — |

公開系（push トリガー、`.github/workflows/`）:

| workflow | トリガー | hook |
| --- | --- | --- |
| `post-to-slack.yml` | `01_Daily-Briefs/**` push | `post_brief_to_slack.py` |
| `post-weekly-to-slack.yml` | `02_Weekly/**` push | `post_weekly_to_slack.py` |
| `deploy-docs.yml` | main push / 手動 | `mkdocs build` |

プロンプト内 placeholder（routine 実行時に差し込み）: `${TODAY}` / `${WEEK}` / `${START_DATE}` / `${YEAR_MONTH}` / `${REPO_ROOT}`。

---

## 2. コンテンツ層の情報 → ファイル map

```
一次情報(URL)
   │  source_url + 3 dates
   ▼
00_Inbox/ … 個別の事実（Mechanism / 再収集可能 / 変化多い）
   │  ├─ 概念ページへ相互リンク → 06_Entities, 04_Protocols
   │  └─ その run の採用分を要約 → 01_Daily-Briefs/
   ▼
03_Topics, 05_MOCs … 論点枠組み・横断マップ（Intent / 保護資産 / 安定）
   ▲  「根拠ノート」セクションで Inbox を上向き参照
```

- **横断索引（CODEMAP の中核）は `05_MOCs`**: 規制 / 企業 / プロトコル / ステーブルコイン決済の入口。「どこに何があるか」を知りたいときの起点。
- **論点の枠組みは `03_Topics`**: テーマごとの問題の本質・比較軸・監視ポイント。
- **実体ページは `06_Entities`（企業 / ネットワーク / 組織）と `04_Protocols`**。

---

## 3. ディレクトリ別 層・安定度・禁止事項

| ディレクトリ | 層 | 安定度 | してはいけないこと |
| --- | --- | --- | --- |
| `_meta/` | Intent（OS） | 最も安定 | 日々の実務ルールをここに散らさない（CLAUDE.md へ） |
| `CLAUDE.md` | Contract（OS）＋ Intent 節 | 安定 | Mechanism の都合を無印で直書きしない |
| `90_Templates/` | Contract（OS） | 安定 | テンプレを末端ノートの都合で頻繁に変えない |
| `.claude/` | Mechanism（OS） | 変化中 | Contract / Intent を黙って書き換えない（上流を先に更新） |
| `05_MOCs/` | Intent（コンテンツ） | 安定 | 個別ニュースで枠組みを黙って上書きしない |
| `03_Topics/` | Intent（コンテンツ） | 安定 | 同上。矛盾は surface して残す |
| `04_Protocols/` `06_Entities/` | Intent〜Contract（コンテンツ） | やや安定 | 根拠ノートなしに断定を足さない |
| `01_Daily-Briefs/` `02_Weekly/` | Contract 出力（コンテンツ） | 日次・週次で増える | リンク形式（出力 Contract）を崩さない |
| `00_Inbox/` | Mechanism（コンテンツ） | 最も変化が多い | 事実と解釈を混ぜない。枠組み判断は Topics 側で |

---

## 4. 来歴チェーンの保持先

| 来歴の向き | 保持する場所 |
| --- | --- |
| 上向き（解釈 → 一次情報） | news note の `source_url` ＋ `article_published_date` / `underlying_event_date` / `primary_source_date` |
| 下向き（枠組み → 根拠） | `03_Topics` / `05_MOCs` / `06_Entities` / `04_Protocols` の「根拠ノート」「Inbox との紐付け」「関連ニュース」テーブル |
| 層の識別 | ディレクトリ位置 ＋ frontmatter（概念ページ `type:` / news `category`・`primary_category`） |

### 将来の拡張余地（今回未実装）

`check_note_links.py` は現在「概念ページ → Inbox の双方向リンク漏れ」を検出する。
将来、**「Topic / MOC の主張に根拠ノートが紐付いているか（来歴セクションの欠落）」** の検出を追加できる。
やるなら別タスクとして切り出す（今回はスクリプト改修しない）。

---

## 5. Steering mechanisms（Claude Code の制御手段の使い分け）

Anthropic「Steering Claude Code」の分類を、この vault の Mechanism 層に対応づけたもの。
**どの挙動をどの手段で表現すべきか**の決定表。新しいルールを足すときはこの表で置き場所を決める。

| 挙動の種類 | 使う手段 | この vault での実体 |
| --- | --- | --- |
| 横断的な事実・方針（常時保持） | root `CLAUDE.md` | Intent ＋ 横断 Contract ＋ 索引（<200 行を維持） |
| path 固有の「満たすべき形」 | **rules**（`.claude/rules/*.md` ＋ `paths:`） | `inbox-notes` / `daily-briefs` / `concept-pages` |
| 再利用する手順（作り方） | **skills**（`.claude/skills/<name>/SKILL.md`） | `daily-news` / `weekly-digest` / `nightly-link-check` / `skill-improver` |
| 決定論的な強制（必ず / 禁止） | **hooks**（`settings.json` ＋ スクリプト） | `validate_inbox_note.py`（PostToolUse、exit 2 で自己修正） |
| 隔離した重い副作業 | subagents | 今回は未導入（将来: 多ソース検索の隔離など） |
| 読者向けの一行説明 | 各 `index.md` 層宣言 | 公開サイト用 |

### 用語のズレ（重要）

この vault は歴史的に「hooks」「skills」を緩く使ってきた。記事の正式な定義と区別する:

- `.claude/hooks/*.py`（`check_note_links.py` / `post_*_to_slack.py`）は、記事の言う lifecycle hook **ではなく**、routine / CI が呼ぶ **実体スクリプト**。
- 記事の言う正式 **hook** は `settings.json` の `PostToolUse` 等に登録するもの。この vault では `validate_inbox_note.py` がそれ。
- `.claude/skills/<name>/SKILL.md` は frontmatter（`description` / `when_to_use`）を持つ正式 **Skill**（`/command`・自動マッチ可）。`skill-improver` は `disable-model-invocation: true` で unattended 専用。

### ICM 層との対応

- rules / skills / hooks はいずれも **Mechanism 層**の道具。Contract（CLAUDE.md / rules）と Intent（`_meta` / 概念ページ）を満たす手段にすぎない。
- 非対称ルールは不変: Mechanism（手段の選択・スクリプト都合）が Contract / Intent を黙って書き換えない。変更は上流から。
