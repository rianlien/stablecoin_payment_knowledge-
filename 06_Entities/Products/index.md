---
title: "Product Notes"
type: index
updated: 2026-06-18
tags:
  - stablecoin
  - payments
  - product-research
---

# Product Notes

ステーブルコイン決済関連プロダクトを、PM が比較しやすい「利用シーン / 導入目的」ベースで整理する索引。

会社単位の戦略理解は `06_Entities/Companies/`、プロダクト単位の比較・参入余地・UX差分の把握はこのページを起点にする。

---

## 使い方

| 見たい問い | 見る場所 |
|---|---|
| 加盟店が stablecoin checkout を入れるなら何が候補か | [[06_Entities/Products/Checkout-Merchant-Acceptance/index|Checkout / Merchant Acceptance]] |
| AI agent / x402 / machine payment の実装候補は何か | [[06_Entities/Products/Agent-Payments-x402/index|Agent Payments / x402]] |
| 請求・経費・法人支払いに近いものは何か | [[06_Entities/Products/Invoicing-Business-Ops/index|Invoicing / Business Ops]] |
| B2B 決済・精算・ペイアウトで使えるものは何か | [[06_Entities/Products/Settlement-Payouts/index|Settlement / Payouts]] |
| wallet / card / spend UX として使えるものは何か | [[06_Entities/Products/Wallets-Cards/index|Wallets / Cards]] |
| AML、policy、approval、attack surface を見るには何か | [[06_Entities/Products/Compliance-Risk/index|Compliance / Risk]] |

---

## Categories

### Agent Payments / x402

AI agent、MCP、x402、pay-per-call API、machine-native spending を主な導入シーンにするプロダクト。

- [[06_Entities/Products/Agent-Payments-x402/alchemy-x402|Alchemy x402]]
- [[06_Entities/Products/Agent-Payments-x402/aws-agentcore-payments|AWS AgentCore Payments]]
- [[06_Entities/Products/Agent-Payments-x402/circle-agent-stack|Circle Agent Stack]]
- [[06_Entities/Products/Agent-Payments-x402/coinbase-agentic-market|Coinbase Agentic.Market]]
- [[06_Entities/Products/Agent-Payments-x402/crossmint-agent-payments|Crossmint Agent Payments]]
- [[06_Entities/Products/Agent-Payments-x402/fireblocks-agentic-payments|Fireblocks Agentic Payments]]
- [[06_Entities/Products/Agent-Payments-x402/pay-sh|Pay.sh]]
- [[06_Entities/Products/Agent-Payments-x402/quicknode-x402-payments|QuickNode x402 Payments]]
- [[06_Entities/Products/Agent-Payments-x402/x402-foundation|x402 Foundation]]
- [[06_Entities/Products/Agent-Payments-x402/x402scan|x402scan]]

### Checkout / Merchant Acceptance

加盟店・PSP・commerce platform が stablecoin acceptance を導入するための checkout / acceptance surface。

- [[06_Entities/Products/Checkout-Merchant-Acceptance/base-pay|Base Pay]]
- [[06_Entities/Products/Checkout-Merchant-Acceptance/checkout-com-stablecoin-acceptance|Checkout.com stablecoin acceptance]]
- [[06_Entities/Products/Checkout-Merchant-Acceptance/fireblocks-flow|Fireblocks Flow]]
- [[06_Entities/Products/Checkout-Merchant-Acceptance/mnee-pay|MNEE Pay]]
- [[06_Entities/Products/Checkout-Merchant-Acceptance/ppro-coinbase-stablecoin-payments|PPRO + Coinbase stablecoin payments]]
- [[06_Entities/Products/Checkout-Merchant-Acceptance/stripe-x402|Stripe x402]]
- [[06_Entities/Products/Checkout-Merchant-Acceptance/volt-stablecoin-checkout|Volt stablecoin checkout]]

### Invoicing / Business Ops

請求、売掛、支払、法人カード、経費処理など、finance ops に近いプロダクト。

