---
title: "MOC: ステーブルコイン決済"
type: moc
updated: 2026-04-24
tags:
  - stablecoin
  - payments
  - psp
---

# MOC: ステーブルコイン決済

ステーブルコインを決済インフラとして活用する動きを横断的に整理するマップ。
企業事例・プロトコル・規制・主要企業の4軸で参照する。

---

## 全体構造

```
ステーブルコイン決済
├── 企業事例（送金・精算・ペイアウト）
├── インフラ・プロトコル → [[MOC_Protocols]]
├── 主要企業 → [[MOC_Companies]]
└── 規制・コンプライアンス → [[MOC_Regulation]]
```

---

## 企業事例

### B2B 法人送金・社内精算

| ノート | 概要 |
|--------|------|
| [[2026-03-07_Circle_usdc-internal-treasury]] | Circle が USDC で子会社間送金（6,800万ドルを30分以内） |
| [[2026-04-22_Veem-Bridge_stablecoin-accounts-launch]] | Veem が Bridge（Stripe傘下）採用、法人向けステーブルコイン口座・送金を提供 |

### 加盟店・プラットフォーム向けペイアウト

| ノート | 概要 |
|--------|------|
| [[2026-04-21_DoorDash-Tempo_stablecoin-merchant-payouts]] | DoorDash が Tempo チェーン上で40カ国以上の加盟店・配達員向けペイアウト |

### 国際送金・オン/オフランプ

| ノート | 概要 |
|--------|------|
| [[2026-04-22_MoneyGram-Stellar_usdc-latam-expansion]] | MoneyGram × Stellar、USDC 残高機能を中南米展開（現金化拠点50万拠点） |
| [[2026-06-02_MoneyGram_mgusd-stellar-launch]] | MoneyGram が Stellar 上で MGUSD ステーブルコインを本番ローンチ（発行体は Bridge） |

### マネージド決済プラットフォーム

| ノート | 概要 |
|--------|------|
| [[2026-04-08_Circle_cpn-managed-payments]] | Circle CPN Managed Payments：銀行・PSP が暗号資産管理なしで USDC 決済利用可 |
| [[2026-05-27_Circle-Nium_cpn-usdc-global-payouts]] | Circle × Nium：CPN 上の USDC 決済を Nium の 190 カ国・100 通貨ペイアウトに接続 |
| [[2026-06-11_MassPay-Coinbase_stablecoin-payouts]] | MassPay × Coinbase：USDC + CPN を活用したグローバルペイアウト展開 |

---

## 主要企業

| 企業 | 現在の位置づけ |
|------|----------------|
| [[Stripe]] | Bridge / Tempo / Privy / Link を組み合わせ、既存決済フローにステーブルコインを吸収 |
| [[Coinbase]] | x402 / Base / CDP / custody を軸に、オンチェーン決済とエージェント決済の開発者基盤を形成 |

---

## 注目テーマ

### PSP・PayFac の組み込み戦略
Bridge（Stripe傘下）が B2B プラットフォームに採用され、PSP がステーブルコイン機能を API として提供するモデルが確立しつつある。Veem、DoorDash の事例が参照モデル。

### オン/オフランプの実用化
MoneyGram の事例はステーブルコインが既存送金ネットワークと接続し、現金化まで一気通貫で機能することを示した。Swift 非依存の国際送金ルートが具体的に見えてきた。

### エージェント・機械向け決済
x402 プロトコルや Tether WDK が AI エージェントの自律的な支払いを想定した設計に進んでいる。Stripe / Tempo 側では、AI トークン消費に応じたストリーミング決済も出てきた。→ [[MOC_Protocols]]

| ノート | 概要 |
|--------|------|
| [[2026-05-13_Stripe-Tempo_streaming-stablecoin-payments]] | Stripe が Metronome の利用量トラッキングと Tempo 上のステーブルコイン・マイクロペイメントを組み合わせ、AI トークン単位の回収を構想 |
| [[2026-05-27_Block-CashApp_usdc-stablecoin-rollout-60m-users]] | Block / Cash App が 6,000 万ユーザーへの USDC ロールアウト——消費者向けステーブルコイン普及の先行事例 |
| [[2026-06-02_Fireblocks_flow-psp-stablecoin-acceptance]] | Fireblocks Flow：Flutterwave・Nuvion 経由で PSP がステーブルコイン受け取りを導入 |
| [[2026-06-03_Chainalysis_x402-100M-agentic-payments-base]] | Chainalysis が Base 上の x402 アジェンティック決済 1 億件突破を報告 |
| [[2026-06-03_Mastercard_stablecoin-settlement-expansion]] | Mastercard が 8 チェーン・6 ステーブルコインで 24/7 オンチェーン決済を本番展開 |
| [[2026-06-03_Stripe-Visa-Mastercard-Coinbase_stablecoin-consortium]] | Stripe・Visa・Mastercard・Coinbase が共同ステーブルコインプラットフォームを発表 |
| [[2026-06-03_Stripe-Visa-Mastercard_joint-stablecoin-platform-report]] | 同コンソーシアムの共同プラットフォームレポート詳細 |
| [[2026-06-10_Mastercard_agent-pay-for-machines-ap4m]] | Mastercard AP4M 正式ローンチ：35 社超パートナー、マルチレール対応 |
| [[2026-06-10_Ripple_xrpl-ai-starter-kit-x402-rlusd]] | Ripple が XRPL × x402 × RLUSD の AI エージェント向けスターターキットを公開 |
| [[2026-06-10_Visa_payments-forum-openai-agentic-commerce]] | Visa × OpenAI：ChatGPT 内での Visa カード決済連携・Agentic Registry を発表 |
| [[2026-06-15_AllUnity_sekau-june-target-missed]] | AllUnity が BaFin ライセンス取得目標を未達——EU MiCA 対応ステーブルコイン発行の遅延リスク |

---

## 関連 MOC

- [[MOC_Protocols]] — x402、CPN、Stellar、WDK などのプロトコル・インフラ
- [[MOC_Companies]] — Stripe、Coinbase など企業別の現状・ニュース紐付け
- [[MOC_Regulation]] — GENIUS Act、FinCEN/OFAC、BIS など規制動向
