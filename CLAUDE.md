# Stablecoin Payments Research Repo

## Default
- この repo は stablecoin / agentic commerce 関連の調査ノート蓄積用
- 本文は自然な日本語、YAML key は英語
- 固有名詞、会社名、規格名、法令名は必要に応じて原文維持

## Paths
- ニュース: `/00_Inbox/`
- Daily Brief: `/01_Daily-Briefs/YYYY-MM/`
- Weekly: `/02_Weekly/`
- Topics / MOC: `/03_Topics/`
- Protocol research: `/04_Protocols/`
- Entities / Companies: `/06_Entities/Companies/`
- テンプレート: `/90_Templates/`

## Common rules
- 1ニュース1ファイル
- 既存ノート確認後に作成し、同一イベントの重複作成は避ける
- 重要な続報、正式ローンチ、規制変更、標準更新は別ノート化してよい
- 事実と解釈を分け、推測は推測と明記し、出典リンクを残す
- 重要度と確からしさを分けて評価する
- 既存タグ優先、tags は 3〜5 個
- 変更は review しやすい形を優先し、原則 direct commit しない

## Daily agentic-commerce routine defaults
- JST の今日を基準に `start_date=today-7 days`、`end_date=today`
- 採用基準は `underlying_event_date`
- `article_published_date` が期間内でも underlying event が期間外なら除外
- 日付が曖昧な項目は、一次情報で裏どりできない限り除外
- 主対象: agentic commerce, agent payments, payment authorization, agent identity, merchant / PSP readiness, API billing, machine payments, payment-related protocol / standard
- stablecoin 項目は、agent-led commerce / machine payments / API billing / x402 / AP2 などに直接関係する場合のみ採用
- 一般 AI ニュース、一般 stablecoin ニュース、価格動向、意見記事、古い発表の再報道は除外
- 既存 `/00_Inbox/` と `/01_Daily-Briefs/` を見て重複回避
- 新規ノートは 1 run で最大 10 件。重要項目が少なければ無理に埋めない
- ニュースノートは `/90_Templates/news_note_template.md`、Daily Brief は `/90_Templates/daily_brief_template.md`
- ニュースノートには `article_published_date`、`underlying_event_date`、`primary_source_date` を記録
- confirmed facts / likely implications / speculation-watch を分ける
- Daily Brief にはその run で新規採用した項目だけを書き、`/01_Daily-Briefs/YYYY-MM/YYYY-MM-DD.md` に保存する
- 重要項目がない日も Daily Brief を作成または更新し、「該当なし」と明記する

## Weekly defaults
- 週次まとめは毎週月曜日に、直前の暦週（月曜〜日曜）を対象に作成
- 元データは `/00_Inbox/` と `/01_Daily-Briefs/`
- 事実の羅列より、変化の方向性、示唆、監視ポイントを優先
- 重複話題は統合して `/02_Weekly/` に保存
