---
title: "AllUnity"
type: company
updated: 2026-07-01
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
- **SEKAU（SEK 建て EMT）の正式ローンチ**: スウェーデン・クローナ完全準備担保の 3 本目の MiCA 準拠 EMT。2026 年 5 月発表時の「6 月ローンチ目標」は BaFin 最終承認未取得のまま 2026-06-15 を通過し一旦未達となったが、MiCA 移行期間終了（2026-07-01）直前の 2026-06-19 に BaFin 承認を取得し正式ローンチ。世界初の完全準備担保 MiCAR 準拠 SEK 建て EMT。
- **Agentic Payments インフラの正式公開**: x402 プロトコルを採用したインフラを SEKAU ローンチと同時（2026-06-19）に公開。AI エージェント起点の取引を受け入れ、SEPA 経由でローカル銀行口座に SEK で精算できる。ステーブルコイン保有不要の設計で、欧州 PSP・加盟店の参入障壁を下げる。実際の PSP・加盟店の採用事例は未確認（ローンチ直後）。

### 見立て

AllUnity の戦略は「EU 規制（MiCA）への先行適合」と「ローカル通貨ステーブルコインによる USD 依存脱却」の 2 軸で成立している。MiCA 準拠の EU 規制下で非 USD ステーブルコインを発行し、x402 による Agentic Payments を組み合わせることで、欧州デジタルサービス市場での規制準拠型エージェント決済の最初期参照実装となる可能性がある。

SEKAU は当初 6 月ローンチ目標に対し BaFin 承認遅延で一旦未達となったが（「MiCA EMT 審査プロセスの不確実性」を示す事例）、MiCA 移行期間終了直前の 2026-06-19 に承認を取得し、x402 Agentic Payments インフラと同時に正式ローンチした。「承認取得後に同時ローンチを実現できるか」という当初の論点は解消され、今後は Agentic Payments の実際の採用事例（PSP・加盟店の統合）が欧州 x402 エコシステムへの実質的な貢献度を左右する。

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

- **SEKAU ローンチ後の実運用状況**: 2026-06-19 に BaFin 承認・正式ローンチ済み。対応チェーン（EURAU・CHFAU 実績の Ethereum / Polygon / Arbitrum / Base / Optimism / Solana に対応するか）や流通量を継続監視
- **Agentic Payments の採用事例**: インフラ自体は 2026-06-19 に公開済み。x402 ファシリテーター実装仕様（Coinbase CDP 利用か独自実装か）、SEPA / SEPA Instant 接続の具体設計、実際に統合する EU PSP・加盟店の有無を継続監視
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
