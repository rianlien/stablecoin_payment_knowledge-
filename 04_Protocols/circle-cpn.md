---
title: "Circle Payments Network (CPN)"
type: protocol
updated: 2026-06-15
category: payment-rails
tags:
  - stablecoin
  - payment-rails
  - agentic-commerce
  - cross-border
  - circle
---

# Circle Payments Network (CPN)

Circle Payments Network（CPN）は、Circle が運営するグローバル B2B 決済ネットワーク。銀行・PSP・フィンテック・企業が USDC 決済レールにアクセスするための共通基盤として機能し、参加機関が直接ブロックチェーンインフラを管理することなくステーブルコイン決済を導入できる。2026 年に入り CPN Managed Payments（フルマネージド層）のローンチ、Nium によるグローバルペイアウト統合、Kyriba 経由のエンタープライズ財務 TMS 連携と急速にエコシステムが拡大している。

この vault では、CPN を「USDC を法定通貨決済インフラに接続するグローバル B2B 決済レール」として追う。

---

## プロトコル概要

| 項目 | 内容 |
|---|---|
| 運営主体 | Circle Internet Financial |
| 対象参加者 | 銀行、PSP、フィンテック、グローバル企業 |
| 決済通貨 | USDC（Circle 発行ステーブルコイン） |
| 年換算処理量 | $83 億（2026 年 3 月末時点） |
| ペイアウトカバレッジ | 190 カ国・100 通貨（Nium 統合後） |
| ローンチパートナー（CPN Managed Payments） | Veem、Thunes、Worldline |

---

## アーキテクチャ

CPN は 2 層構造で設計されている。

**CPN コアレール（参加型）**
参加機関が Circle と直接接続し、USDC を用いたセトルメントを実行するベースレイヤー。USDC のミント・バーン、コンプライアンス管理、ブロックチェーンインフラは Circle が一括管理する。

**CPN Managed Payments（フルマネージド層）**
2026 年 4 月 8 日に正式ローンチ。デジタル資産の自己管理が不要なフルマネージド接続。PSP や銀行はフィアット通貨で取引でき、USDC の技術的詳細を抽象化できる。参加機関のステーブルコイン導入障壁を実質的に撤廃する設計。

**グローバルペイアウト層（Nium 統合）**
2026 年 5 月 27 日、Nium が CPN のグローバルペイアウトパートナーに参加。CPN 上の USDC 決済後、Nium の 190 カ国・100 通貨払い出しネットワークに単一 API で到達可能になった。プリファンディング削減とオンチェーン透明性によるリアルタイムトラッキングを実現。

---

## アジェンティックコマースとの関係

Circle VP Spencer Spinelli は Nium 統合発表の声明で、CPN の設計意図を明示している：

> "Agentic commerce will require payment infrastructure that can support increasingly automated and real-time decision making."

Circle Agent Stack（2026 年 5 月 11 日発表）との組み合わせにより、「エージェントが USDC を支払う → CPN でルーティング → Nium で各国ローカル通貨着地」というエンドツーエンドのエージェント決済フローが揃う。将来的に x402 エコシステムが CPN に接続されれば、x402 決済の着地通貨を世界 190 カ国で柔軟に設定できる構造になる。

Kyriba の Trusted Agentic AI（TAI）との統合事例（2026 年 4 月 28 日）では、エンタープライズ財務 TMS 内で USDC を使ったほぼリアルタイムの自律決済が実証されており、「財務 AI エージェントが CPN 経由で社内外送金を自律実行する」モデルが機関レベルで現実化しつつある。

---

## 競合との比較

| 観点 | Circle CPN | Coinbase × Nium |
|---|---|---|
| アプローチ | Circle が直接 PSP をオンボード | Coinbase が Nium という集約者経由で間接展開 |
| ターゲット | 銀行・PSP・フィンテック | 銀行・PSP・企業（Nium クライアント） |
| フルマネージド | あり（CPN Managed Payments） | Nium の API 経由で抽象化 |
| ペイアウトカバレッジ | 190 カ国（Nium 統合後） | 190 カ国（同一 Nium インフラ） |

注：2026 年 4 月 26 日に Coinbase × Nium の統合が発表されたことで、CPN と Coinbase の間に同一の Nium インフラを共有する競合構造が生じている。

---

## 関連ノート

### ローンチ・正式発表

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-08 | [[2026-04-08_Circle_cpn-managed-payments]] | CPN Managed Payments 正式ローンチ、Worldline 等 Tier-1 PSP 参加 |
| 2026-05-27 | [[2026-05-27_Circle-Nium_cpn-usdc-global-payouts]] | Nium がグローバルペイアウトパートナーに参加、190 カ国対応完成 |

### エコシステム拡大

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-26 | [[2026-04-26_Coinbase-Nium_usdc-global-190-countries]] | Coinbase × Nium 統合、CPN との競合構造が明確化 |
| 2026-04-28 | [[2026-04-28_Kyriba-Circle_usdc-enterprise-treasury]] | Kyriba TMS への USDC 統合、エンタープライズ財務 AI 自律決済 |
| 2026-06-11 | [[2026-06-11_MassPay-Coinbase_stablecoin-payouts]] | MassPay が Coinbase 経由で CPN + USDC を使ったグローバルペイアウトを展開 |

---

## 未解決の論点

- CPN Managed Payments の手数料体系が非公開。既存 PSP 手数料との比較ができない
- Nium ペイアウト着地時の USDC → 法定通貨変換は Circle と Nium のどちらが担うか未確認
- GENIUS Act 最終規則（2026-07-18 デッドライン）後の PPSI ライセンス要件と CPN 参加機関への影響
- EU MiCA 下での USDC 取り扱い（Worldline 等欧州 PSP の法的位置づけ）
- CPN の参加要件——スタートアップ・中小 PSP も参加可能か、あるいは大型金融機関向けか

---

## 監視ポイント

- CPN の次のパートナー追加（Airwallex・Rapyd 等の競合ペイアウトプロバイダーとの差別化）
- Circle Agent Stack + CPN + Nium を一気通貫で使う商業事例の公開
- GENIUS Act 最終規則後の Circle の PPSI 申請状況と CPN 対応方針
- Kyriba TAI のような「エージェント自律決済 × CPN」の事例が他 TMS ベンダーにも波及するか
- x402 エコシステムとの接続——x402 決済のセトルメントレイヤーとして CPN が採用される事例

---

## 参考リンク

- [Circle CPN 公式](https://www.circle.com/circle-payments-network)
- [CPN Managed Payments 発表（2026-04-08）](https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement)
- [Circle × Nium 発表（2026-05-27）](https://www.circle.com/pressroom/nium-and-circle-to-connect-usdc-settlement-with-global-payouts)
- [Kyriba × Circle 発表（2026-04-28）](https://www.circle.com/pressroom/kyriba-and-circle-bring-usdc-capabilities-to-enterprise-treasury-unlocking-a-path-toward-more-intelligent-treasury-decisioning)
