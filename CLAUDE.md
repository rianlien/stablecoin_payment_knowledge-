# Stablecoin Payments Research Repo

この repo は **Intent → Contract → Mechanism** の一方向で組み立てる。
**非対称ルール: Mechanism（実装・スクリプトの都合）が Contract / Intent を黙って書き換えてはいけない。** 変えるときは上流から。
設計思想の全体は [`_meta/PHILOSOPHY.md`](_meta/PHILOSOPHY.md)、配線図は [`_meta/ARCHITECTURE.md`](_meta/ARCHITECTURE.md)。

---

## Intent — 目的と意図的制約

なぜ集めるか / 何を捨てるか。再生成できない北極星。

- この repo は stablecoin / agentic commerce 関連の調査ノートを、チームで再利用可能な資産として蓄積する。
- 本文は自然な日本語、YAML key は英語。固有名詞・会社名・規格名・法令名は必要に応じて原文維持。
- **主対象**: agentic commerce, agent payments, payment authorization, agent identity, merchant / PSP readiness, API billing, machine payments, payment-related protocol / standard。
- **stablecoin 項目**は、agent-led commerce / machine payments / API billing / x402 / AP2 などに直接関係する場合のみ採用。
- **除外**: 一般 AI ニュース、一般 stablecoin ニュース、価格動向、意見記事、古い発表の再報道。
- 保護資産は `03_Topics` / `05_MOCs` の論点枠組みと各ノートの「我々への示唆」。事実は再収集できるが、視座は失うと戻らない。

---

## Contract — ノート・出力・リンクの約束

外から見て満たすべき形と境界。テンプレートは `/90_Templates/`。

### Paths
- ニュース: `/00_Inbox/`
- Daily Brief: `/01_Daily-Briefs/YYYY-MM/`
- Weekly: `/02_Weekly/`
- Topics / MOC: `/03_Topics/`、`/05_MOCs/`
- Protocol research: `/04_Protocols/`
- Entities: `/06_Entities/Companies/`、`/Networks/`、`/Organizations/`
- テンプレート: `/90_Templates/`

### ノート品質
- 1ニュース1ファイル。既存ノート確認後に作成し、同一イベントの重複作成は避ける。
- 重要な続報、正式ローンチ、規制変更、標準更新は別ノート化してよい。
- **事実と解釈を分け、推測は推測と明記し、出典リンクを残す。**
- 重要度（importance）と確からしさ（confidence）を分けて評価する。
- confirmed facts / likely implications / speculation-watch を分ける。
- 既存タグ優先、tags は 3〜5 個。
- 層はディレクトリ位置と frontmatter で識別する（概念ページは `type:`、news は `category` / `primary_category`）。新しい層フィールドは発明しない。
- 変更は review しやすい形を優先し、原則 direct commit しない（PR 経由）。

### path 別 Contract（rules に委譲）
ファイル種別ごとの「満たすべき形」は `paths:` でスコープした rule に置く（該当ファイル編集時に自動ロード）:
- Inbox ニュースノート → [`.claude/rules/inbox-notes.md`](.claude/rules/inbox-notes.md)（必須 frontmatter・ファイル名・来歴。`validate_inbox_note.py` hook が機械検証）
- Daily Brief → [`.claude/rules/daily-briefs.md`](.claude/rules/daily-briefs.md)（リンク形式・該当なし・翌日追記）
- 概念ページ（Topics / Protocols / MOCs / Entities） → [`.claude/rules/concept-pages.md`](.claude/rules/concept-pages.md)（紐付けテーブル・根拠ノート）

### 非対称ルール（コンテンツ層）と来歴
- 新しい事実（`00_Inbox`）が `03_Topics` / `05_MOCs` の既存の枠組みと矛盾する場合、枠組みを黙って上書きしない。矛盾を当該ページ上で surface（明示）して残す。
- 来歴: news note は `source_url` ＋ 3日付で一次情報まで遡れ、概念ページは根拠ノートを下向きに紐付ける。

### Daily routine 判定パラメータ
- JST の今日を基準に `start_date=today-7 days`、`end_date=today`。
- 採用基準は `underlying_event_date`。`article_published_date` が期間内でも underlying event が期間外なら除外。
- 日付が曖昧な項目は、一次情報で裏どりできない限り除外。
- 既存 `/00_Inbox/` と `/01_Daily-Briefs/` を見て重複回避。
- 新規ノートは 1 run で最大 10 件。重要項目が少なければ無理に埋めない。

### Weekly 出力
- 毎週月曜日に、直前の暦週（月曜〜日曜）を対象に作成。元データは `/00_Inbox/` と `/01_Daily-Briefs/`。
- 事実の羅列より、変化の方向性・示唆・監視ポイントを優先。重複話題は統合して `/02_Weekly/` に保存。

---

## Mechanism — 実装への参照

どう実現するか。詳細はここに直書きせず、手段別に委譲する（使い分けの決定表は [`_meta/ARCHITECTURE.md`](_meta/ARCHITECTURE.md) §5）:
- **rules**（path 固有 Contract）: `.claude/rules/*.md`
- **skills**（手順）: `.claude/skills/<name>/SKILL.md`、実行プロンプトは `.claude/prompts/*.txt`
- **hooks**（決定論的強制）: `.claude/settings.json` ＋ `.claude/hooks/validate_inbox_note.py`
- **スクリプト / CI**: `.claude/hooks/*.py`（routine・CI が呼ぶ実体）、`mkdocs.yml`、`.github/workflows/`

**Mechanism の都合をこの CLAUDE.md（Contract / Intent）に無印で持ち込まない。** 必要なら抽象化して Contract に昇格し、具体理由は Mechanism 側に置く。
