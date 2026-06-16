---
title: "MOC: ステーブルコイン決済プロトコル・インフラ"
type: moc
updated: 2026-06-15
tags:
  - stablecoin
  - payments
  - x402
  - agentic-commerce
  - agent-payments
---

# MOC: ステーブルコイン決済プロトコル・インフラ

決済を支えるプロトコル・SDK・ネットワーク層の動向を整理するマップ。
「誰が何のために使う基盤か」を軸に分類する。

---

## エージェント決済プロトコル全体像

AI エージェントが自律的に決済を行うために必要な「層」を整理する。各プロトコルは排他的な競合ではなく、解いている問題のレイヤーが異なる。

```
[ 認証・アイデンティティ層 ]  AP2（Google/FIDO）, Visa TAP, ERC-8004
         ↓
[ 支払いプロトコル層     ]  x402（HTTP）, MPP（Stripe）, Mastercard A2A
         ↓
[ 決済実行層           ]  USDC（Circle/Coinbase）, Tether WDK
         ↓
[ 取引・エスクロー層     ]  ERC-8183（Agentic Commerce）
         ↓
[ 調整・ルーティング層   ]  OTL（Fireblocks/Checkout.com/Robinhood）
```

### 認証・アイデンティティ層

| プロトコル | 主体 | 概要 |
|---|---|---|
| AP2（Agentic Payment Protocol） | Google / FIDO Alliance | デバイスバインドの passkey でエージェントのアイデンティティを証明。エンドユーザーの委任を安全に表現 |
| Visa TAP（Trusted Agent Protocol） | Visa | カードネットワークがエージェントの信頼を保証。既存加盟店・PSP と互換 |
| ERC-8004（Trustless Agents） | Ethereum Foundation | オンチェーンの ID・評判・バリデーションレジストリ。AI エージェント間の信頼確立 |

関連ノート:
- [[2026-04-28_Google_ap2-fido-alliance]]
- [[2026-05-28_Visa-Replit_trusted-agent-protocol]]
- [[ERC-8004_Trustless-Agents]]

詳細:
- [[ap2-agent-payments-protocol]]
- [[visa-tap-trusted-agent-protocol]]
- [[ERC-8004_Trustless-Agents]]

### 支払いプロトコル層

| プロトコル | 主体 | 概要 |
|---|---|---|
| x402 | Coinbase / Linux Foundation | HTTP 402 拡張。API・コンテンツ・AI サービスをリクエスト単位でオンチェーン決済。OSSで標準化済み |
| MPP（Machine Payments Protocol） | Stripe | Stripe インフラを通じてエージェントが加盟店へ決済。既存カード/銀行レールを活用 |
| Mastercard A2A | Mastercard | エージェント間（B2B）の清算フレームワーク。Mastercard のカードネットワーク上で動作 |
| AP4M（Agent Pay for Machines） | Mastercard | A2A をマシン間決済に特化させた拡張。2026-06-10 発表 |
| Circle Agent Stack | Circle | USDC 上のナノペイメント・エージェントウォレット・認可スコープ管理のコンポーネント群 |

関連ノート:
- [[2026-04-02_x402-Foundation_linux-foundation-launch]]
- [[2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments]]
- [[2026-04-30_Mastercard_q1-2026-agent-to-agent-payments]]
- [[2026-06-10_Mastercard_agent-pay-for-machines-ap4m]]
- [[2026-05-11_Circle_agent-stack-nanopayments-agentic-economy]]

詳細 → [[x402]] · [[mpp-machine-payments-protocol]] · [[x402-ecosystem]] · [[agent-payment-authorization]]

### 取引・エスクロー層

| プロトコル | 主体 | 概要 |
|---|---|---|
| ERC-8183（Agentic Commerce） | Ethereum Foundation + Virtuals Protocol | AI エージェント間でのジョブ委託・評価・決済を仲裁なしで行うオンチェーン・エスクロー標準 |

関連ノート:
- [[ERC-8183_Agentic-Commerce]]

### 調整・ルーティング層

| プロトコル | 主体 | 概要 |
|---|---|---|
| OTL（Open Transaction Layer） | Fireblocks / Checkout.com / Robinhood | エージェント間の支払い調整・ルーティングを担うオープンレイヤー。2026-05 に構想公開 |

関連ノート:
- [[2026-05-28_OTL_open-transaction-layer-agentic-coordination]]

---

### プロトコル比較表

