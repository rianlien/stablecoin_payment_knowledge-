---
title: "Base"
type: company
updated: 2026-06-27
category: blockchain-infrastructure
tags:
  - x402
  - agentic-commerce
  - agent-payments
  - L2
  - company
aliases:
  - Base Network
  - Coinbase Base
---

# Base

Coinbase が運営する Ethereum Layer-2 ブロックチェーン。x402 プロトコルの主要稼働チェーンとして、AI エージェント間の自律決済インフラの中心的役割を担っている。

この vault では、Base を「x402 エコシステムのコアチェーン」として追う。企業実体としては Coinbase の一部だが、x402・MCP・agentic commerce の文脈で独立した言及が多いため独立ページとして管理する。Coinbase 本体については [[Coinbase]] を参照。

---

## 現状の要約

### 何をしているか

- **x402 プロトコルのコアチェーン**：AI エージェントが API・コンピューティング・デジタルサービスの代金を HTTP リクエスト内で直接支払う x402 プロトコルは、Base を主要チェーンとして稼働。2026-06-03 時点で累計 1 億件以上の取引を記録
- **x402 バッチ決済対応**：2026-05-13 に Jesse Pollak（Base コアチーム）が $0.0001 未満の AI マイクロペイメントを実現するバッチ決済機能を発表。ERC-20 エスクロー + オフチェーンバウチャー方式で複数支払いを一括オンチェーン決済
- **Base MCP Server（AI エージェントウォレット）**：2026-05-26 ローンチ。Claude・ChatGPT 等の AI エージェントが Base スマートウォレットに接続し、自然言語でトークン送金・スワップ・DeFi 操作を実行できる。秘密鍵は TEE セキュアエンクレーブで管理。エージェントごとの支出上限・ホワイトリストをインフラ層で強制
- **エコシステム拡大**：2026-05-29 時点で直近 30 日の x402 取引が 310 万件・$1.2M の価値移転。旅行分野（Amadeus / Tripadvisor / FlightAware）・AI 推論（Venice / BlockRunAI）・計算（Wolfram Alpha）等が参加

### 見立て

x402 の取引件数（直近 30 日 310 万件）は急成長しているが、平均単価が $0.39 と低水準で、出来高の多くは PING ミームコインに依存していると Chainalysis が指摘している（2026-06-03）。旅行分野（Amadeus 等）の参入で高単価決済への移行が始まれば、出来高が本質的に成長するシグナルとなる。Base は x402 のデファクトチェーンとして先行しているが、XRPL（Ripple）・Solana・Arbitrum も対応済みで、マルチチェーン競争が始まっている。

---

## Inbox との紐付け

| 日付 | ノート | 位置づけ一行 |
|---|---|---|
| 2026-05-13 | [[2026-05-13_x402_batch-settlement-sub-cent-ai-payments]] | x402 バッチ決済対応——$0.0001 以下の AI マイクロペイメントを Base 上で実現 |
| 2026-05-26 | [[2026-05-26_Coinbase-Base_mcp-ai-agent-wallet]] | Base MCP Server ローンチ——AI エージェントがスマートウォレットと自然言語で統合 |
| 2026-05-29 | [[2026-05-29_Base_x402-agentic-economy-is-here]] | Base 公式ブログが x402 エコシステム拡張を発表——旅行分野（Amadeus 等）も参加 |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100M-agentic-payments-base]] | Chainalysis が x402 の 1 億件突破を分析——Base がメイン稼働チェーン |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100m-agentic-payments]] | Chainalysis による x402 1 億件達成の詳細分析 |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100m-transactions-base]] | x402 取引 1 億件統計データ |
