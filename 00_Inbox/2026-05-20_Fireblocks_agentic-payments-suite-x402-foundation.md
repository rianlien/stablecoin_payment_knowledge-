---
title: "Fireblocks、Agentic Payments Suite をローンチし x402 Foundation に参加——PSP 向けゲートウェイ・ユーザー向けエージェントウォレットで send/receive の全ライフサイクルをカバー"
date: 2026-05-20
source: "PR Newswire / CoinTelegraph / TipRanks"
source_url: "https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html"
entity: "Fireblocks"
category: "agentic-payments-infrastructure"
primary_category: "x402"
article_published_date: 2026-05-20
underlying_event_date: 2026-05-20
primary_source_date: 2026-05-20
tags:
  - x402
  - agent-payments
  - PSP
  - agentic-commerce
  - stablecoin-infrastructure
summary: "Fireblocks が Agentic Payments Suite（Agentic Payments Gateway + Agentic Wallets）を発表し、x402 Foundation（Linux Foundation ホスト）にセキュリティ拡張コントリビューターとして参加。PSP が加盟店向けにステーブルコイン受取を提供できるゲートウェイと、エンドユーザーが AI エージェントに安全に決済権限を委任できるウォレットで、エージェント決済の送受信ライフサイクル全体をカバーする。任意ステーブルコイン・任意チェーン対応、x402・MPP 両プロトコルをサポート。"
implications: "機関向け最大手デジタル資産カストディアン（取引額累計 $14 兆）が x402 エコシステムに参加し、PSP・フィンテック向けのエンタープライズグレードのエージェント決済インフラが整備された。x402 Foundation の構成員に Google・Microsoft・Visa・Coinbase・Fireblocks が揃い、業界標準としての地位がさらに確固化。"
importance: High
confidence: High
follow_up: "Agentic Payments Gateway の PSP 向け具体的な料金モデル・AML コンプライアンスの実装詳細、Agentic Wallets のスマートコントラクト設計（マルチシグ構成・支出ポリシーのオンチェーン格納方式）、x402 セキュリティ拡張の技術仕様（request integrity の署名方式・spend governance のポリシー表現形式）、MPP（Stripe/Tempo）との同時サポートの実装詳細"
---

## 概要

2026 年 5 月 20 日、デジタル資産カストディ・決済インフラ大手の Fireblocks が Agentic Payments Suite を発表し、同時に x402 Foundation（Linux Foundation ホスト）にセキュリティ拡張のコントリビューターとして参加した。Suite は「エージェントが送金する側（Agentic Wallets）」と「マーチャントが受け取る側（Agentic Payments Gateway）」の両レイヤーを一体でカバーし、PSP・フィンテックが既存インフラに追加できる形で設計されている。

## 何が起きたか

- **Agentic Payments Gateway**：PSP がカード決済や銀行振込と同様に、加盟店向けステーブルコイン受取を提供できるインフラ。ブロックチェーン専門知識不要。エージェントからのインバウンド決済は Fireblocks ウォレットまたは連携口座に直接ルーティングされ、コンプライアンス・セキュリティが組み込み済み
- **Agentic Wallets**：フィンテックがエンドユーザーにプログラマブルウォレットを提供する基盤。ユーザーが AI エージェントに安全に決済権限を委任できる設計。エージェントは定義済みの支出上限内で x402 または MPP に対応した加盟店への支払いと署名を実行可能。完全な監査証跡付き
- **x402 Foundation 参加**：request integrity（リクエスト整合性）と spend governance（支出ガバナンス）を付加するセキュリティ拡張を x402 に貢献。既存メンバーは Google・Microsoft・Visa・Coinbase
- **プロトコル非依存設計**：任意ステーブルコイン・任意チェーンに対応。x402 と MPP の両標準をサポートし、エコシステムの変化に追従できる設計
- **フルライフサイクルカバレッジ**：オフランプ・通貨変換・会計照合を単一プラットフォームで処理。規制当局・監査人に説明できる構造化されたセトルメントデータを生成

## 確認された事実

- 発表日：2026 年 5 月 20 日（PR Newswire / CoinTelegraph）
- Fireblocks は累計 $14 兆超のデジタル資産取引をセキュアしたエンタープライズ向け最大手カストディアン
- Agentic Payments Gateway：PSP 向け加盟店ステーブルコイン受取インフラ、ブロックチェーン専門知識不要
- Agentic Wallets：エンドユーザーが AI エージェントへ支出上限付きで決済権限を委任できるプログラマブルウォレット
- x402 Foundation 参加：セキュリティ拡張（request integrity・spend governance）を提供
- 任意ステーブルコイン・任意チェーン・x402・MPP 対応を公式に表明
- x402 Foundation の他のメンバー：Google・Microsoft・Visa・Coinbase

