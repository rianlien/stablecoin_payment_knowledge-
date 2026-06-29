---
title: "MOC: ステーブルコイン決済"
type: moc
updated: 2026-06-29
tags:
  - stablecoin
  - payments
  - psp
---

# MOC: ステーブルコイン決済

ステーブルコインを決済インフラとして活用する動きを横断的に整理するマップ。
企業事例・プロダクト・プロトコル・規制・主要企業の5軸で参照する。

---

## 全体構造

```
ステーブルコイン決済
├── 企業事例（送金・精算・ペイアウト）
├── プロダクト比較 → [[06_Entities/Products/index|Product Notes]]
├── インフラ・プロトコル → [[MOC_Protocols]]
├── 主要企業 → [[MOC_Companies]]
└── 規制・コンプライアンス → [[MOC_Regulation]]
```

---

## プロダクト比較

| 観点 | 参照先 | 用途 |
|---|---|---|
| Agent payments / x402 | [[06_Entities/Products/Agent-Payments-x402/index|Agent Payments / x402]] | AI agent、MCP、pay-per-call API、machine payment の比較 |
| Checkout / merchant acceptance | [[06_Entities/Products/Checkout-Merchant-Acceptance/index|Checkout / Merchant Acceptance]] | 加盟店・PSP が stablecoin acceptance を導入する時の候補比較 |
| Invoicing / business ops | [[06_Entities/Products/Invoicing-Business-Ops/index|Invoicing / Business Ops]] | 請求、法人支払い、カード、finance ops への適用比較 |
| Settlement / payouts | [[06_Entities/Products/Settlement-Payouts/index|Settlement / Payouts]] | B2B settlement、cross-border payout、managed settlement の比較 |
| Wallets / cards | [[06_Entities/Products/Wallets-Cards/index|Wallets / Cards]] | end-user wallet、business card、stablecoin-backed spend UX の比較 |
| Compliance / risk | [[06_Entities/Products/Compliance-Risk/index|Compliance / Risk]] | AML、screening、authorization、x402 attack surface の比較 |

全体索引: [[06_Entities/Products/index|Product Notes]]

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
| [[2026-06-22_MoneyGram-Solana_validator-developer-platform]] | MoneyGram が Solana のバリデーターに参加＋機関向け Developer Platform に加盟——Stellar（MGUSD）＋ Solana の 2 チェーン戦略へ移行 |
| [[2026-06-24_Ripple-SBI_rlusd-japan-jfsa-launch]] | Ripple × SBI が RLUSD の日本ローンチ——JFSA「第4種電子決済手段」認可取得、外国発行ステーブルコインとして国内初 |
| [[2026-06-25_Circle-Nomura_usdc-japan-fx-settlement]] | Circle × 野村が USDC で日本企業向け FX 即時決済プラットフォームを構築発表——日次 4,400 億ドル FX 市場、2027 年ローンチ目標 |

### マネージド決済プラットフォーム

| ノート | 概要 |
|--------|------|
| [[2026-04-08_Circle_cpn-managed-payments]] | Circle CPN Managed Payments：銀行・PSP が暗号資産管理なしで USDC 決済利用可 |
| [[2026-05-27_Circle-Nium_cpn-usdc-global-payouts]] | Circle × Nium：CPN 上の USDC 決済を Nium の 190 カ国・100 通貨ペイアウトに接続 |
| [[2026-06-11_MassPay-Coinbase_stablecoin-payouts]] | MassPay × Coinbase：USDC + CPN を活用したグローバルペイアウト展開 |
| [[2026-06-24_Invesco-Superstate_stablecoin-reserves-onchain-fund]] | Invesco が GENIUS Act 準拠の stablecoin 準備金向けオンチェーン MMF（Superstate 技術）を SEC に申請——主要 TradFi が GENIUS Act 準拠専用インフラを初提供 |

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
MoneyGram の事例はステーブルコインが既存送金ネットワークと接続し、現金化まで一気通貫で機能することを示した。Swift 非依存の国際送金ルートが具体的に見えてきた。2026-06-24〜25 には日本市場でも外国ステーブルコインが本格参入——RLUSD（Ripple × SBI、JFSA 認可）と USDC（Circle × 野村、2027 年ローンチ目標）が日次 4,400 億ドルの日本 FX 市場をターゲットにほぼ同時期に動いた。改正資金決済法の完全施行が直接の契機であり、G3 以外の主要市場での実案件が初めて形成された。

