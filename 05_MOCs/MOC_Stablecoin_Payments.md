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
企業事例・プロトコル・規制の3軸で参照する。

---

## 全体構造

```
ステーブルコイン決済
├── 企業事例（送金・精算・ペイアウト）
├── インフラ・プロトコル → [[MOC_Protocols]]
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

### マネージド決済プラットフォーム

| ノート | 概要 |
|--------|------|
| [[2026-04-08_Circle_cpn-managed-payments]] | Circle CPN Managed Payments：銀行・PSP が暗号資産管理なしで USDC 決済利用可 |

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

---

## 関連 MOC

- [[MOC_Protocols]] — x402、CPN、Stellar、WDK などのプロトコル・インフラ
- [[MOC_Regulation]] — GENIUS Act、FinCEN/OFAC、BIS など規制動向
