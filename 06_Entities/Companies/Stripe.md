---
title: "Stripe"
type: company
updated: 2026-06-18
category: payments
tags:
  - stablecoin
  - payments
  - psp
  - agentic-commerce
  - company
aliases:
  - Bridge
  - Tempo
  - Privy
---

# Stripe

Stripe は、既存の PSP / PayFac 基盤にステーブルコイン・エージェント決済・ウォレット・トレジャリー機能を組み込み、法定通貨圏とオンチェーン決済を接続する方向で動いている。

この vault では、Stripe を「ステーブルコインを単体プロダクトではなく、既存の決済・送金・残高管理フローへ吸収する企業」として追う。

---

## 現状の要約

### 何をしているか

- **ステーブルコイン決済の PSP 化**: Link / Checkout / Payment Links / Elements など既存 Stripe フローにステーブルコイン受け取りを組み込む。32 市場追加（Sessions 2026）。
- **Bridge によるオン/オフランプ・清算レイヤー化**: Bridge を通じて多通貨・多チェーン・企業向け送金の裏側を担う。Celo に対応（2026-05-12）し 66 か国以上の USDC オンランプ・オフランプが単一 API で利用可能に。
- **Tempo / MPP による機械決済**: AI エージェントやサービスがプログラムで支払える Machine Payments Protocol（MPP）を展開。Stripe × Tempo によるストリーミング決済（AI トークン利用量に応じた課金）も実装（2026-05-13）。
- **Shared Payment Tokens（SPT）によるエージェント決済の支払い手段拡張**: 2026-06-16 に Zip US が SPT 経由で BNPL をエージェントコマースに統合。エージェント起点取引における支払い手段が Stripe カード決済から BNPL 等へ拡張。
- **Privy / Link によるウォレット化**: エージェント・ユーザー・クリエイター向けのウォレット発行、支出管理、受け取り導線を整える。
- **Treasury / stablecoin payouts の拡張**: 企業残高、グローバル送金、ステーブルコイン払い出しを既存の金融オペレーションに近い形で提供する。
- **Visa・Mastercard・Coinbase との共同ステーブルコインプラットフォーム計画（報道段階）**: 2026-06-03 に The Information が報道。Stripe が既存ネットワーク各社と組んで独自ステーブルコインを発行するプラットフォームを検討中。詳細・発表時期は未確定。

### 見立て

Stripe の戦略は「暗号資産らしさ」を前面に出すより、加盟店やプラットフォームが意識せず使える金融 API にステーブルコインを吸収すること。Bridge、Tempo、Privy、Link、Treasury を組み合わせることで、受け取り・保管・送金・ウォレット・エージェント決済まで垂直統合しようとしている。

Visa・Mastercard・Coinbase との共同ステーブルコインプラットフォーム計画の報道（2026-06-03）は、Stripe が単独 PSP から業界連合の一角へと転換する可能性を示す。実現すれば Bridge による清算インフラと自社発行ステーブルコインが連携し、Circle USDC との差別化軸が鮮明になる。ただし情報リーク段階であり、設計・発表時期は未確定。

---

## 主要レイヤー

| レイヤー | Stripe の動き | 意味 |
|---|---|---|
| 決済受付 | Link / Checkout で stablecoin acceptance を拡張 | 加盟店は USD 着金のまま、顧客は任意ウォレットで支払える方向 |
| 送金・清算 | Bridge による多通貨・多チェーン対応 | PSP / B2B プラットフォームの裏側に入る |
| ウォレット | Privy / Link agent wallet | ユーザー・エージェント・開発者の支払い主体を管理 |
| エージェント決済 | MPP / streaming payments | API・AI 推論・マイクロペイメントの課金単位を細かくする |
| 企業資金管理 | Treasury / stablecoin payouts | 法定通貨とステーブルコイン残高を同じ運用面で扱う |

---

## Inbox との紐付け

### 中核ニュース

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-30 | [[2026-04-30_Stripe-Sessions-2026_stablecoin-expansion]] | ステーブルコイン受け入れ市場、Bridge、Privy、Treasury の大規模拡張 |
| 2026-05-12 | [[2026-05-12_Celo_bridge-stripe-consensus-miami]] | Stripe 傘下 Bridge が Celo に対応——単一 API で 66 か国以上の USDC オンランプ・オフランプが可能に |
| 2026-05-13 | [[2026-05-13_Stripe-Tempo_streaming-stablecoin-payments]] | Stripe × Tempo が AI トークン利用量に応じたステーブルコイン・ストリーミング決済を実装 |
| 2026-04-30 | [[2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments]] | MPP、Link エージェントウォレット、Shared Payment Tokens の発表 |
| 2026-05-06 | [[2026-05-06_RedotPay-Tempo_mpp-agentic-payments-launch]] | MPP が RedotPay で実稼働した事例 |
| 2026-05-07 | [[2026-05-07_AWS_bedrock-agentcore-payments-x402]] | AWS AgentCore で Stripe / Privy がウォレット選択肢として組み込まれた事例 |
| 2026-06-03 | [[2026-06-03_Stripe-Visa-Mastercard-Coinbase_stablecoin-consortium]] | Visa・Mastercard・Coinbase と共同ステーブルコインプラットフォームを発表 |
| 2026-06-04 | [[2026-06-03_Stripe-Visa-Mastercard_joint-stablecoin-platform-report]] | Visa・Mastercard・Coinbase 共同ステーブルコインプラットフォームレポート |

