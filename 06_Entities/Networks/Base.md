---
title: "Base"
type: network
updated: 2026-06-16
category: ethereum-l2
tags:
  - blockchain-network
  - ethereum-l2
  - stablecoin
  - x402
  - agentic-commerce
aliases:
  - Base Network
  - Coinbase Base
---

# Base

Base は Coinbase が開発・運営する Ethereum L2 network。会社・事業主体としての Coinbase については [[Coinbase]] を参照。

この vault では、Base を「USDC on Base、x402、Base MCP などを通じて、AI エージェント決済とオンチェーン操作が実行される主要ネットワーク」として追う。

---

## 現状の要約

### 何を担っているか

- **x402 の主要実行環境**: x402 の取引、マイクロペイメント、agentic commerce のオンチェーン実行先として繰り返し登場する。
- **USDC 決済レール**: AI エージェント、API、コンテンツ、旅行データなどの支払いに USDC on Base が使われる文脈が多い。
- **Base MCP の実行基盤**: ChatGPT、Claude、Codex、Cursor などの AI クライアントが Base Account / smart wallet を通じてオンチェーン操作する接続先。
- **オンチェーン活動データの観測対象**: Chainalysis や Base 公式ブログが、x402 の取引件数・出来高・利用者プロファイルを Base 上のデータとして分析している。

### 見立て

Base は Coinbase の会社戦略の一部だが、分析対象としては「企業」ではなく「決済実行環境」。Coinbase が x402 / CDP / wallet infrastructure を提供し、Base がその実行面とデータ面を担う構図で見るのが自然。

---

## 主要レイヤー

| レイヤー | Base の役割 | 意味 |
|---|---|---|
| L0 / Network | Ethereum L2 として USDC 決済を処理 | 低コスト・高速なオンチェーン支払いの実行環境 |
| L1 / Wallet | Base Account / smart wallet / Base MCP | AI クライアントがユーザー承認付きで送金・スワップ・DeFi 操作を実行できる |
| L3 / Protocol | x402 の主要展開先 | HTTP 402 ベースの API / AI / machine payments を実取引へ接続する |
| Data / Analytics | x402 取引件数・出来高の観測対象 | agentic payments の実需と投機的利用を分けて評価するための基礎データ |

---

## Coinbase との関係

- **会社・事業主体**: [[Coinbase]]
- **ネットワーク / 実行環境**: [[Base]]
- **プロトコル / 標準**: x402

Base は Coinbase のプロダクト・エコシステムの一部だが、ノート上は会社分析とネットワーク分析を分ける。Coinbase ページでは事業戦略、提携、CDP、custody、x402 標準化を扱い、Base ページではネットワーク上で何が実行され、どのデータが観測されているかを扱う。

---

## Inbox との紐付け

### x402 実行環境

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-13 | [[2026-05-13_x402_batch-settlement-sub-cent-ai-payments]] | Base / Coinbase が x402 バッチ決済対応を発表。サブセントの AI マイクロペイメントを可能にする設計 |
| 2026-05-29 | [[2026-05-29_Base_x402-agentic-economy-is-here]] | Base 公式ブログが x402 エコシステム拡張と直近 30 日の活動統計を発表 |

### Agent wallet / MCP

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-26 | [[2026-05-26_Coinbase-Base_mcp-ai-agent-wallet]] | Base MCP により、AI クライアントから Base Account 経由でオンチェーン操作が可能に |

### Activity data / analytics

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100m-agentic-payments]] | Chainalysis が Base 上の x402 採用状況を分析。累計 1 億件突破を報告 |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100m-transactions-base]] | 初期急増の投機要因、$1 以上取引比率、利用者プロファイルを整理 |
| 2026-06-04 | [[2026-06-03_Chainalysis_x402-100M-agentic-payments-base]] | 直近 30 日出来高など、既存データとのギャップ確認が必要な分析ノート |

---

## 監視ポイント

- x402 の Base 上の月次件数・出来高が、投機的用途を除いて成長しているか
- Base 公式統計、第三者分析、Chainalysis の数字の集計対象・期間・方法論の差
- Base MCP と x402 支払いの直接統合
- USDC on Base が旅行、API、コンテンツ、推論課金でどの程度使われるか
- Solana、Arbitrum、Polygon、Injective など他チェーンへの x402 展開により、Base の相対的な中心性が下がるか

---

## 関連ページ

- [[Coinbase]]
- [[MOC_Protocols]]
- [[MOC_agent-payments-stack]]
- [[x402-ecosystem]]

---

## 参考リンク

- 一次情報: [Base Blog「The Agentic Economy Is Here」](https://blog.base.org/the-agentic-economy-is-here)
- 一次情報: [Base](https://www.base.org/)
- 一次情報: [Coinbase x402 docs](https://docs.cdp.coinbase.com/x402/welcome)
- 一次情報: [Chainalysis Blog「Inside x402」](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/)
