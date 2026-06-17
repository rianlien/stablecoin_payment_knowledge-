---
title: "x402 エコシステム概観"
type: topic
updated: 2026-06-15
tags:
  - x402
  - agentic-commerce
  - agent-payments
  - micropayments
---

# x402 エコシステム概観

HTTP 402 ステータスコードを使い、AI エージェントが API・コンテンツ・サービスをリクエスト単位で自律的に決済できるプロトコル。Coinbase が OSS として公開し、2026年4月に Linux Foundation へ移管して業界標準化を推進している。

個別プロトコルページ → [[x402]]

---

## エコシステムの構造

```
標準化・ガバナンス
  └ x402 Foundation（Linux Foundation 傘下）
      └ 参加: Google, Microsoft, AWS, Mastercard, Visa, Circle,
              Fireblocks, Polygon Labs, Solana Foundation 等

インフラ・ファシリテーター
  ├ Coinbase CDP facilitator（Base, Solana, Polygon）
  ├ Fireblocks Agentic Payments Suite（x402 Gateway + Wallets）
  └ AWS AgentCore Payments（x402 + Coinbase wallet infrastructure）

アプリケーション・マーケットプレイス
  ├ Agentic.market（x402 対応サービス一覧）
  ├ Cryptorefills（x402 対応チェックアウト）
  └ OpenRouter（AI ルーティング → x402 決済に移行）

決済効率化
  └ x402 Batch Settlement（大量マイクロペイメントを1 Tx に集約）
      └ 関連: [[x402-batch-settlement]]

チェーン拡張
  ├ Base（Coinbase L2、主要環境）
  ├ Arbitrum（2026-05-14 拡張）
  └ AllUnity SEK ステーブルコイン（北欧市場向け）
```

---

## 主要ノード別の位置づけ

### 標準化

| 日付 | ノート | 意味 |
|---|---|---|
| 2026-04-02 | [[2026-04-02_x402-Foundation_linux-foundation-launch]] | [[x402 Foundation]] への移管。業界中立ガバナンスが確立し、特定企業依存を脱する |

### インフラ拡張

| 日付 | ノート | 意味 |
|---|---|---|
| 2026-05-07 | [[2026-05-07_AWS_bedrock-agentcore-payments-x402]] | AWS AgentCore Payments が x402 を正式採用。クラウド側の決済ランタイムとして認知 |
| 2026-05-14 | [[2026-05-14_x402_arbitrum-launch-agent-payments]] | Arbitrum 対応で低コスト L2 でのマイクロペイメントが可能に |
| 2026-05-20 | [[2026-05-20_Fireblocks_x402-foundation-agentic-payments-suite]] | Fireblocks が機関グレードの x402 Gateway と Wallets を提供開始 |
| 2026-06-15 | [[2026-06-15_AWS-Coinbase_x402-cloudfront-waf-ai-traffic-monetization]] | AWS WAF が AI トラフィック課金を GA。CloudFront（インターネット約 25%）経由のサイトがコンソール変更のみで x402 USDC 有料ゲートウェイになれる |
| 2026-05-20 | [[2026-05-20_AllUnity_sekau-stablecoin-agentic-payments]] | AllUnity が MiCA 準拠 SEKAU ステーブルコインの 6 月ローンチと x402 Agentic Payments インフラを発表。欧州ローカル通貨 x402 対応の先行事例 |
| 2026-05-20 | [[2026-05-20_AllUnity_sekau-stablecoin-agentic-payments-x402]] | AllUnity SEK ステーブルコインが x402 対応を発表。非 USD 圏への拡張 |
| 2026-05-20 | [[2026-05-20_Fireblocks_agentic-payments-suite-x402-foundation]] | Fireblocks が x402 Foundation 参加と Agentic Payments Suite をローンチ（機関グレード実装） |
| 2026-05-23 | [[2026-05-20_Fireblocks_agentic-payments-suite-x402]] | Fireblocks × x402 Foundation 連携による PSP・フィンテック向けスイート詳細 |
| 2026-05-25 | [[2026-05-20_AllUnity_sekau-sek-stablecoin-agentic-payments]] | AllUnity SEK/AU ステーブルコインの x402 対応詳細：欧州市場での非 USD 決済拡張 |
| 2026-05-26 | [[2026-05-26_Coinbase-Base_mcp-ai-agent-wallet]] | Base 上の MCP 対応 AI エージェントウォレット：MCP プロトコルから x402 決済へのブリッジ |

### アプリケーション・ユースケース

