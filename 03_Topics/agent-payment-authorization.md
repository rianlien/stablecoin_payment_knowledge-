---
title: "エージェント決済の認可モデル"
type: topic
updated: 2026-06-15
tags:
  - agent-payments
  - payment-authorization
  - agentic-commerce
  - identity
---

# エージェント決済の認可モデル

AI エージェントが人間に代わって決済を実行する際の「誰が何をどこまで許可するか」の枠組み。認証（Authentication）、認可（Authorization）、責任帰属（Liability）の3層で整理する。

---

## 問題の本質

人間が決済する場合、認証（カード・生体）と認可（金額・スコープ）は暗黙に人間が担う。エージェントが決済する場合：
- **認証**: エージェントのアイデンティティをどう証明するか
- **認可**: ユーザーがエージェントに「どこまで払ってよいか」を事前に定義する必要がある
- **責任**: エラー・不正が起きた時、誰が責任を負うか

---

## 認可モデルの主要アプローチ

### AP2（Agentic Payment Protocol）— Google / FIDO Alliance

**概念**: AI エージェントがデバイスバインドの認証情報で決済を認可される標準。FIDO2 の passkey モデルをエージェントに適用。ユーザー → エージェント → マーチャント の信頼チェーンをデバイスレベルで担保。

詳細 → [[ap2-agent-payments-protocol]]

| 日付 | ノート |
|---|---|
| 2026-04-28 | [[2026-04-28_Google_ap2-fido-alliance]] |
| 2026-05-19 | [[2026-05-19_Google_universal-cart-ap2-io2026]] |

### MPP（Machine Payments Protocol）— Stripe

**概念**: Stripe が提案する AI エージェント向け決済プロトコル。マーチャント側の実装を最小化し、エージェントが Stripe のインフラを通じて支払いを完結させる。x402 とは補完・競合の両面がある（AWS AgentCore では共存）。

詳細 → [[mpp-machine-payments-protocol]]

| 日付 | ノート |
|---|---|
| 2026-04-30 | [[2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments]] |
| 2026-05-06 | [[2026-05-06_RedotPay-Tempo_mpp-agentic-payments-launch]] |

### Visa Trusted Agent Protocol（TAP）— Visa

**概念**: Visa が提案するエージェント向け決済認可フレームワーク。エージェントのアイデンティティをカードネットワークが保証し、既存の加盟店・PSP インフラと互換性を持たせる。

詳細 → [[visa-tap-trusted-agent-protocol]]

| 日付 | ノート |
|---|---|
| 2026-05-05 | [[2026-05-05_Visa_agentic-ready-canada-global]] |
| 2026-05-28 | [[2026-05-28_Visa-Replit_trusted-agent-protocol]] |
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-ai-initiated-payments]] |
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-b2b-payments]] |
| 2026-06-11 | [[2026-06-11_Visa-OpenAI_chatgpt-agent-payments]] |

### Mastercard Agent-to-Agent（A2A）

**概念**: Mastercard がエージェント間決済のための認可・清算フレームワークを整備。JD.com との連携でアジア市場向けの実装を進める。

| 日付 | ノート |
|---|---|
| 2026-04-30 | [[2026-04-30_Mastercard_q1-2026-agent-to-agent-payments]] |
| 2026-05-18 | [[2026-05-18_Mastercard-JDcom_agent-pay-strategic-partnership]] |
| 2026-06-02 | [[2026-06-02_Worldline-ING-Mastercard_agentic-payments-europe]] |
| 2026-06-02 | [[2026-06-02_Worldline-ING-Mastercard_first-european-agentic-payment]] |
| 2026-06-04 | [[2026-06-02_Worldline-ING-Mastercard_europe-first-live-agentic-payment]] |

### Circle Agent Stack

**概念**: Circle が提案するエージェント経済向けのコンポーネント群。ナノペイメント、エージェントウォレット、認可スコープ管理を USDC インフラ上で提供。

| 日付 | ノート |
|---|---|
| 2026-05-11 | [[2026-05-11_Circle_agent-stack-nanopayments-agentic-economy]] |

---

