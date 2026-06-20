---
title: "AllUnity、SEKAU（SEK ステーブルコイン）と x402 Agentic Payments を正式ローンチ（2026-06-19）"
date: 2026-06-19
source: "AllUnity 公式プレスリリース、CoinMarketCap、The Block、Incrypted"
source_url: "https://allunity.com/news/allunity-launches-the-first-fully-reserved-swedish-krona-backed-stablecoin-sekau"
entity: "AllUnity"
category: stablecoin-payments / agentic-commerce
primary_category: stablecoin-payments
article_published_date: 2026-06-19
underlying_event_date: 2026-06-19
primary_source_date: 2026-06-19
tags:
  - AllUnity
  - SEKAU
  - x402
  - agentic-commerce
  - MiCA
summary: "AllUnity（DWS × Flow Traders × Galaxy Digital 合弁、フランクフルト・BaFin 規制）が 2026-06-19 に SEKAU（SEK 完全準備担保の MiCAR 準拠 EMT）を正式ローンチ。同時に x402 プロトコルを採用した Agentic Payments インフラも公開——AI エージェント起点の取引を受け入れ、ローカル銀行口座に SEK で精算できる。6/15 時点で「6月ローンチ目標未達」と判断していたが（[[2026-06-15_AllUnity_sekau-june-target-missed]]）、BaFin 最終承認取得後に 6/19 に公式ローンチが実現した。世界初の完全準備担保 MiCAR 準拠スウェーデンクローナ建てステーブルコイン。"
implications: "EU 内 non-USD・non-EUR 圏での x402 エージェント決済が初めて本番稼働。北欧（スウェーデン等）向けのエージェント決済設計で USDC 以外の選択肢が加わった。ステーブルコイン保有不要の「x402 受け入れ → SEK 銀行精算」設計は EU 加盟店の参入障壁を大幅に下げる可能性がある。"
importance: High
confidence: High
follow_up: "SEKAU の Agentic Payments 採用事例（どの EU 加盟店・PSP が接続するか）、EURAU・CHFAU での Agentic Payments 有効化の有無、NOK・DKK 等の他ローカル通貨 EMT への拡張計画"
---

## 概要

- AllUnity が 2026-06-19 に SEKAU（SEK 完全準備担保 MiCAR 準拠 EMT）を正式ローンチした
- 同時に「Agentic Payments」インフラを公開——x402 プロトコルで AI エージェント起点の支払いを受け付け、SEPA 経由でローカル銀行口座に SEK 建てで精算する設計
- 世界初の完全準備担保 MiCAR 準拠 SEK 建て EMT
- 2026-06-15 時点では BaFin 最終承認未取得のまま 6 月ローンチ目標が「未達」と記録していたが（[[2026-06-15_AllUnity_sekau-june-target-missed]]）、その後 BaFin 承認を取得し 6/19 に正式ローンチが実現した

## 何が起きたか

- **SEKAU 正式ローンチ（2026-06-19）**：AllUnity が BaFin 承認のもと SEKAU を正式に流通開始。1:1 SEK 準備担保、24/7 即時決済、クロスボーダー決済・プログラマブルファイナンスアプリ対応
- **Agentic Payments インフラ同時公開**：AI エージェントが x402 標準で取引を開始し、企業（加盟店・PSP）が銀行口座に SEK 建てで受け取れるシステム。加盟店はステーブルコインを直接保有する必要なし
- **MiCA 移行期間内でのローンチ達成**：MiCA 全面施行（7/1）の 12 日前に BaFin 承認を取得。MiCA 移行期間内に認可された EMT として既存枠組みで流通可能

## 確認された事実

- AllUnity 公式プレスリリースで 2026-06-19 付け正式ローンチ発表を確認
- SEKAU：SEK 完全準備担保、AllUnity GmbH が BaFin 規制下で発行、MiCA EMT 分類
- Agentic Payments：Coinbase x402 標準採用、AI エージェント起点取引に対応、SEPA / SEPA Instant オフランプ
- 既存 EMT シリーズ：EURAU（EUR、2025-07-31）・CHFAU（CHF、2026-02-26）に続く第 3 弾
- AllUnity の株主構成：DWS（ドイツ銀行系資産運用）・Flow Traders・Galaxy Digital（三社合弁）

## なぜ重要か

### 決済事業者視点

- **EU 内 x402 エージェント決済が非 USD 圏でも本番稼働**：これまで EU 内の x402 決済は事実上 USDC（Base / Arbitrum / Solana）に限定されていた。SEKAU × Agentic Payments により、SEK 建ての x402 決済レールが初めて稼働した
- **ステーブルコイン保有不要の受け入れ設計**：加盟店は x402 経由で AI エージェントから支払いを受け取り、SEPA 経由で自行口座に SEK で精算できる。暗号資産カストディなしに x402 加盟店になれる
- MiCA 移行期間内（7/1 前）のローンチにより、AllUnity は「MiCA 準拠済み EMT」として EU 全域で流通できる法的根拠を確保した

### 加盟店視点

- 北欧（スウェーデン等）向けエージェント決済の設計選択肢が増加——USDC 一択から USDC + SEKAU の 2 択に
- 通貨換算コストを排除した SEK ネイティブの受け取りが可能
- ただし Agentic Payments の採用事例（実際にどの PSP・加盟店が統合を進めているか）は未確認。初期はデモ段階の可能性