| 日付 | ノート | 意味 |
|---|---|---|
| 2026-04-21 | [[2026-04-21_Coinbase-x402_agentic-market-launch]] | Agentic.market ローンチ。エージェントが購入できるサービスの流通面が整う |
| 2026-05-05 | [[2026-05-05_Solana-GoogleCloud_pay-sh-x402-agent-payments]] | Google Cloud / Solana 側で Pay.sh が登場。競合実装が x402 互換で動く |
| 2026-05-11 | [[2026-05-11_Cryptorefills_x402-merchant-agent-payments-checkout]] | Cryptorefills がチェックアウトに x402 を採用。実マーチャントの導入事例 |
| 2026-05-26 | [[2026-05-26_OpenRouter_series-b-x402-transition]] | OpenRouter が AI ルーティングサービスの決済を x402 に移行 |
| 2026-05-20 | [[2026-05-20_AllUnity_sek-stablecoin-agentic-payments-x402]] | AllUnity が x402 向け SEK ステーブルコインを発表——北欧市場向け agentic payments |
| 2026-05-25 | [[2026-05-21_Keyrock_ai-agent-payments-crypto-rails-report]] | Keyrock が AI エージェント決済のクリプトレール活用レポートを公開——x402 を主要プロトコルとして評価 |
| 2026-06-04 | [[2026-06-04_Kustodia_x402-escrow-mcp-agents]] | Kustodia が x402 × MCP を使ったエスクロー型エージェント決済を実装 |
| 2026-06-04 | [[2026-06-04_Travala_travel-mcp-x402-usdc-hotels]] | Travala が x402 + MCP でホテル・旅行向けエージェント決済を展開 |
| 2026-06-05 | [[2026-06-04_Casper-Network_x402-ai-toolkit-wasm]] | Casper Network が WebAssembly 対応の x402 AI エージェントツールキットを公開 |
| 2026-06-09 | [[2026-06-09_Injective_x402-agent-payments]] | Injective Protocol が Coinbase × x402 で AI エージェント決済を実装 |
| 2026-06-10 | [[2026-06-10_Ripple_xrpl-ai-starter-kit-x402-rlusd]] | Ripple が XRPL × x402 × RLUSD の AI エージェント向けスターターキットを公開 |

### 採用・市場データ

| 日付 | ノート | 意味 |
|---|---|---|
| 2026-05-13 | [[2026-05-13_x402_batch-settlement-sub-cent-ai-payments]] | バッチ決済仕様が公開。サブセント決済の経済性が成立 |
| 2026-05-27 | [[2026-05-27_x402_approval-gap-volume-data]] | 実取引データ公開。承認ギャップとボリューム動向が可視化 |
| 2026-05-29 | [[2026-05-29_Base_x402-agentic-economy-is-here]] | Base 上の x402 エコノミーが本格稼働。ユースケース事例集 |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100m-agentic-payments]] | Chainalysis が x402 の 1 億件突破を分析——Base がメイン環境 |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100m-transactions-base]] | Chainalysis による x402 トランザクション 1 億件達成の統計データ詳細 |
| 2026-06-04 | [[2026-06-03_Chainalysis_x402-100M-agentic-payments-base]] | Chainalysis が Base 上の x402 アジェンティック決済 1 億件突破を報告（大規模市場データ） |

---

## 技術的論点

### バッチ決済との組み合わせ
リクエストごとのオンチェーン決済はガスコスト・レイテンシで非現実的。x402 Batch Settlement と組み合わせることで、1000リクエストを1 Tx に集約できる。詳細 → [[x402-batch-settlement]]

### マルチチェーン展開
Base（主戦場）→ Arbitrum（コスト削減）→ Solana（高速決済）の順に拡張中。ファシリテーターが複数チェーンに対応することで、マーチャント側は1実装で複数チェーンからの受け取りが可能になる。

### 非 USD ステーブルコイン
AllUnity SEK の参加が示すように、USDC 以外のステーブルコインが x402 エコシステムに入り始めている。非 USD 圏での agentic commerce 拡張に向けた布石。

---

## 監視ポイント

- Agentic.market の課金サービス数・日次取引量（エコシステムの厚みを示す）
- AWS / Google Cloud 側の x402 ファシリテーター正式 GA タイミング
- x402 バッチ決済の採用率（取引量中のバッチ比率）
- Stripe MPP との競合・共存（AWS AgentCore では両社が共存）
- 非 USD ステーブルコインの x402 対応拡大

---

## 関連ページ

- [[x402-batch-settlement]] — バッチ決済仕様の詳細
- [[x402]] — x402 プロトコルの正規ページ
- [[x402 Foundation]] — x402 の標準化・ガバナンス組織
- [[Fireblocks]] — x402 Gateway / Wallets インフラ
- [[Coinbase]] — x402 標準化の主導企業
- [[MOC_Protocols]] — プロトコル全体マップ
