---
title: "Solana Foundation × Google Cloud、AI エージェント向け x402 決済ゲートウェイ「Pay.sh」を正式ローンチ"
date: 2026-05-05
source: "Solana 公式 / Decrypt / BanklessTimes"
source_url: "https://solana.com/news/solana-foundation-launches-pay-sh-in-collaboration-with-google-cloud"
entity: "Solana Foundation / Google Cloud"
category: "agentic-commerce"
tags:
  - agentic-commerce
  - x402
  - stablecoin
  - payments
  - protocol
summary: "Solana Foundation と Google Cloud が 2026 年 5 月 5 日、AI エージェント向け x402 ベースの決済ゲートウェイ「Pay.sh」を正式ローンチ。Gemini・BigQuery・Vertex AI などの Google Cloud API を含む 75 以上の API に、USDC on Solana でのサブセント・従量払いを提供。アカウント登録・API キー管理不要で、AI エージェントがリアルタイムで API へのアクセス料金を決済できる。"
implications: "Google Cloud が x402 プロトコルのエコシステムに参入したことで、x402 は『暗号資産プロジェクト』の実験から『メジャークラウドプロバイダーが採用する決済標準』に格上げされた。AWS Bedrock AgentCore Payments（May 7）と合わせて、主要クラウド 2 社が x402 をサポートしたことは事実上の標準化に向けた決定的な出来事。"
follow_up: "Pay.sh の対応 API 数拡大、Google Cloud 以外のクラウドプロバイダーによる x402 採用動向、Solana USDC の決済量推移"
---

## 概要

Solana Foundation と Google Cloud が 2026 年 5 月 5 日、AI エージェント向け決済ゲートウェイ「Pay.sh」を正式ローンチした。Coinbase が開発し現在 Linux Foundation が管轄する x402 プロトコル（HTTP 402 "Payment Required" ステータスコードを活用した機械間決済標準）を基盤とし、Google Cloud の主要 API を含む 75 以上のサービスに対し、USDC on Solana でのサブセント・リアルタイム従量決済を提供する。

## 何が起きたか

- **ローンチ日**：2026 年 5 月 5 日
- **提供元**：Solana Foundation × Google Cloud（共同開発）
- **基盤プロトコル**：x402（Linux Foundation 管轄）・Machine Payments Protocol（MPP）も一部活用
- **対応 API（75 以上）**：
  - Google Cloud API：Gemini、BigQuery、Vertex AI など
  - コミュニティ API 50 以上：ブロックチェーンデータ・クラウドインフラ・開発ツール・AI サービス等
- **決済通貨**：USDC on Solana
- **コスト**：多くの API アクセスがフラクションセント（数分の 1 セント）
- **仕組み**：
  1. AI エージェントが Pay.sh 上の API マーケットプレイスでサービスを検索
  2. リアルタイム価格を確認し、USDC でリクエストごとに即時決済
  3. Google Cloud ベースのプロキシが x402 プロトコルで認証・決済をリアルタイム処理
  4. アカウント登録・API キー管理・サブスクリプション契約は不要
- **差別化点**：AWS AgentCore の支払いは USDC だが、Solana チェーン上の USDC を使うのは Pay.sh が最初の大規模事例

## なぜ重要か

### 決済事業者視点

- Google Cloud が Solana 上の USDC を AI エージェントへの API 課金手段として採用したことは、ステーブルコイン決済がエンタープライズ B2B 課金に組み込まれつつあることを示す。「サブスクリプション中心」から「従量制・マイクロ課金」への B2B 課金モデルの転換を加速させる
- x402 対応 API マーケットプレイスは、PSP にとって新たな「AI エージェント向け決済フロー」の設計参照点となる

### プロダクト視点

- Pay.sh の設計（アカウント不要・API キー不要・リアルタイム USDC 決済）は、AI エージェントが人間の介入なしに外部サービスを利用する際の標準的なインターフェースとなりうる
- Gemini・Vertex AI など生成 AI API への USDC 従量決済は、AI サービスの収益化モデルとして実用段階に入ったことを示す

### 規制 / リスク視点

- Google Cloud という規制準拠の大企業が USDC 決済を採用したことで、機関投資家・企業のステーブルコイン決済リスク評価が大幅に低下する可能性がある
- ただし、エージェント代理決済の送金業法上の位置付けは各国で未確定

## 我々への示唆

- いま検討すべきこと:
  - Pay.sh の API カタログを確認し、自社プロダクトが利用・接続できる API があるか評価する
  - x402 プロトコルの実装仕様を Pay.sh の動作から逆引きし、自社エージェント決済プロダクトへの組み込み要件を整理する
- 後で深掘りすべきこと:
  - Google Cloud API の x402 対応が Google の他サービス（Google Workspace・Google Maps API 等）に拡張されるか
  - Pay.sh の取引量データ（Agentic.market の 1.65 億件と比較した際のスケール感）
- 今は優先度が低いこと:
  - Solana 以外のチェーンへの展開（Solana 上の USDC で十分なユースケースが多い）

## 未解決の論点

- Pay.sh は x402 と MPP の両方を活用するとされるが、使い分けはどのように行われるか？
- Google Cloud 以外のクラウドプロバイダー（Microsoft Azure・GCP の競合）が x402 を採用するか？
- API プロバイダーの収益分配モデル（Pay.sh プラットフォームフィーの詳細）は？
- 日本の AI 企業・スタートアップが Pay.sh を利用できる地理的制約はあるか？

## 参考リンク

- 一次情報:
  - [Solana Foundation 公式発表 — Pay.sh ローンチ](https://solana.com/news/solana-foundation-launches-pay-sh-in-collaboration-with-google-cloud)
- 補足情報:
  - [Decrypt — Solana and Google Cloud launch stablecoin payments service for AI agents](https://decrypt.co/366876/solana-google-cloud-launch-stablecoin-payments-service-ai-agents)
  - [BanklessTimes — Solana and Google Cloud Launch Pay.sh for AI Agent Micropayments](https://www.banklesstimes.com/articles/2026/05/06/solana-and-google-cloud-launch-pay-sh-for-ai-agent-micropayments/)
  - [crypto.news — Stablecoins enter AI payments as Solana and Google launch Pay.sh](https://crypto.news/stablecoins-enter-ai-payments-as-solana-and-google-launch-pay-sh/)
  - [関連ノート：x402 Foundation Linux Foundation 移管（2026-04-02）](2026-04-02_x402-Foundation_linux-foundation-launch.md)
  - [関連ノート：Coinbase Agentic.market × x402（2026-04-21）](2026-04-21_Coinbase-x402_agentic-market-launch.md)
  - [関連ノート：AWS Bedrock AgentCore Payments × x402（2026-05-07）](2026-05-07_AWS_bedrock-agentcore-payments-x402.md)

## 重要度

- High

## 確からしさ

- High
