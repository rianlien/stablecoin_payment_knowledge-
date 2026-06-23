---
title: "PSP・マーチャントのエージェント決済対応"
type: topic
updated: 2026-06-23
tags:
  - agentic-commerce
  - merchant-readiness
  - payments
  - psp
---

# PSP・マーチャントのエージェント決済対応

AI エージェントからの決済を受け取れる／処理できる状態にある PSP・決済インフラ・マーチャントの動向を整理する。「人間が開始する決済」から「エージェントが開始する決済」への移行における受け手側の準備状況。

---

## なぜ「受け手側の対応」が必要か

エージェント決済が成立するには、送り手（エージェント + ウォレット）だけでなく、**受け手（マーチャント・PSP）がエージェントを認識・受け入れできる**ことが必要。現状の課題：

- エージェントに人間向け CAPTCHA・OTP を要求してしまう
- エージェントのアイデンティティを確認する仕組みがない
- ステーブルコイン決済を受け取るインフラがない
- チェックアウトフローがエージェントのコンテキスト長外（HTML フォームなど）

---

## 対応状況マップ

### Stripe — MPP + ステーブルコイン拡張

Stripe は MPP（Machine Payments Protocol）を通じてエージェントからの決済を受け取れる加盟店網を構築中。同時にステーブルコイン決済のアクワイアリングも拡張。

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-04-30 | [[2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments]] | MPP 発表。AI エージェント向け決済フローを Stripe セッション 2026 で公開 |
| 2026-04-30 | [[2026-04-30_Stripe-Sessions-2026_stablecoin-expansion]] | ステーブルコイン決済の受け取り・配信を 100 カ国以上に拡大 |
| 2026-05-13 | [[2026-05-13_Stripe-Tempo_streaming-stablecoin-payments]] | Tempo と連携してストリーミング型ステーブルコイン支払いを実装 |
| 2026-06-16 | [[2026-06-16_Zip-Stripe_shared-payment-tokens-agentic]] | Zip US が Stripe SPT を採用——BNPL をエージェントコマースに拡張 |

### Visa — Agentic-Ready 認証 + TAP

Visa は「Agentic-Ready」という認定プログラムを用意し、Visa Trusted Agent Protocol（TAP）で認可されたエージェントが Visa 加盟店で決済できる仕組みを整備中。

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-05-05 | [[2026-05-05_Visa_agentic-ready-canada-global]] | Agentic-Ready 認定プログラムをカナダ・グローバルで展開開始 |
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-ai-initiated-payments]] | Highnote が Visa と連携してエージェント起点の B2C 決済を実装 |
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-b2b-payments]] | 同連携の B2B 決済拡張 |
| 2026-05-28 | [[2026-05-28_Visa-Replit_trusted-agent-protocol]] | Replit と TAP の実装連携。開発者環境でのエージェント決済テスト |
| 2026-06-10 | [[2026-06-10_Visa_payments-forum-openai-agentic-commerce]] | Visa Payments Forum：OpenAI 連携・Agent Score・Agentic Registry 発表 |
| 2026-06-11 | [[2026-06-11_Visa-OpenAI_chatgpt-agent-payments]] | ChatGPT 内の Visa カード連動によるエージェント決済。最大規模の統合事例 |

### Mastercard — A2A + 欧州展開

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-04-30 | [[2026-04-30_Mastercard_q1-2026-agent-to-agent-payments]] | A2A（Agent-to-Agent）決済フレームワークの進捗を Q1 決算で公表 |
| 2026-05-18 | [[2026-05-18_Mastercard-JDcom_agent-pay-strategic-partnership]] | JD.com とのパートナーシップ。アジア EC でのエージェント決済実装 |
| 2026-06-02 | [[2026-06-02_Worldline-ING-Mastercard_agentic-payments-europe]] | Worldline・ING・Mastercard が欧州向けエージェント決済基盤を共同発表 |
| 2026-06-02 | [[2026-06-02_Worldline-ING-Mastercard_first-european-agentic-payment]] | 欧州初の本番 agentic payment フロー実装の詳細 |
| 2026-06-04 | [[2026-06-02_Worldline-ING-Mastercard_europe-first-live-agentic-payment]] | 欧州初ライブ agentic payment の続報：体制と技術詳細 |
| 2026-06-05 | [[2026-06-03_Mastercard_stablecoin-settlement-24-7-onchain]] | Mastercard の 24/7 ステーブルコイン決済本番展開——PSP 受け取りへの含意 |

