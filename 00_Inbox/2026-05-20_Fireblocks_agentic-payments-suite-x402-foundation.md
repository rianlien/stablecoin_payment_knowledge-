---
title: "Fireblocks、Agentic Payments Suite をローンチし x402 Foundation に参加"
date: 2026-05-25
source: PR Newswire / Fireblocks Blog
source_url: https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html
entity: Fireblocks
category: agentic-payments-infrastructure
primary_category: agentic-commerce
article_published_date: 2026-05-20
underlying_event_date: 2026-05-20
primary_source_date: 2026-05-20
tags:
  - agentic-commerce
  - x402
  - stablecoin-infrastructure
  - agent-payments
  - PSP
summary: "Fireblocks が AI エージェント向け決済インフラ「Agentic Payments Suite」を正式ローンチし、同時に x402 Foundation（Linux Foundation ホスト）にも参加。PSP 向け Agentic Payments Gateway とフィンテック向け Agent Wallets の 2 製品を提供し、あらゆるステーブルコイン・チェーンに対応する中立的なインフラとして設計。x402 プロトコルにはリクエスト完全性と支出ガバナンスを追加するセキュリティ拡張を提供する。"
implications: "Fireblocks の参加により x402 Foundation に $14 兆超のデジタル資産取引実績を持つ機関グレードの企業が加わり、エンタープライズ採用の信頼性が向上。PSP が自社加盟店向けにエージェント決済受け入れを white-label で展開できる仕組みは、x402 エコシステムの加盟店側展開を加速させる可能性がある。"
importance: High
confidence: High
follow_up: "Agentic Payments Gateway の PSP 採用状況・提携 PSP 名・ローンチ時期、Agent Wallets の MPC + Policy Engine の技術仕様と既存 Fireblocks カストマー向けの移行パス、x402 セキュリティ拡張の仕様公開時期と x402 Foundation での採択プロセス"
---

## 概要

- Fireblocks（機関向けデジタル資産プラットフォーム、$14 兆超取引実績）が 2026 年 5 月 20 日に Agentic Payments Suite をローンチし、同日 x402 Foundation に参加した
- Suite は PSP 向け「Agentic Payments Gateway」とフィンテック向け「Agent Wallets」の 2 製品で構成
- x402 Foundation 参加と同時に、リクエスト完全性（request integrity）と支出ガバナンス（spend governance）を x402 プロトコルに追加するセキュリティ拡張を提供

## 何が起きたか

- Fireblocks が AI エージェントによるステーブルコイン決済向けのフルスタックインフラ「Agentic Payments Suite」を正式リリース
- 製品 1：**Agentic Payments Gateway** — PSP が white-label で加盟店に提供できる x402 対応ファシリテーター。加盟店は x402 または MPP 対応のエージェント決済を受け入れ可能
- 製品 2：**Agent Wallets** — フィンテックが自社エンドユーザーに提供できるプログラマブルウォレット。MPC 技術で自己カストディを維持しながら、支出上限・加盟店許可リスト・時間制限などを Policy Engine で強制執行。エージェントへの委任は取り消し可能（revocable permission）
- x402 セキュリティ拡張はマンインザミドル再ルーティング防止とプロトコルレベルの支出ガバナンスを追加する

## 確認された事実

- Fireblocks 共同創業者 Idan Ofrat が「10 億人超が AI アシスタントを日常使用しており、その一部が支出権限をエージェントに委任するだけでステーブルコイン流通速度は大きく増加する」とコメント（出典：PR Newswire）
- Suite は「チェーンおよびステーブルコイン非依存（chain and stablecoin agnostic）」で設計、Fireblocks 既存顧客向けの Policy Engine・KYT・Travel Rule・MPC カストディ・共同署名ガバナンスを統合
- x402 Foundation は Linux Foundation がホストするガバナンス機関。Fireblocks 参加で主要メンバーには AWS・Google・Visa・Coinbase・Stripe が名を連ねることになる

## なぜ重要か

### 決済事業者視点
- Fireblocks の Agentic Payments Gateway は PSP が自社インフラを変えずにエージェント決済受け入れを加盟店に展開できる仕組みを提供。従来は各 PSP が独自に x402 ファシリテーターを構築する必要があったが、white-label 化により展開コストが大幅に低下する

### 加盟店視点
- PSP 経由で Fireblocks ゲートウェイを導入すれば、カード決済や銀行振込と同様のフローでエージェント決済受け入れを追加できる（別途 x402 実装不要）

### プロダクト視点
- Agent Wallets の MPC + Policy Engine の組み合わせは、エージェントへの支出委任を安全に実装する際のリファレンス設計として参考になる。「ユーザーが保有する自己カストディ＋エージェントへのスコープ付き委任」というトラストモデルが機関品質で実装されている

### 規制 / リスク視点
- KYT（Know Your Transaction）・Travel Rule・AML 機能が Suite に統合されており、GENIUS Act PPSI 基準への適合を意識した設計。既存 Fireblocks 顧客（銀行・フィンテック）にとってコンプライアンスの観点でハードルが低い

## 我々への示唆
- いま検討すべきこと:
  - Agentic Payments Gateway の PSP パートナー発表を追跡。自社が利用する PSP が提携すれば、x402 対応を自前実装せずに受け入れ側になれる
  - Agent Wallets の Policy Engine がどのパラメーターをオンチェーン vs. オフチェーンで管理するかを確認——自社のエージェント委任設計の参照に使えるか
- 後で深掘りすべきこと:
  - Fireblocks の x402 セキュリティ拡張の技術仕様（GitHub / x402 Foundation 公式ドキュメント）
  - Gateway の手数料体系・加盟店側の導入要件
- 今は優先度が低いこと:
  - Fireblocks 既存顧客でない企業にとっての即時採用メリットは限定的——PSP 経由展開の具体例が出てから再評価

## ありそうな示唆
- Fireblocks の参加で x402 Foundation が「Coinbase 主導の技術標準」から「業界横断的なガバナンス機関」としての性格を強める。今後 Stripe MPP との競合ではなく「x402 vs. MPP」という形で収斂するかもしれない
- MPC + Policy Engine による委任型決済は GENIUS Act 下でのエージェント ID とウォレット紐づけの一つの実装解になりうる

## 推測 / 監視ポイント
- Agentic Payments Gateway が x402 だけでなく MPP（Machine Payments Protocol）も「中立的に」サポートするかは未確認——将来的な標準統合の試金石
- x402 セキュリティ拡張が Coinbase の公式 x402 仕様に組み込まれるのか、Fireblocks 独自の実装として並走するのかは未確定
- 現在 x402 30 日ボリュームが $24.2M という数字（Keyrock 報告）は、Fireblocks の参加でどう変化するか

## 未解決の論点
- Agentic Payments Gateway の提携 PSP は誰か（発表済みパートナーが存在するか）
- Agent Wallets の「revocable permission」はどのトリガーで取り消されるか——ユーザー手動か、ポリシー自動か
- EU MiCA / EU AI Act との整合性（Fireblocks は欧州でも大手顧客を持つ）

## 参考リンク
- 一次情報: [PR Newswire（2026-05-20）](https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html)
- 補足情報: [The Paypers（2026-05-20）](https://thepaypers.com/payments/news/fireblocks-launches-agentic-payments-suite-for-stablecoin-transactions), [Cointelegraph（2026-05-20）](https://coinspectator.com/cointelegraph/2026/05/20/fireblocks-launches-agentic-payment-support-joins-x402-foundation/)

## 重要度
- High

## 確からしさ
- High