- [[06_Entities/Products/Invoicing-Business-Ops/acctual|Acctual]]
- [[06_Entities/Products/Invoicing-Business-Ops/paystand-usdb|Paystand USDb]]
- [[06_Entities/Products/Invoicing-Business-Ops/request-finance|Request Finance]]
- [[06_Entities/Products/Invoicing-Business-Ops/request-stablecoin-business-cards|Request Stablecoin Business Cards]]
- [[06_Entities/Products/Invoicing-Business-Ops/stableinvoicing|StableInvoicing]]

### Settlement / Payouts

B2B settlement、cross-border payout、bank / PSP 向け managed settlement、口座型資金移動に近いプロダクト。

- [[06_Entities/Products/Settlement-Payouts/banking-circle-stablecoin-settlement|Banking Circle Stablecoin Settlement]]
- [[06_Entities/Products/Settlement-Payouts/circle-cpn-managed-payments|Circle CPN Managed Payments]]
- [[06_Entities/Products/Settlement-Payouts/cobo-adoption-clearing-layer|Cobo Adoption Clearing Layer]]
- [[06_Entities/Products/Settlement-Payouts/lightspark-grid-global-accounts|Lightspark Grid Global Accounts]]
- [[06_Entities/Products/Settlement-Payouts/mastercard-stablecoin-settlement|Mastercard stablecoin settlement]]
- [[06_Entities/Products/Settlement-Payouts/moneygram-tempo-stablecoin-settlement|MoneyGram + Tempo settlement]]
- [[06_Entities/Products/Settlement-Payouts/veem-stablecoin-accounts|Veem Stablecoin Accounts]]

### Wallets / Cards

end-user wallet、agent wallet、business card、stablecoin-backed spend、addressless transfer など、支払い手段そのものの UX。

- [[06_Entities/Products/Wallets-Cards/cash-app-stablecoins|Cash App stablecoins]]
- [[06_Entities/Products/Wallets-Cards/corpay-bvnk-stablecoin-wallets|Corpay + BVNK stablecoin wallets]]
- [[06_Entities/Products/Wallets-Cards/crossmint-stablecoin-wallet-quickstart|Crossmint Stablecoin Wallet Quickstart]]
- [[06_Entities/Products/Wallets-Cards/open-wallet-standard|Open Wallet Standard]]
- [[06_Entities/Products/Wallets-Cards/slash-global-usd-cards|Slash Global USD Cards]]
- [[06_Entities/Products/Wallets-Cards/solayer-pay|Solayer Pay]]
- [[06_Entities/Products/Wallets-Cards/tether-wallet|tether.wallet]]
- [[06_Entities/Products/Wallets-Cards/zap-wallet|Zap Wallet]]

### Compliance / Risk

AML、screening、policy、identity、agent authorization、x402 attack surface など、決済導入時のリスク管理レイヤ。

- [[06_Entities/Products/Compliance-Risk/anchain-aml-mcp|AnChain AML MCP]]
- [[06_Entities/Products/Compliance-Risk/boundary-usbd|Boundary USBD]]
- [[06_Entities/Products/Compliance-Risk/finscan-payments-stablecoin-screening|FinScan Payments stablecoin screening]]
- [[06_Entities/Products/Compliance-Risk/five-attacks-x402|Five Attacks on x402]]
- [[06_Entities/Products/Compliance-Risk/free-riding-x402|Free-Riding in the AI Economy]]
- [[06_Entities/Products/Compliance-Risk/presidio-hardened-x402|presidio-hardened-x402]]
- [[06_Entities/Products/Compliance-Risk/x402-secure|x402-secure]]

---

## 運用ルール

- 1プロダクト1ファイルを原則にする。
- 物理配置は「主なPM比較軸」で決める。複数カテゴリにまたがる場合は、この index か topic note から横断リンクする。
- 会社の戦略理解は `06_Entities/Companies/` に集約し、会社ページから関連プロダクトへリンクする。
- ニュース単体は `00_Inbox`、横断分析は `03_Topics`、プロダクト比較はこの `06_Entities/Products` に置く。