### Bridge / Tempo の採用事例

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-22 | [[2026-04-22_Veem-Bridge_stablecoin-accounts-launch]] | B2B 送金プラットフォームが Bridge を採用 |
| 2026-04-21 | [[2026-04-21_DoorDash-Tempo_stablecoin-merchant-payouts]] | 3者間マーケットプレイスのペイアウトに Tempo を採用 |
| 2026-04-28 | [[2026-04-28_OnePay-Tempo_stablecoin-payouts-partnership]] | Walmart 系フィンテック OnePay と Tempo の提携 |
| 2026-04-29 | [[2026-04-29_OnePay-Tempo_stablecoin-payouts-walmart]] | OnePay / Walmart 文脈での Tempo 採用続報 |
| 2026-04-29 | [[2026-04-29_Meta_usdc-creator-payouts-stripe]] | Meta クリエイター報酬支払いで Stripe Link を採用 |

### 周辺ニュース

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-02 | [[2026-04-02_x402-Foundation_linux-foundation-launch]] | Stripe は [[x402 Foundation]] 創設メンバーでもある |
| 2026-04-29 | [[2026-04-29_Visa_stablecoin-settlement-9chains-7b]] | Visa が Tempo / Base / Arc などを清算対象に拡張 |
| 2026-05-10 | [[2026-05-10_PayPal-Google_consensus-miami-agentic-commerce]] | agentic commerce の業界標準化文脈 |
| 2026-06-16 | [[2026-06-16_Zip-Stripe_shared-payment-tokens-agentic]] | Zip US が Stripe SPT を採用——BNPL をエージェントコマースに拡張 |

---

## 競争上の論点

### x402 との関係

Stripe は [[x402 Foundation]] に参加しつつ、独自に MPP / Tempo を推進している。現時点では、MPP が [[x402]] の代替標準なのか、Tempo エコシステム向けの補完レイヤーなのかが未確定。

### Circle / Coinbase との違い

- Circle は USDC 発行体としてネットワークと流動性を押さえる。
- Coinbase は x402 / Base / wallet / custody を軸に、オンチェーン決済の開発者基盤を押さえる。
- Stripe は加盟店・プラットフォームの既存決済フローに入り込み、法定通貨とステーブルコインの変換を抽象化する。

### 導入判断への示唆

Stripe は、既に Stripe を使う企業にとって導入摩擦が低い。一方で、プロトコルのオープン性、MPP と x402 の相互運用性、地域別の規制対応は確認が必要。

---

## 監視ポイント

- **Visa・Mastercard・Coinbase 共同ステーブルコインプラットフォームの詳細**: 名称・トークン設計・準備金構造・発行体・公式発表タイミング
- **SPT（Shared Payment Tokens）の拡張**: Affirm・Klarna 等他 BNPL プロバイダーの対応状況、エージェントが BNPL を選択した際のキャンセル・リスク管理設計
- **MPP 仕様が公開標準としてどこまで外部実装可能になるか**
- **Tempo ストリーミング決済の実稼働トランザクション量と主要採用企業**
- **Bridge の Celo 対応後の新興国向けオフランプ実績**（66 か国・単一 API の実取引量）
- **Link stablecoin acceptance の対象国・対象フローの拡大**
- **Stripe が x402 と MPP をどう棲み分けるか**

---

## 関連 MOC

- [[MOC_Companies]]
- [[MOC_Stablecoin_Payments]]
- [[MOC_Protocols]]
- [[MOC_agent-payments-stack]]

---

## 参考リンク

- 一次情報: [Stripe Sessions 2026 newsroom](https://stripe.com/newsroom/news/sessions-2026)
- 補足情報: [Stripe stablecoin growth overview](https://stripe.com/resources/more/behind-stablecoin-growth)
- 補足情報: [Stripe Sessions 2026 stablecoin talk](https://stripe.com/sessions/2026/best-of-both-rails)