| 観点 | x402 | MPP | AP2/TAP | A2A/AP4M |
|---|---|---|---|---|
| **レール** | オンチェーン（USDC/ERC-20） | カード/銀行 | カード/標準 | カード |
| **主な利用場面** | API 課金・AI マイクロペイメント | 加盟店決済 | 委任・認証 | B2B・機械間 |
| **標準化** | Linux Foundation（OSSで公開済み） | Stripe 独自 | FIDO Alliance / Visa | Mastercard |
| **AWS AgentCore での扱い** | 採用 | 採用 | — | — |
| **実取引実績** | 1億件超（Base、2026-06-03時点） | 未公開 | — | — |

---

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

### ERC-8183（Agentic Commerce）— AI エージェント間エスクロー・取引標準

| ノート | 概要 |
|--------|------|
| [[ERC-8183_Agentic-Commerce]] | AIエージェント同士が仲裁なしにジョブを委託・評価・決済できるオンチェーン・エスクロー標準。Ethereum Foundation + Virtuals Protocol 共同提案 |

**特徴**: 6状態のステートマシンでジョブライフサイクルを管理。Client・Provider・Evaluator の3役割を定義し、評価者アテステーションで成果物の完了/拒否を決定する。x402（決済実行）・ERC-8004（信頼確立）と組み合わせてエージェント経済の取引レイヤーを担う。Base・BNB Chain で稼働実績あり、Draft ステータス。

---

### プライバシー・ステルス決済

| ノート | 概要 |
|-------|------|
| [[ERC-5564_Stealth-Addresses]] | 送信者が受取人の公開鍵から使い捨てステルスアドレスを生成。受取人の紐づけを防ぐ受取人プライバシー規格。Standards Track・アクティブ |
| [[EIP-7503_ZK-Wormholes]] | ETH をバーンアドレスに送付し ZK 証明でバーン事実を証明→プロトコルが新アドレスにミント。送受信リンクを切断するコア変更型提案。Stagnant |
| [[EIP-8182_Private-ETH-ERC20-Transfers]] | ベースレイヤー内蔵のシールドプールと ZK 証明プリコンパイルで ETH・ERC-20 のネイティブプライベート送金を実現。標準アドレス / ENS 宛てに送金可能。2026-04-24 提出の最新 Draft |

**特徴**: 3 提案はプライバシーの「深度」と「実現レイヤー」が異なる。ERC-5564 は受取人プライバシーのみでアプリ層実装が可能。EIP-7503 は送受信リンクを切断するがコア変更が必要で Stagnant。EIP-8182 は最も包括的だが Draft 段階でハードフォーク必要。いずれもコンプライアンス（KYT・Travel Rule）との両立が普及の鍵になる。

---

## 注目テーマ

### エージェント経済への対応
x402（Linux Foundation）、ERC-8004、ERC-8183、Tether WDK が相次いで登場し、AI エージェントによる自律決済の基盤整備が本格化している。x402 が「決済実行レイヤー」、ERC-8004 が「信頼・評判レイヤー」、ERC-8183 が「エスクロー・取引レイヤー」として補完関係にあり（Ethereum Foundation が dAI スタックとして整理）、スタック全体の標準化競争が焦点。

### マネージド vs セルフカストディ
Circle CPN（マネージド）と Tether WDK（自己管理）は対照的なアプローチ。前者は既存金融機関の参入を促し、後者はユーザー主権を前面に出す。市場ごとに採用モデルが分かれる可能性。

### プロトコルレイヤーへのプライバシー組み込み
ERC-5564（アプリ層・受取人匿名化）・EIP-7503（コア層・送受信リンク切断）・EIP-8182（コア層・完全プライベート送金）と、プライバシー実装の「深度」をめぐる提案が並存している。Tornado Cash の制裁（2022年）以降、アプリ層ミキサーは規制リスクが高く、代替として Privacy Pools 概念（Vitalik 提案）や ZK ベースのコンプライアンス証明が注目されている。ステーブルコイン決済への応用では、KYT・FATF Travel Rule との両立設計が採否の鍵になる。

### PSP が選ぶインフラの多様化
Veem → Bridge、DoorDash → Tempo、MoneyGram → Stellar と、PSP・プラットフォームによってインフラ選択が異なる。ロックインリスクと機能適合性のトレードオフが設計判断のポイント。

---

## 関連 MOC

- [[MOC_Stablecoin_Payments]] — 企業事例・ユースケース全体
- [[MOC_Regulation]] — プロトコル採用に影響する規制動向