## ウォレット・委任の実装事例

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-05-26 | [[2026-05-26_Coinbase-Base_mcp-ai-agent-wallet]] | Base 上の MCP 対応エージェントウォレット。MCP プロトコルで AI ツールからウォレット操作を委任 |
| 2026-05-20 | [[2026-05-20_Fireblocks_x402-foundation-agentic-payments-suite]] | Fireblocks Agentic Wallets。フィンテックがエンドユーザーのエージェントへの委任を仲介 |
| 2026-05-06 | [[2026-05-06_AnchorageDigital_agentic-banking-google-cloud]] | Anchorage Digital が Google Cloud と連携してエージェント向け銀行グレードの認可インフラを提供 |
| 2026-05-14 | [[2026-05-14_NEAR-AI_usdc-confidential-intents-agent-payments]] | NEAR AI の Confidential Intents。プライバシー保護型の決済認可モデル |
| 2026-05-01 | [[2026-05-01_MoonPay_moonagents-card-mastercard-ai-agents]] | MoonPay が AI エージェント向けカードを Mastercard と提供 |
| 2026-05-04 | [[2026-05-04_OwlTing_owlpay-agent-wallet]] | OwlPay エージェントウォレット。台湾発の実装事例 |
| 2026-05-27 | [[2026-05-27_Robinhood_agentic-trading-credit-card-agent-payments]] | Robinhood Agentic Trading + Credit Card：AI エージェントへの支出権限委任の先行参照実装 |
| 2026-06-02 | [[2026-06-02_Crossmint_agentic-cards-visa-basis-theory]] | Crossmint が Visa + Basis Theory でエージェント向けプログラマブルカードを提供 |
| 2026-06-04 | [[2026-06-04_Notabene_flow-responders-b2b-stablecoin-payments]] | Notabene Flow：Travel Rule 準拠の B2B ステーブルコイン決済——受け手側の認可・到達性を強化 |
| 2026-06-16 | [[2026-06-16_Zip-Stripe_shared-payment-tokens-agentic]] | Zip US が Stripe SPT を採用——エージェント起点の BNPL 取引に対する支払い認可委任の実装事例 |
| 2026-06-17 | [[2026-06-17_x402_onpaymentrequired-trust-gate]] | x402 クライアントに `onPaymentRequired` trust-gate フックを追加——支払い前のペイアドレス検証・支出上限を標準化 |
| 2026-06-19 | [[2026-06-19_x402_siwx-go-support]] | x402 SIWX（Sign-In-With-X）が Go に対応——エージェントの署名認証による繰り返しアクセス認可 |

---

## 規制・ガードレール

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-05-13 | [[2026-05-13_CFES_agentic-payments-guardrails-report]] | CFES が支出上限・監査ログ・人間承認のガードレール基準を提言 |
| 2026-05-13 | [[2026-05-13_CFES_agentic-payments-liability-authority]] | エージェントの決済エラー時の責任帰属を整理 |

---

## 現在の構図

```
アプローチ      主体          レール      強み
-----------     ----          ------      ----
AP2 / FIDO      Google        カード/標準  デバイスバインド認証
MPP             Stripe        カード/Stripe 既存マーチャントとの互換
x402            Coinbase/LF   オンチェーン 開発者標準・マイクロペイメント
TAP             Visa          カード       カードネットワーク信頼性
A2A             Mastercard    カード/CPN   企業間決済・B2B
```

AP2 と MPP と x402 は AWS AgentCore Payments で共存しており、排他的な競合というよりレイヤーが異なる補完関係になりつつある。認証レイヤー（AP2/TAP）と決済プロトコル（x402/MPP）は異なる問題を解いている。

---

## 監視ポイント

- AP2 / FIDO Alliance の仕様確定タイミングと採用状況
- Visa TAP の GA と PSP 実装数
- CFES ガードレール提言の業界・規制への波及
- MCP（Model Context Protocol）経由のウォレット委任が標準化されるか
- エージェント向けカード（MoonPay, Crossmint 等）の発行量

---

## 関連ページ

- [[x402-ecosystem]] — x402 決済プロトコルの全体像
- [[psp-merchant-readiness]] — PSP・マーチャント側の対応状況
- [[MOC_agent-payments-stack]] — エージェント決済スタック全体マップ
- [[MOC_Regulation]] — CFES 等の規制・ガイドライン
