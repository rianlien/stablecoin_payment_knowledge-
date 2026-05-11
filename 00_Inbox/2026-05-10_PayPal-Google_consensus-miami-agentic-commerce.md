---
title: "PayPal と Google Cloud が Consensus Miami で「エージェンティックコマースはクリプトレールで動く」と表明——加盟店の 95% がエージェントトラフィックを確認も機械読取カタログ整備は 20% 止まり"
date: 2026-05-10
source: "CoinDesk / CoinSpectator"
source_url: "https://www.coindesk.com/business/2026/05/10/agentic-commerce-will-run-on-crypto-rails-paypal-and-google-reps-tell-consensus-miami"
entity: "PayPal / Google Cloud"
category: "agentic-commerce"
tags:
  - agentic-commerce
  - merchant
  - payments
  - agent-identity
summary: "2026 年 5 月 10 日、Consensus Miami のパネルで PayPal と Google Cloud の幹部がエージェンティックコマースはクリプトレールを基盤とする必要があると公言。PayPal の Agentic Commerce Pulse Report（2026 年 3 月）の調査結果として、加盟店の 95% が AI エージェントトラフィックを確認する一方、機械読取可能なカタログを整備済みの加盟店は 20% に止まることが示された。Google Cloud は Cloud KMS の暗号資産カストディへの拡張を表明。PayPal は PYUSD をエージェント決済の自然なプログラマブル決済レイヤーと位置付けた。"
implications: "大手決済事業者（PayPal）と主要クラウドプロバイダー（Google Cloud）の両者が公式にクリプトレールの必要性を認めたことで、エージェント決済の業界コンセンサスが加速。加盟店の機械読取カタログ整備が最大のボトルネックであることが定量的に示された。"
follow_up: "PayPal のエージェント向けチェックアウト API の詳細仕様、Google Cloud KMS 暗号資産カストディ機能の GA タイムライン、加盟店カタログ整備を加速する業界イニシアチブ"
---

## 概要

2026 年 5 月 10 日、CoinDesk 主催の Consensus Miami 2026 カンファレンスのパネルセッションで、PayPal の May Zabaneh（SVP・暗号資産担当 GM）と Google Cloud の Richard Widmann（Web3 グローバル戦略ヘッド）が、エージェンティックコマースはクリプトレールを基盤とする必要があると公言した。両者は AI エージェントが従来の銀行口座を取得できないという構造的な制約を指摘し、クリプトウォレット・ステーブルコインが不可欠なインフラであると主張した。

## 何が起きたか

- **イベント日**：2026 年 5 月 10 日（Consensus Miami 2026 パネルセッション）
- **underlying_event_date**：2026-05-10
- **article_published_date**：2026-05-10（CoinDesk）
- **primary_source_date**：2026-05-10（Consensus Miami セッション）
- **登壇者**：
  - May Zabaneh（PayPal・SVP 兼 暗号資産担当 GM）
  - Richard Widmann（Google Cloud・Web3 グローバル戦略ヘッド）

### 主な発言内容

**Google Cloud（Richard Widmann）**：
- 「AI エージェントは銀行口座を取得できない。難しいのではなく、構造的に不可能だ」（技術的・規制的障壁を理由に挙げる）
- 既存のインターネットユーザー体験は自律エージェントに拡張できない
- Google Cloud の Cloud KMS（鍵管理サービス）を暗号資産カストディ向けに拡張する計画を言及
- マルチパーティカストディがエージェント設計の中心になると指摘（エージェントは鍵シャードの 1 つのみを保持すべき）

**PayPal（May Zabaneh）**：
- PayPal はエージェントを「次のコマースチャネル」と位置付け（オフライン → オンライン → モバイル → エージェントという進化軸）
- PYUSD（PayPal USD）は「グローバル化・AI ネイティブ体験・トークン化資産の潮流に対して、ごく自然なプログラマブル決済レイヤー」と発言
- AP2（Agent Payments Protocol）を 120 社以上のパートナーと共に推進中

### PayPal Agentic Commerce Pulse Report の調査結果（公開データ）

調査：2026 年 2 月 23 日〜3 月 3 日、米国 498 社の加盟店を対象に実施（売上規模小中大を含む）

| 指標 | 結果 |
|---|---|
| AI エージェントトラフィックを確認している加盟店 | **95%** |
| 機械読取可能なカタログを整備済みの加盟店 | **20%** |

この「95% 対 20%」の乖離は、エージェントがすでに加盟店サイトに到達しているにもかかわらず、加盟店側のデータインフラが追いついていない現状を定量的に示す。

## なぜ重要か

### 決済事業者視点