### エージェント・機械向け決済
x402 プロトコルが急速に普及し、2026-06 時点で Base 上の x402 取引が 1 億件を突破（Chainalysis 報告）。当初は USD（USDC on Base/Arbitrum）中心だったが、2026-06-19 に AllUnity が EU 初の非 USD x402 決済レール（SEKAU × SEPA 精算）を本番稼働させ、地理・通貨の多様化が始まった。Visa TAP・Mastercard AP4M・Google AP2 など既存カードネットワーク側も独自のエージェント認証・決済フローを整備し、x402 系プロトコルとの競合・共存の構図が明確になってきている。→ [[MOC_Protocols]]

| ノート | 概要 |
|--------|------|
| [[2026-05-13_Stripe-Tempo_streaming-stablecoin-payments]] | Stripe が Metronome の利用量トラッキングと Tempo 上のステーブルコイン・マイクロペイメントを組み合わせ、AI トークン単位の回収を構想 |
| [[2026-05-27_Block-CashApp_usdc-stablecoin-rollout-60m-users]] | Block / Cash App が 6,000 万ユーザーへの USDC ロールアウト——消費者向けステーブルコイン普及の先行事例 |
| [[2026-06-02_Fireblocks_flow-psp-stablecoin-acceptance]] | Fireblocks Flow：Flutterwave・Nuvion 経由で PSP がステーブルコイン受け取りを導入 |
| [[2026-06-03_Chainalysis_x402-100M-agentic-payments-base]] | Chainalysis が Base 上の x402 アジェンティック決済 1 億件突破を報告 |
| [[2026-06-03_Mastercard_stablecoin-settlement-24-7-onchain]] | Mastercard が USDC・PYUSD・RLUSD を含む 6 種ステーブルコインで 8 チェーン 24/7 オンチェーン決済を本番展開（Cross River・Nuvei 等が先行採用） |
| [[2026-06-03_Mastercard_stablecoin-settlement-expansion]] | Mastercard が 8 チェーン・6 ステーブルコインで 24/7 オンチェーン決済を本番展開 |
| [[2026-06-03_Stripe-Visa-Mastercard-Coinbase_stablecoin-consortium]] | Stripe・Visa・Mastercard・Coinbase が共同ステーブルコインプラットフォームを発表 |
| [[2026-06-03_Stripe-Visa-Mastercard_joint-stablecoin-platform-report]] | 同コンソーシアムの共同プラットフォームレポート詳細 |
| [[2026-06-10_Mastercard_agent-pay-for-machines-ap4m]] | Mastercard AP4M 正式ローンチ：35 社超パートナー、マルチレール対応 |
| [[2026-06-10_Ripple_xrpl-ai-starter-kit-x402-rlusd]] | Ripple が XRPL × x402 × RLUSD の AI エージェント向けスターターキットを公開 |
| [[2026-06-10_Visa_payments-forum-openai-agentic-commerce]] | Visa × OpenAI：ChatGPT 内での Visa カード決済連携・Agentic Registry を発表 |
| [[2026-06-15_AllUnity_sekau-june-target-missed]] | AllUnity が BaFin ライセンス取得目標を未達——EU MiCA 対応ステーブルコイン発行の遅延リスク |
| [[2026-06-19_AllUnity_sekau-launch-agentic-payments]] | AllUnity が SEKAU（SEK MiCAR 準拠 EMT）と x402 Agentic Payments を正式ローンチ——EU 初の非 USD x402 決済レールが稼働 |
| [[2026-06-22_MoonPay-Entendre_agentic-finance-accounting-agents]] | MoonPay が AI 経理エージェント Entendre を買収——仕訳 93% 自動化でステーブルコイン決済の back-office agentic finance を垂直統合 |

---

## 関連 MOC

- [[MOC_Protocols]] — x402、CPN、Stellar、WDK などのプロトコル・インフラ
- [[MOC_Companies]] — Stripe、Coinbase など企業別の現状・ニュース紐付け
- [[MOC_Regulation]] — GENIUS Act、FinCEN/OFAC、BIS など規制動向
- [[06_Entities/Products/index|Product Notes]] — PM視点のプロダクトカテゴリ別比較
