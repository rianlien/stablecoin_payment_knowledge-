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
| 2026-04-02 | [[2026-04-02_x402-Foundation_linux-foundation-launch]] | Linux Foundation 移管。業界中立ガバナンスが確立し、特定企業依存を脱する |

### インフラ拡張

| 日付 | ノート | 意味 |
|---|---|---|
| 2026-05-07 | [[2026-05-07_AWS_bedrock-agentcore-payments-x402]] | AWS AgentCore Payments が x402 を正式採用。クラウド側の決済ランタイムとして認知 |
| 2026-05-14 | [[2026-05-14_x402_arbitrum-launch-agent-payments]] | Arbitrum 対応で低コスト L2 でのマイクロペイメントが可能に |
| 2026-05-20 | [[2026-05-20_Fireblocks_x402-foundation-agentic-payments-suite]] | Fireblocks が機関グレードの x402 Gateway と Wallets を提供開始 |
| 2026-05-20 | [[2026-05-20_AllUnity_sekau-stablecoin-agentic-payments-x402]] | AllUnity SEK ステーブルコインが x402 対応を発表。非 USD 圏への拡張 |

### アプリケーション・ユースケース

| 日付 | ノート | 意味 |
|---|---|---|
| 2026-04-21 | [[2026-04-21_Coinbase-x402_agentic-market-launch]] | Agentic.market ローンチ。エージェントが購入できるサービスの流通面が整う |
| 2026-05-05 | [[2026-05-05_Solana-GoogleCloud_pay-sh-x402-agent-payments]] | Google Cloud / Solana 側で Pay.sh が登場。競合実装が x402 互換で動く |
| 2026-05-11 | [[2026-05-11_Cryptorefills_x402-merchant-agent-payments-checkout]] | Cryptorefills がチェックアウトに x402 を採用。実マーチャントの導入事例 |
| 2026-05-26 | [[2026-05-26_OpenRouter_series-b-x402-transition]] | OpenRouter が AI ルーティングサービスの決済を x402 に移行 |

### 採用・市場データ

| 日付 | ノート | 意味 |
|---|---|---|
| 2026-05-13 | [[2026-05-13_x402_batch-settlement-sub-cent-ai-payments]] | バッチ決済仕様が公開。サブセント決済の経済性が成立 |
| 2026-05-27 | [[2026-05-27_x402_approval-gap-volume-data]] | 実取引データ公開。承認ギャップとボリューム動向が可視化 |
| 2026-05-29 | [[2026-05-29_Base_x402-agentic-economy-is-here]] | Base 上の x402 エコノミーが本格稼働。ユースケース事例集 |

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
- [[Fireblocks]] — x402 Gateway / Wallets インフラ
- [[Coinbase]] — x402 標準化の主導企業
- [[MOC_Protocols]] — プロトコル全体マップ