### Fireblocks Flow — PSP 向けステーブルコイン受け取り

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-05-20 | [[2026-05-20_Fireblocks_agentic-payments-suite-x402-foundation]] | Agentic Payments Suite（Gateway + Wallets）ローンチと x402 Foundation 参加 |
| 2026-05-23 | [[2026-05-20_Fireblocks_agentic-payments-suite-x402]] | x402 Foundation 連携によるエージェント決済スイート詳細（PSP・フィンテック向け） |
| 2026-06-02 | [[2026-06-02_Fireblocks_flow-stablecoin-acceptance-psp-fintech]] | Fireblocks Flow：PSP・フィンテックがステーブルコイン受け取りを組み込めるインフラ |
| 2026-06-02 | [[2026-06-02_Fireblocks_flow-psp-stablecoin-acceptance]] | Flutterwave・Nuvion 経由 PSP ステーブルコイン受け取りの展開 |

### Adyen — Adyen Agentic

グローバル Top-5 PSP の Adyen がエンタープライズ向けエージェントコマース専用インフラを本番化。

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-06-16 | [[2026-06-16_Adyen_agentic-commerce-api-suite]] | Adyen Agentic 発表。Agentic Feed・Cart・Payments の 3 層 API で加盟店のエージェントコマース対応を支援 |

### Crossmint — エージェント向けカード発行

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-06-02 | [[2026-06-02_Crossmint_agentic-cards-visa-basis-theory]] | Crossmint が Visa + Basis Theory でエージェント向けプログラマブルカードを提供 |

### Circle — 返金・チャージバックプロトコル

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-06-18 | [[2026-06-18_Circle_refund-protocol-release]] | Circle が非カストディアル仲裁型ステーブルコイン返金プロトコルを公開——受取側が資金管理権を維持しながら第三者アービターが紛争を仲裁。ステーブルコイン決済の「返金・チャージバック不可」障壁の解消に向けた参照実装（現在脆弱性修正中、本番採用はセキュリティ監査完了後を推奨） |

### FV Bank — 規制銀行によるステーブルコイン請求書発行

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-06-18 | [[2026-06-18_FV-Bank_stablecoin-invoicing-agentic-platform]] | 米国チャーター銀行として初のステーブルコイン請求書発行（USDC/PYUSD→即時 USD 着金）ローンチ。agentic-ready 仮想カード・開発者 API を今後展開予定 |

### MiniPay / Gnosis Pay — ステーブルコイン残高の Visa 加盟店利用

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-06-23 | [[2026-06-23_MiniPay-Visa_stablecoin-card-gnosis-pay]] | Opera MiniPay が Gnosis Pay 経由 Visa デビットカードをローンチ。16M+ ウォレット・65 カ国以上のステーブルコイン残高を 175M+ Visa 加盟店で利用可能に。欧州・アフリカ・東南アジア・中南米対応 |