### プロダクト視点

- EU × x402 の参照実装が登場した。「x402 対応だがステーブルコイン保有なし」の加盟店フローが具体的な実装として示された
- SEKAU が利用できるチェーン（EURAU・CHFAU は Ethereum・Polygon・Arbitrum・Base・Optimism・Solana に展開済み）の正式確認が必要
- Agentic Payments の x402 ファシリテーター実装が Coinbase CDP 利用か AllUnity 独自実装かは未確認——Coinbase CDP 依存ならばフォールバック設計の重要性が高まる

### 規制 / リスク視点

- MiCA 移行期間内（7/1 前）のローンチにより、SEKAU は MiCA「完全移行後」の一段厳格な審査を回避した可能性がある
- BaFin 審査プロセスが AllUnity 内部で 5/20 発表から約 30 日で完結したことは、MiCA EMT 申請期間の参照事例になる（ただし申請自体は 5/20 以前から進行していた可能性が高い）
- **EU 内 non-EUR ステーブルコインの先例**：SEKAU の成功は NOK・DKK・GBP 等の他ローカル通貨 EMT 発行者にとって MiCA 審査実現可能性の「陽性事例」となる

## 我々への示唆

- いま検討すべきこと:
  - SEKAU / Agentic Payments の対応チェーン・ファシリテーター仕様を確認し、既存の x402 実装との互換性を評価する
  - EU（特に北欧）向けエージェント決済設計で USDC 代替候補として SEKAU を評価する（特にスウェーデン法人顧客向け）
- 後で深掘りすべきこと:
  - AllUnity Agentic Payments の x402 ファシリテーター実装詳細（Coinbase CDP vs 独自実装、対応チェーン、SEPA Instant 接続タイミング）
  - 初期の Agentic Payments 加盟店事例・PSP 統合パートナーの公開
  - EURAU・CHFAU での Agentic Payments 対応（SEKAU 先行か、後から全通貨対応になるか）
- 今は優先度が低いこと:
  - SEKAU の発行量・市場流通量——ローンチ直後のため数週間後に確認

## ありそうな示唆

- AllUnity の「ステーブルコイン保有不要の x402 受け入れ」設計は、Adyen Agentic（6/16 ローンチ、TradFi 保証型）と対照的な「オープンプロトコル + 銀行精算」の EU 実装例として位置づけられる。欧州の決済事業者が x402 に参入するためのコスト・法規制ハードルを大幅に下げる可能性がある
- MiCA 移行期間内（7/1 前）のローンチは、BaFin が「MiCA 準拠済み EMT」の先行認定を急いだ証左とも読める。MiCA 7/1 後は SEKAU が EU 全域の既認可 EMT として扱われる一方、後発の GBP/NOK/DKK EMT は「MiCA 完全施行後」の審査基準に直面する

## 推測 / 監視ポイント

- **EURAU・CHFAU での Agentic Payments 有効化**：SEKAU と同時に他 2 通貨での有効化が発表されなかった場合、SEKAU 先行の理由（技術的・規制的）が重要
- **Adyen との接続**：Adyen Agentic（6/16 ローンチ）が AllUnity SEKAU を決済通貨として対応するか——両社ともに EU エージェント決済を狙っており、統合の可能性が高い
- **NOK・DKK 等の拡張**：AllUnity が SEKAU に続き北欧他通貨の EMT を計画しているかは今後の発表待ち
- BaFin が 7/1 前後で SEK EMT 審査を完了した具体的な審査期間（申請から承認まで）が情報開示されれば、他発行者の参照値になる

## 未解決の論点

- SEKAU の対応チェーン（EURAU・CHFAU 実績の Ethereum / Polygon / Arbitrum / Base / Optimism / Solana に対応するか、追加チェーンがあるか）
- Agentic Payments の x402 ファシリテーター構成（Coinbase CDP か独自実装か）
- SEPA Instant オフランプの接続状況（SEPA 通常 vs SEPA Instant で精算スピードが異なる）
- MiCA 7/1 施行後の SEKAU 流通への影響（移行期間内認可によりスムーズに移行できる見通しだが、ESMA ガイドラインとの整合性確認が必要）

## 参考リンク

- 一次情報: [AllUnity プレスリリース（2026-06-19）](https://allunity.com/news/allunity-launches-the-first-fully-reserved-swedish-krona-backed-stablecoin-sekau)
- 補足情報: [CoinMarketCap（2026-06）](https://coinmarketcap.com/academy/article/allunity-swedish-krona-stablecoin)
- 補足情報: [Incrypted（2026-06）](https://incrypted.com/en/allunity-announces-swedish-krona-stablecoin-and-ai-agent-payment-infrastructure-launch/)
- 前提ノート: [[2026-06-15_AllUnity_sekau-june-target-missed]]（6/15 時点の未達記録）
- 前提ノート: [[2026-05-20_AllUnity_sekau-stablecoin-agentic-payments-x402]]（5/20 発表時の詳細）

## 重要度

- High

## 確からしさ

- High（AllUnity 公式プレスリリース + 複数メディアの 6/19 報道で確認）