## なぜ重要か

### 決済事業者視点

- PSP が「ブロックチェーン専門知識なし」で加盟店向けステーブルコイン受取を提供できる具体的なプロダクトが登場した。カード決済・銀行振込と並ぶ「第三の決済レール」としてエージェント決済を加盟店ポートフォリオに追加できる可能性がある
- x402 と MPP の両方をサポートするプロトコル非依存設計は、PSP にとって「どの標準が勝つかを決めずに参入できる」リスクヘッジになる

### 加盟店視点

- Fireblocks のブランドとコンプライアンス体制（AML・OFAC スクリーニング組み込み）は、規制対応が厳格な金融機関・大手企業の加盟店にとって採用障壁を大幅に下げる可能性がある
- 「エージェントからの決済が Fireblocks 経由で来る」という事実は、機関投資家・企業が B2B API サービスのエージェント決済受取を始める際の信頼の担保になる

### プロダクト視点

- Agentic Wallets の「スマートコントラクト + 支出上限 + 監査証跡」設計は、CFES が提言した「認可範囲の確認・責任帰属」フレームワーク（2026-05-13 既報）と方向性が一致する
- x402 セキュリティ拡張（request integrity）は、API 応答のなりすまし・中間者攻撃を防ぐ署名検証機能と推定される。これが x402 標準に組み込まれれば、プロトコル全体のセキュリティレベルが向上する

### 規制 / リスク視点

- Fireblocks の AML・コンプライアンス体制が Gateway に組み込まれている点は、GENIUS Act 施行後に求められる「決済事業者の AML 義務」への対応を示唆する
- x402 Foundation が Linux Foundation ホストである点は、OSS ガバナンス標準に従う非営利ガバナンスを意味し、特定企業による囲い込みリスクを低下させる

## 我々への示唆

- いま検討すべきこと:
  - Agentic Payments Gateway の PSP 向け API 仕様・審査要件を確認し、自社が加盟店獲得レールとして活用できるか評価する
  - x402 セキュリティ拡張（request integrity・spend governance）の技術仕様が公開されたら、自社の x402 実装へのアップデートが必要かどうかを確認する
- 後で深掘りすべきこと:
  - Agentic Wallets の支出ポリシーとオンチェーンのスマートコントラクト実装（マルチシグ・MPC 等）の詳細
  - Fireblocks Gateway と Circle Agent Marketplace・AWS AgentCore の市場分担——誰が PSP を主要顧客とし、誰がフィンテック・AI 企業を主要顧客とするか
- 今は優先度が低いこと:
  - Fireblocks の価格体系（エンタープライズ向けのためエントリー障壁が高い可能性）

## ありそうな示唆

- Fireblocks が x402 に参加することで、$14 兆規模のカストディネットワークに接続する PSP・フィンテックが自然に x402 対応を検討するようになる。x402 のネットワーク効果が B2B・機関向けセグメントに波及するエンジンとして機能する可能性がある

## 推測 / 監視ポイント

- Fireblocks Gateway が MPP（Stripe/Tempo Machine Payments Protocol）とも正式に統合するかどうか——両プロトコルのサポートを公言しているが、実装の深度は不明
- x402 セキュリティ拡張が x402 コア仕様に取り込まれる時期と、Coinbase CDP ファシリテーターとの互換性
- 既存の Fireblocks 顧客（大手 PSP・フィンテック・機関投資家）が Agentic Payments Gateway を早期採用する事例が出るか

## 未解決の論点

- Agentic Wallets の「defined limits（支出上限）」のポリシー表現形式——オンチェーンのスマートコントラクトか、Fireblocks のオフチェーンポリシーエンジンか
- AML コンプライアンスの具体的な実装——OFAC スクリーニングをエージェントの支払いごとにリアルタイムで行う場合の処理レイテンシが問題にならないか
- Fireblocks 自身の GENIUS Act PPSI ステータス（カストディアンとしての位置づけ）

## 参考リンク

- 一次情報: [PR Newswire（2026-05-20）](https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html)
- 補足情報: [CoinTelegraph（2026-05-20）](https://cointelegraph.com/news/fireblocks-launches-agent-payment-support-for-ai-agents) / [TipRanks（2026-05-20）](https://www.tipranks.com/news/private-companies/fireblocks-launches-agentic-payments-suite-to-power-stablecoin-based-ai-transactions) / [Fireblocks 公式ページ](https://www.fireblocks.com/solutions/agentic-digital-asset-infrastructure)

## 重要度

- High

## 確からしさ

- High（PR Newswire 公式リリース + CoinTelegraph・TipRanks 等複数媒体で確認）
