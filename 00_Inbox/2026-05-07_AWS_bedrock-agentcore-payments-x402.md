---
title: "Amazon Bedrock AgentCore Payments プレビュー：AWS が Coinbase（x402）・Stripe（Privy）と AI エージェント向けステーブルコイン決済インフラを発表"
date: 2026-05-07
source: "AWS 公式ブログ / CoinDesk / The Block"
source_url: "https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/"
entity: "Amazon Web Services / Coinbase / Stripe"
category: "agentic-commerce"
tags:
  - agentic-commerce
  - x402
  - stablecoin
  - payments
  - protocol
summary: "AWS が Amazon Bedrock AgentCore Payments（プレビュー）を 2026 年 5 月 7 日に発表。Coinbase（x402 プロトコル）と Stripe（Privy ウォレット）を基盤とし、AI エージェントが API・ウェブコンテンツ・MCP サーバー等へのアクセスを USDC で自律的に支払えるインフラを提供。エージェントの推論ループを中断せず HTTP 402 ネゴシエーション・ウォレット認証・ステーブルコイン決済・証明配送を自動処理する。"
implications: "主要クラウドプロバイダーが x402 プロトコルをネイティブサポートしたことで、x402 が事実上のエージェント決済標準として確立される可能性が高まった。Stripe MPP と x402 の並走構図において、AWS が x402 側に立ったことは重要な分岐点。"
follow_up: "GA タイムライン、ホテル予約等の大型トランザクション対応時期、Warner Bros. Discovery 等のアーリーアダプター事例、Stripe MPP との統合または競合の方向性"
---

## 概要

Amazon Web Services（AWS）が 2026 年 5 月 7 日、Amazon Bedrock AgentCore Payments のプレビューを発表した。Coinbase と Stripe を決済パートナーとして採用し、AI エージェントがステーブルコイン（USDC）を用いて API・ウェブコンテンツ・MCP サーバー・他エージェントへのアクセス料金を自律的に支払えるインフラを提供する。x402 プロトコル（Coinbase が開発し現在は Linux Foundation 管轄）を基盤とし、Stripe の Privy ウォレットも接続オプションとして提供。

## 何が起きたか

- **発表日**：2026 年 5 月 7 日（プレビュー開始）
- **提供元**：AWS（Amazon Bedrock AgentCore の新機能として追加）
- **決済パートナー**：Coinbase（x402 プロトコル・USDC 流動性）/ Stripe（Privy ウォレット）
- **開発者の選択肢**：Coinbase ウォレットまたは Stripe Privy ウォレットの 2 択で AgentCore に接続
- **対象ユースケース**：
  - API への従量アクセス（AI 推論・データフィード・ブロックチェーンデータ等）
  - ウェブコンテンツのペイウォール突破
  - MCP サーバーへの接続料金
  - エージェント間取引（agent-to-agent payments）
- **今後の拡張計画**：ホテル予約・旅行手配・加盟店支払い等の大型トランザクション対応を予定
- **動作仕組み**：
  1. エージェントが有料リソースにアクセスすると HTTP 402 レスポンスを受信
  2. AgentCore が x402 プロトコルネゴシエーション・ウォレット認証・USDC 決済・支払い証明配送を自動処理
  3. エージェントの推論ループは中断されず、決済は透過的に完了する
  4. 支出上限はインフラ層で決定論的に強制（スマートコントラクトレベル）
  5. 全取引は AgentCore の既存ログ・メトリクス・トレースで可視化
- **アーリーアダプター**：Warner Bros. Discovery が早期テストに参加

## なぜ重要か

### 決済事業者視点

- 主要クラウドプロバイダー（AWS）が x402 プロトコルをネイティブサポートしたことで、x402 が「AI エージェント向け決済の HTTP 標準」として実質的に確立されつつある。AWS が採用したプロトコルは短期間で業界標準になる傾向があり、影響は大きい
- Stripe Privy ウォレットが AWS インフラに組み込まれたことで、PSP としての Stripe が決済レイヤー争いにおいてさらに有利なポジションを獲得

### プロダクト視点

- AI エージェントが「ユーザーの事前承認のもとで自律的に USDC を支払う」フローが AWS インフラとして標準化されることは、エージェント決済プロダクトの設計において参照すべきアーキテクチャを提供する
- 支出上限をインフラ層で強制するモデルは、従来のカード決済の承認モデルに近い。この設計思想はリスク管理・コンプライアンスの観点からも採用しやすい

### 規制 / リスク視点

- 現時点ではプレビュー段階。GA 前に KYC/AML 要件・スペンディングリミット規制対応・エージェント識別の枠組みが追加される可能性がある
- AWS・Coinbase・Stripe という 3 社の規制対応が揃っているため、機関採用への障壁は相対的に低い

## 我々への示唆

- いま検討すべきこと:
  - x402 プロトコルが AWS・Google Cloud・Coinbase に採用された事実を踏まえ、自社エージェント決済プロダクトが x402 対応を優先事項とする判断を固める時期に来た
  - AgentCore Payments の API 仕様・ウォレット接続モデル・支出上限の設計を分析し、自社プロダクトの参照アーキテクチャとして評価する
- 後で深掘りすべきこと:
  - GA タイムラインと大型トランザクション対応スケジュール（B2B 支払い・ホテル予約等）
  - Stripe MPP と x402 の技術的位置付けが AgentCore の文脈でどう整理されるか
  - Warner Bros. Discovery の実運用事例の詳細（ユースケース・決済金額・API 種別）
- 今は優先度が低いこと:
  - Solana 以外のチェーン対応（現時点では USDC/x402 中心で十分）

## 未解決の論点

- AgentCore Payments の GA タイムラインはいつか？
- 大型トランザクション（旅行・加盟店支払い）対応時に、KYC 要件はどう変わるか？
- Stripe MPP が x402 との共存でどう位置付けられるか（MPP は x402 の上位層か、代替標準か）？
- エージェントの「代理支払い」に関する米国の送金業法上の解釈はどうなるか？

## 参考リンク

- 一次情報:
  - [AWS 公式ブログ — Introducing Amazon Bedrock AgentCore payments](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/)
  - [AWS What's New — AgentCore Payments Preview](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/)
- 補足情報:
  - [CoinDesk — Amazon rolls out AI agent stablecoin payments platform](https://www.coindesk.com/business/2026/05/07/amazon-rolls-out-ai-agent-stablecoin-payments-platform-with-coinbase-and-stripe)
  - [The Block — AWS taps Coinbase and Stripe to power USDC payments for AI agents](https://www.theblock.co/post/400421/aws-taps-coinbase-and-stripe-to-power-usdc-payments-for-ai-agents)
  - [関連ノート：x402 Foundation Linux Foundation 移管（2026-04-02）](2026-04-02_x402-Foundation_linux-foundation-launch.md)
  - [関連ノート：Coinbase Agentic.market × x402（2026-04-21）](2026-04-21_Coinbase-x402_agentic-market-launch.md)
  - [関連ノート：Stripe Sessions 2026 MPP・エージェント決済（2026-04-30）](2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments.md)

## 重要度

- High

## 確からしさ

- High
