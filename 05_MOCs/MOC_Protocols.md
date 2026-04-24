---
title: "MOC: ステーブルコイン決済プロトコル・インフラ"
type: moc
updated: 2026-04-24
tags:
  - stablecoin
  - payments
  - x402
  - agentic-commerce
---

# MOC: ステーブルコイン決済プロトコル・インフラ

決済を支えるプロトコル・SDK・ネットワーク層の動向を整理するマップ。
「誰が何のために使う基盤か」を軸に分類する。

---

## プロトコル別マップ

### x402 — AI エージェント・機械向けマイクロペイメント

| ノート | 概要 |
|--------|------|
| [[2026-04-02_x402-Foundation_linux-foundation-launch]] | x402 が Linux Foundation に移管。Google・Stripe・Visa が設立メンバー |

**特徴**: HTTP 402 ステータスを拡張し、API コール単位での自律的な支払いを実現。人間の介入なしにエージェントがサービスを購買できる設計。

### Circle CPN（Circle Payments Network）

| ノート | 概要 |
|--------|------|
| [[2026-04-08_Circle_cpn-managed-payments]] | CPN Managed Payments：銀行・PSP が USDC を暗号資産管理なしで利用可能 |

**特徴**: マネージドサービスとして提供し、参加機関がウォレット管理・鍵管理を自前で持たなくてよい設計。既存 PSP の参入障壁を下げる。

### Stellar ネットワーク — 国際送金・オン/オフランプ

| ノート | 概要 |
|--------|------|
| [[2026-04-22_MoneyGram-Stellar_usdc-latam-expansion]] | MoneyGram × Stellar で USDC 残高機能を中南米展開 |

**特徴**: 低コスト・高速の決済レイヤーとして機能。MoneyGram の現金拠点ネットワークとのオン/オフランプ統合が実証段階を超えた。

### Tempo ブロックチェーン — プラットフォーム向けペイアウト

| ノート | 概要 |
|--------|------|
| [[2026-04-21_DoorDash-Tempo_stablecoin-merchant-payouts]] | DoorDash が Tempo 上で加盟店・配達員への多通貨ペイアウトを実装 |

**特徴**: Stripe・Paradigm 支援。マーケットプレイス・ギグエコノミー向けのペイアウト最適化に特化。

### Tether WDK（Wallet Development Kit）

| ノート | 概要 |
|--------|------|
| [[2026-04-14_Tether_tether-wallet-launch]] | Tether が tether.wallet をローンチ、AI・機械向け WDK も公開 |

**特徴**: オープンソース SDK で人間・機械・AI エージェントが自己管理型ウォレットを構築できる。x402 と方向性が近い「エージェント経済」へのアプローチ。

### Bridge（Stripe 傘下）— API 型インフラ

| ノート | 概要 |
|--------|------|
| [[2026-04-22_Veem-Bridge_stablecoin-accounts-launch]] | Veem が Bridge を採用し法人向けステーブルコイン口座・送金を提供 |

**特徴**: B2B プラットフォームが自社プロダクトにステーブルコイン機能を埋め込む際の API レイヤー。コンプライアンス処理も API 側に委譲できる設計。

---

### ERC-8004（Trustless Agents）— AI エージェント間信頼インフラ

| ノート | 概要 |
|--------|------|
| [[ERC-8004_Trustless-Agents]] | AI エージェントの ID・評判・バリデーションを管理するオンチェーン・レジストリ群。x402 と組み合わせてエージェント経済の信頼レイヤーを担う |

**特徴**: Identity Registry（ERC-721 ベース）・Reputation Registry・Validation Registry の 3 コンポーネントで構成。直接の決済機能は持たず、x402 や ERC-4337 と組み合わせて使う。Draft ステータス、2026年1月メインネットデプロイ済み。

---

## 注目テーマ

### エージェント経済への対応
x402（Linux Foundation）、Tether WDK、ERC-8004 が相次いで登場し、AI エージェントによる自律決済の基盤整備が本格化している。x402 が「決済実行レイヤー」、ERC-8004 が「信頼・評判レイヤー」として補完関係にあり、スタック全体の標準化競争が焦点。

### マネージド vs セルフカストディ
Circle CPN（マネージド）と Tether WDK（自己管理）は対照的なアプローチ。前者は既存金融機関の参入を促し、後者はユーザー主権を前面に出す。市場ごとに採用モデルが分かれる可能性。

### PSP が選ぶインフラの多様化
Veem → Bridge、DoorDash → Tempo、MoneyGram → Stellar と、PSP・プラットフォームによってインフラ選択が異なる。ロックインリスクと機能適合性のトレードオフが設計判断のポイント。

---

## 関連 MOC

- [[MOC_Stablecoin_Payments]] — 企業事例・ユースケース全体
- [[MOC_Regulation]] — プロトコル採用に影響する規制動向
