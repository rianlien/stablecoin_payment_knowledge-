---
title: "トークン化預金（Tokenized Deposits）"
type: topic
updated: 2026-06-15
tags:
  - tokenized-deposits
  - bank-competition
  - stablecoin-regulation
  - payment-rails
  - GENIUS-Act
---

# トークン化預金（Tokenized Deposits）

銀行が自行の顧客預金をブロックチェーン上でトークンとして表現し、24/7 即時決済・プログラマブルな資金移動を可能にする仕組み。ステーブルコイン（USDC・USDT 等）と機能的に類似しながら、FDIC 保険の対象となる銀行システム内に資金を保持する点で異なる。2026 年に入り、米国大手銀行連合・Fiserv・欧州 Banking Circle 等が具体的な展開計画を打ち出しており、ステーブルコインとの規制上・競合上の関係を整理する必要性が高まっている。

---

## 全体像

### 背景：なぜ今、銀行がトークン化預金を動かすのか

GENIUS Act・CLARITY Act（米国）の立法進展によって、Circle USDC や Tether USDT のようなステーブルコインが合法的・大規模に普及する経路が生まれつつある。銀行業界が最も危惧するのは「預金のデポジット・フライト」——顧客が銀行預金をステーブルコイン（または暗号資産ウォレット）に移し替えることで、銀行の資金調達基盤が侵食されるシナリオ。トークン化預金は、この脅威に対する銀行側の防衛的かつ攻撃的な応答として位置づけられる。

### 主なアプローチ

**1. 銀行連合モデル（The Clearing House ネットワーク）**
JPMorgan・Citi・BofA・Wells Fargo が The Clearing House（銀行共同所有の決済インフラ）を通じて共有トークン化預金ネットワークを 2027 年上半期に構築する計画。ターゲットは大企業のプログラマブル財務管理・クロスボーダー決済。現行の RTP（Real-Time Payments）ネットワークとの統合が想定される。

**2. コアバンキングプロバイダーモデル（Fiserv FIUSD）**
Fiserv が約 1 万の銀行・信用組合に展開できる FIUSD（Financial Institution U.S. Dollar）を 2026 年 7 月にローンチ。各銀行・信用組合が自行ブランドのステーブルコインを独自発行できる分散型モデル。GENIUS Act 準拠設計で、Bank of North Dakota がパイロットパートナー。

**3. 規制準拠インフラモデル（Banking Circle EURI 等）**
EU では Banking Circle が MiCA に基づく CASP ライセンスを取得し、USDC・USDG・EURI（自社発行 EUR ステーブルコイン）の決済清算を銀行コアインフラから直接提供。厳密にはトークン化預金ではなく MiCA 準拠のステーブルコインだが、「規制済み銀行がステーブルコインを運営する」という接近経路は同系統。

### ステーブルコインとの主な差異

| 観点 | ステーブルコイン（USDC 等） | トークン化預金 |
|---|---|---|
| 発行主体 | ノンバンク（Circle・Tether 等） | 銀行（JPMorgan・各地銀等） |
| FDIC 保険 | 原則なし | 対象となる可能性が高い |
| 規制経路 | GENIUS Act の PPSI 認定 | 既存銀行規制で対応できる可能性 |
| 準備資産 | 外部の米国債・現金等 | 銀行の貸借対照表内に維持 |
| オープン性 | ERC-20 等の公開標準 | 独自設計の可能性あり（未確定） |

---

## 主要ノート

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-06-05 | [[2026-06-05_JPMorgan-Citi-BofA_tokenized-deposit-network]] | JPMorgan・Citi・BofA・Wells Fargo が The Clearing House 経由で 2027 年上半期にトークン化預金ネットワーク構築計画（WSJ 報道） |
| 2026-06-03 | [[2026-06-03_Fiserv_fiusd-bank-stablecoin-genius-act]] | Fiserv が GENIUS Act 準拠の銀行向けステーブルコイン FIUSD を 7 月ローンチ予定、Bank of North Dakota がパイロット |
| 2026-04-27 | [[2026-04-27_BankingCircle_mica-stablecoin-settlement]] | Banking Circle が MiCA CASP ライセンス取得後に USDC・USDG・EURI の決済清算サービスをローンチ（EU） |
| 2026-03-07 | [[2026-03-07_Circle_usdc-internal-treasury]] | Circle が USDC を社内資金移動に活用、8 子会社間 6,800 万ドルを 30 分以内に決済（ステーブルコインとの比較基準） |

---

## 現状の論点

- **規制上の扱い：** 銀行が発行するトークン化預金は GENIUS Act の PPSI（Permitted Payment Stablecoin Issuer）の定義に含まれるのか、それとも既存の銀行規制で完結するのか。この解釈によって、参入コスト・タイムラインが大きく変わる
- **技術標準：** The Clearing House ネットワークや Fiserv FIUSD がオープン標準（ERC-20 等）を採用するか、閉じた独自設計になるかは未確定。閉じた設計になれば x402・AP2 等のエージェント決済プロトコルとの統合コストが高くなる
- **相互運用性：** 銀行トークン化預金と USDC の間でクロスレール決済が可能になるか、それとも「銀行トークン圏」と「ステーブルコイン圏」が分断されるか。エージェント決済インフラがマルチレール対応を求められるかどうかに直結する
- **タイムライン格差：** Fiserv FIUSD が 2026 年 7 月、The Clearing House ネットワークが 2027 年上半期と、銀行側の展開には段差がある。Circle USDC は既に稼働しており短中期の設計に直接影響するのは USDC 優位の状態が続く

---

## 監視ポイント

- The Clearing House による公式発表（2026 年後半）と参加銀行数の拡大
- Fiserv FIUSD の 7 月ローンチ実現と、Clover（約 200 万台 POS）への統合計画
- GENIUS Act 最終規則（7/18 デッドライン）：銀行トークン化預金が PPSI 定義に含まれるかどうかの明確化
- x402・AP2・Mastercard AP4M が銀行トークン化預金への対応を発表するか
- 他のコアバンキングプロバイダー（FIS・Jack Henry）の同等製品発表
- EU 圏での Banking Circle モデルが他欧州銀行に波及するか

---

## 関連ページ

- [[MOC_Regulation]]
- [[x402-ecosystem]]
- [[psp-merchant-readiness]]
- [[agent-payment-authorization]]