### マーチャント直接対応事例

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-04-21 | [[2026-04-21_DoorDash-Tempo_stablecoin-merchant-payouts]] | DoorDash が Tempo 経由でドライバー向けステーブルコインペイアウトを実装 |
| 2026-04-29 | [[2026-04-29_Meta_usdc-creator-payouts-stripe]] | Meta が Stripe 経由で USDC クリエイターペイアウトを展開 |
| 2026-05-10 | [[2026-05-10_PayPal-Google_consensus-miami-agentic-commerce]] | PayPal と Google が Consensus Miami でエージェントコマースの連携を発表 |
| 2026-05-11 | [[2026-05-11_Cryptorefills_x402-merchant-agent-payments-checkout]] | Cryptorefills が x402 対応チェックアウトを実装。ギフトカード・通話クレジット販売 |
| 2026-05-11 | [[2026-05-11_Cryptorefills_x402-agent-checkout-mcp]] | Cryptorefills が x402 + MCP サーバー + オープンソース参照実装を公開——180 か国・6,600 ブランド対応のエージェント向けチェックアウト |
| 2026-05-14 | [[2026-05-14_Stellagent_agentic-commerce-studio-merchant-readiness]] | Stellagent が AI エージェントに対応したマーチャントオンボーディングスタジオを提供 |
| 2026-05-20 | [[2026-05-20_Sui_gasless-stablecoin-transfers-fireblocks]] | Sui・Fireblocks のガスレスステーブルコイン送金：PSP・マーチャントの受け取りコスト削減 |
| 2026-05-22 | [[2026-05-19_Google_universal-cart-ap2-io2026]] | Google I/O 2026：Universal Cart・AP2 対応でマーチャントの AI エージェント対応加速 |
| 2026-05-26 | [[2026-05-26_Alipay_ai-wallet-token-pay-agentic-payments]] | Alipay AI Wallet・Token Pay：アジア市場向けエージェント決済 API |
| 2026-05-27 | [[2026-05-27_Robinhood_agentic-credit-card-trading]] | Robinhood Agentic Credit Card：カードレール上のエージェント決済実装 |
| 2026-05-27 | [[2026-05-27_Robinhood_agentic-trading-credit-card-agent-payments]] | Robinhood Agentic Trading + Credit Card：AI エージェントへの支出権限委任の先行実装 |
| 2026-05-28 | [[2026-05-28_Google_ucp-update-identity-linking-catalog-marketing-live]] | Google UCP/AP2 アップデート：アイデンティティリンク・カタログ・マーケティング本番化 |
| 2026-05-29 | [[2026-05-29_Shopify_ucp-catalog-developer-agentic-commerce]] | Shopify が UCP カタログ対応を開発者向けに展開——マーチャント readiness の具体例 |
| 2026-06-02 | [[2026-06-02_HeySavi-PayPal_uk-agentic-commerce-checkout]] | HeySavi が PayPal 連携で英国向けエージェントコマースチェックアウトを実装 |
| 2026-06-02 | [[2026-06-02_Coinbase-Checkout_stablecoin-merchant-payments]] | Coinbase × Checkout.com：マーチャント向けステーブルコイン決済受け取りソリューション |
| 2026-06-15 | [[2026-06-15_AWS-Coinbase_x402-cloudfront-waf-ai-traffic-monetization]] | AWS WAF が CloudFront 全体に x402 AI トラフィック課金を GA——コンソール変更のみで USDC ペイウォール設置可能に |
| 2026-06-22 | [[2026-06-22_MoonPay-Entendre_agentic-finance-accounting-agents]] | MoonPay が AI 経理エージェント Entendre を買収——ステーブルコイン決済の back-office 自動化（仕訳 93%）を垂直統合 |

---

## 対応レベルの分類

| レベル | 説明 | 代表事例 |
|---|---|---|
| **L3: ネイティブ対応** | エージェントが直接 API で決済。マーチャント側でエージェントを認識 | Cryptorefills（x402）, Agentic.market |
| **L2: PSP 経由対応** | PSP がエージェント決済を仲介。マーチャントは既存 API のまま | Stripe MPP, Fireblocks Flow |
| **L1: カード経由対応** | エージェントがカードを保持して既存カード決済フローを利用 | Visa TAP, Crossmint, MoonPay |
| **L0: 未対応** | エージェントが CAPTCHA・OTP・人間介入を求められる | 大多数の既存マーチャント |

---

## 地域別の進捗

| 地域 | 代表的な動き |
|---|---|
| 北米 | Stripe MPP, Visa Agentic-Ready, Coinbase x402, AWS AgentCore |
| 欧州 | Worldline-ING-Mastercard, MiCA 対応 PSP（BankingCircle 等）, HeySavi-PayPal UK |
| アジア | Mastercard-JD.com A2A, Alipay AI Wallet, OwlPay, WSPN W-Agent |

---

## 監視ポイント

- Visa Agentic-Ready 認定を取得したマーチャント・PSP の数（エコシステムの厚み）
- Stripe MPP の正式 GA と対応マーチャント数
- Worldline-ING-Mastercard 欧州連合の実稼働タイミング
- x402 対応マーチャントの増加速度（Agentic.market のサービス数で代替指標）
- ChatGPT + Visa 統合の取引量（大規模なコンシューマー向け事例として最重要）
- Circle refund protocol の脆弱性修正完了・セキュリティ監査結果と PSP 採用状況

---

## 関連ページ

- [[x402-ecosystem]] — x402 プロトコルエコシステム
- [[agent-payment-authorization]] — エージェント側の認可モデル
- [[Fireblocks]] — PSP 向けステーブルコイン受け取りインフラ
- [[Coinbase]] — x402 / Base エコシステム
- [[MOC_agent-payments-stack]] — エージェント決済スタック全体