- PayPal と Google Cloud という決済・クラウドの巨人が同一の場で「クリプトレール不可避論」を公言したことは、エージェント決済インフラをめぐる業界コンセンサスが形成された証左。PSP は x402・AP2・TAP（Visa）等の複数プロトコルへの対応が事実上の必須要件になりつつある
- PayPal が PYUSD をエージェント決済の「プログラマブル決済レイヤー」と明確に位置付けたことで、PYUSD が stablecoin-native PSP 向け API 決済の主要通貨候補として浮上

### 加盟店視点

- 「95% のエージェントトラフィック対 20% の機械読取カタログ」という乖離は、エージェントの購買判断がすでに始まっているにもかかわらず、加盟店側が対応できていないことを意味する。機械読取可能な商品データ・価格・在庫・返品ポリシーを整備しない加盟店は、エージェント経由の購買機会を逃すリスクが高まっている
- これはすなわち、エージェント対応カタログ整備を支援するサービス（プロダクトフィード最適化・スキーママークアップ等）への需要が急増する可能性を示す

### プロダクト視点

- Google Cloud が Cloud KMS を暗号資産カストディに拡張することは、エンタープライズ向けエージェント決済インフラが「クラウドネイティブなカストディ」を前提に設計されていくことを示唆。AWS AgentCore Payments（Stripe Privy ウォレット）と並び、GCP も独自のカストディ層を持つことになる
- マルチパーティカストディ（エージェントは鍵の 1 シャードのみ保持）は、エージェント決済の安全設計パターンとして急速に標準化しつつある

### 規制 / リスク視点

- PayPal がエージェントを「次のチャネル」と位置付けるということは、エージェント経由の取引が PayPal の既存 AML・KYC・消費者保護フレームワーク下で処理されることを意味する。エージェントトラフィックの識別・認証をどう処理するかが次の規制論点になる
- Zabaneh の発言中に AP2 への言及があり、FIDO Alliance 寄贈済みの AP2 が PayPal のエージェント決済戦略の中核プロトコルであることが確認された

## 我々への示唆

- いま検討すべきこと:
  - 自社が加盟店向けサービスを提供している場合、機械読取カタログ整備を支援する仕組み（API・スキーマガイド等）の提供を優先検討する。「95% 対 20%」の乖離はビジネス機会でもある
  - PYUSD が PayPal エージェント決済の中核になる場合、PYUSD 対応を自社決済フローに加えることを検討する
- 後で深掘りすべきこと:
  - PayPal のエージェント向けチェックアウト API の仕様（エージェントが購買意図を示す方法・承認フロー）
  - Google Cloud KMS 暗号資産カストディの GA タイムラインと API 仕様
  - AP2 v0.2.0 の技術仕様と PayPal 統合詳細
- 今は優先度が低いこと:
  - Consensus Miami の他セッションでの個別発表（本ノートの対象外）

## 未解決の論点

- 機械読取カタログを整備していない 80% の加盟店が対応を進めるには何が必要か？誰が整備支援のインセンティブを持つか（PSP か、プラットフォームか、マーケットプレイスか）？
- Google Cloud KMS の暗号資産カストディ拡張はいつ GA となるか？対象チェーンは何か？
- PayPal が「PYUSD = エージェント決済の自然なプログラマブル層」と位置付けることは、x402（USDC ベース）との競合を生むか、共存するか？

## 参考リンク

- 一次情報:
  - [CoinDesk — Agentic commerce will run on crypto rails, PayPal and Google reps tell Consensus Miami（2026-05-10）](https://www.coindesk.com/business/2026/05/10/agentic-commerce-will-run-on-crypto-rails-paypal-and-google-reps-tell-consensus-miami)
  - [PayPal Agentic Commerce Pulse Report（March 2026）](https://www.paypalobjects.com/marketing/GCI_Q1_26_PayPal_Agentic_Pulse_Final_Report.pdf)
- 補足情報:
  - [CoinDesk — Crypto wallets are being rebuilt for AI agents（2026-05-09）](https://www.coindesk.com/business/2026/05/09/crypto-wallets-are-being-rebuilt-for-ai-agents-trust-wallet-and-mesh-executives-say-at-consensus-miami)
  - [関連ノート：Google AP2 FIDO Alliance 寄贈（2026-04-28）](2026-04-28_Google_ap2-fido-alliance.md)
  - [関連ノート：Stripe Sessions 2026 MPP・エージェント決済（2026-04-30）](2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments.md)
  - [関連ノート：Mastercard Q1 2026 Agent-to-Agent Payments（2026-04-30）](2026-04-30_Mastercard_q1-2026-agent-to-agent-payments.md)

## 重要度

- Medium

## 確からしさ

- High（CoinDesk 一次報道・PayPal 公式調査レポートに基づく）
