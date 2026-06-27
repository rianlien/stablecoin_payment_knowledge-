---
title: "Exodus"
type: company
updated: 2026-06-27
category: crypto-wallet
tags:
  - agentic-commerce
  - stablecoin
  - wallet
  - agent-payments
  - company
---

# Exodus

Exodus Movement（NYSE: EXOD）は、暗号資産ウォレットを主力とする上場フィンテック企業。2026-05-08 に AI エージェント専用ステーブルコイン「XO Cash」と開発者向け SDK「AgentKit」をローンチし、AI エージェントが Solana 上で自律的に決済を行うインフラを提供している。

この vault では、Exodus を「AI エージェント向け専用ステーブルコインと Mastercard/Visa カード接続インフラの提供者」として追う。MoonPay + Monavate スタックを採用したエージェント向けウォレット発行モデルが、agent-payment の参照設計の一つとなっている。

---

## 現状の要約

### 何をしているか

- **XO Cash（AI エージェント専用ステーブルコイン）**：Solana 上で稼働する AI エージェント向けステーブルコイン。決済時に USDC または USDT に自動変換し、手数料ゼロで実行。エージェントは秘密鍵を保有せず、Exodus Pay 残高から支出権限のみを持つ設計
- **AgentKit SDK**：1 回の API 呼び出しでエージェント専用ウォレットと Visa デビットカードを発行。日次支出上限・1 回あたり上限・許可加盟店リスト・レートリミットをユーザーが設定可能
- **加盟店接続**：MoonPay（決済インフラ）+ Monavate（Mastercard プリンシパルメンバー、リアルタイム清算）と連携し、Visa・Mastercard 加盟店での直接決済に対応。非カストディアル設計
- **比較**：MoonPay「MoonAgents Card」（2026-05-01 発表）と同一の MoonPay + Monavate スタックを採用。違いは XO Cash が Exodus ブランドの専用通貨を持ち、AgentKit SDK を提供する点

### 見立て

XO Cash と AgentKit の設計（秘密鍵なし・ユーザー設定スペンドルール・1 API でウォレット発行）は、エージェント決済におけるガーディアンモデルの参照設計として機能する。ただし XO Cash が AI エージェント決済の主要ステーブルコインとして USDC・USDT に対抗できるかは未確認。GENIUS Act 上での XO Cash の法的分類（USDC/USDT への自動変換ラッパーとしての規制適用）が今後の普及を左右する可能性がある。

---

## Inbox との紐付け

| 日付 | ノート | 位置づけ一行 |
|---|---|---|
| 2026-05-08 | [[2026-05-08_Exodus_xo-cash-ai-agent-stablecoin]] | XO Cash と AgentKit のローンチ——MoonPay・Monavate 連携で Mastercard 加盟店決済対応 |
| 2026-05-08 | [[2026-05-08_Exodus_xo-cash-ai-stablecoin]] | XO Cash の詳細——Visa ネットワーク対応と AgentKit SDK の仕様 |
