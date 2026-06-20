---
title: "AllUnity"
type: company
updated: 2026-06-15
category: payments
tags:
  - stablecoin
  - stablecoin-issuer
  - MiCA
  - agentic-payments
  - x402
  - Europe
aliases:
  - AllUnity GmbH
  - SEKAU
  - EURAU
  - CHFAU
---

# AllUnity

AllUnity は DWS（ドイツ銀行系資産運用）・Flow Traders・Galaxy Digital の合弁会社として、フランクフルトを拠点に BaFin 規制下で MiCA 準拠ステーブルコインを発行する欧州の規制準拠型ステーブルコイン発行体。ユーロ（EURAU）・スイスフラン（CHFAU）・スウェーデンクローナ（SEKAU）の 3 通貨ラインナップで非 USD ローカル通貨建てステーブルコインを展開し、Coinbase x402 標準を採用した Agentic Payments インフラも並行して準備している。

この vault では、AllUnity を「EU 規制準拠の非 USD ステーブルコインと x402 を組み合わせ、欧州エージェント決済レールの参照実装を目指す企業」として追う。

---

## 現状の要約

### 何をしているか

- **MiCA 準拠ステーブルコイン発行（EMT シリーズ）**: EURAU（EUR、2025-07-31 ローンチ）・CHFAU（CHF、2026-02-26 ローンチ）を BaFin 規制下で稼働中。Ethereum・Polygon・Arbitrum・Base・Optimism・Solana に展開し、Privy（Stripe 傘下）との統合やオフランプ経路も整備。
- **SEKAU（SEK 建て EMT）の準備**: スウェーデン・クローナ完全準備担保の 3 本目の MiCA 準拠 EMT。2026 年 5 月発表時の「6 月ローンチ目標」は BaFin 最終承認未取得のまま 2026-06-15 を通過し、未達。MiCA 移行期間終了（2026-07-01）前後のローンチを継続監視中。
- **Agentic Payments インフラの構築**: x402 プロトコルを採用し、AI エージェント起点の取引を受け入れてローカル銀行口座に現地通貨で精算できる仕組みを準備。ステーブルコイン保有不要の設計で、欧州 PSP・加盟店の参入障壁を下げる。

### 見立て

AllUnity の戦略は「EU 規制（MiCA）への先行適合」と「ローカル通貨ステーブルコインによる USD 依存脱却」の 2 軸で成立している。MiCA 準拠の EU 規制下で非 USD ステーブルコインを発行し、x402 による Agentic Payments を組み合わせることで、欧州デジタルサービス市場での規制準拠型エージェント決済の最初期参照実装となる可能性がある。

ただし、SEKAU の BaFin 承認遅延は「MiCA EMT 審査プロセスの不確実性」を示す事例になった。承認取得後に x402 Agentic Payments との同時ローンチを実現できるかが、欧州 x402 エコシステムへの実質的な貢献度を左右する。SEKAU が仮に大幅に遅れた場合、EURAU を使った先行 Agentic Payments 運用が代替戦略として浮上する。

---

## Inbox との紐付け

### SEKAU 発表・計画（2026-05）

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-20 | [[2026-05-20_AllUnity_sek-stablecoin-agentic-payments-x402]] | SEKAU + x402 Agentic Payments デュアル発表の概要（CoinDesk・The Block） |
| 2026-05-20 | [[2026-05-20_AllUnity_sekau-stablecoin-agentic-payments-x402]] | SEKAU 発表の詳細分析（EURAU・CHFAU 既存展開状況、MiCA EMT 分類、x402 ファシリテーター構成） |
| 2026-05-20 | [[2026-05-20_AllUnity_sekau-stablecoin-agentic-payments]] | SEKAU 発表の加盟店・PSP 視点の示唆（北欧向け通貨変換なし決済、SEPA オフランプ設計） |
| 2026-05-20 | [[2026-05-20_AllUnity_sekau-sek-stablecoin-agentic-payments]] | SEKAU 発表の規制・技術論点（MiCA EMT vs ART 分類、TFR 対応、x402 との接続方式） |

### 進捗・マイルストーン（2026-06）

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-06-15 | [[2026-06-15_AllUnity_sekau-june-target-missed]] | SEKAU 6 月ローンチ目標未達——BaFin 最終承認・公式発表なしのまま 6/15 を通過 |
| 2026-06-19 | [[2026-06-19_AllUnity_sekau-launch-agentic-payments]] | SEKAU 正式ローンチ（BaFin 承認取得）+ x402 Agentic Payments インフラ同時公開——世界初 MiCAR 準拠 SEK EMT |

---

## 監視ポイント

- **SEKAU の BaFin 承認タイミング**: MiCA 移行期間終了（2026-07-01）前後での駆け込みローンチ、または 7/1 後のローンチ実現可否を継続監視
- **Agentic Payments の公式ローンチと採用事例**: x402 ファシリテーター実装仕様（Coinbase CDP 利用か独自実装か）、対応チェーン、SEPA / SEPA Instant 接続の具体設計が明らかになるタイミング
- **EURAU の x402 Agentic Payments 対応**: SEKAU 代替として EURAU での先行運用が発表されるか
- **欧州 PSP・加盟店との提携発表**: Adyen・Worldpay 等の欧州 PSP が AllUnity ステーブルコインを x402 決済通貨として採用するか
- **他のローカル通貨 EMT 拡張**: NOK・DKK・GBP 等のスカンジナビア・欧州通貨への展開計画

---

## 参考リンク

- [AllUnity 公式サイト](https://allunity.com/)
- [AllUnity SEKAU ページ](https://allunity.com/sekau)
- [CoinDesk 発表記事（2026-05-20）](https://www.coindesk.com/business/2026/05/20/germany-s-allunity-plans-swedish-krona-stablecoin-pushes-into-ai-agentic-payments)
- [The Block（2026-05-20）](https://www.theblock.co/post/402027/allunity-plans-swedish-krona-stablecoin-launches-agentic-payments-infrastructure)
- [Finextra（2026-05-20）](https://www.finextra.com/newsarticle/47790/allunity-preps-swedish-krona-backed-stablecoin)
- [PaymentExpert（2026-05-22）](https://paymentexpert.com/2026/05/22/allunity-beyond-euro-stablecoin-krona/)
