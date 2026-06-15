---
title: "B2B越境ステーブルコイン決済"
type: topic
updated: 2026-06-15
tags:
  - stablecoin
  - B2B-payments
  - crossborder
  - remittance
  - psp
---

# B2B越境ステーブルコイン決済

法人間のクロスボーダー決済において、USDC・USDT などのステーブルコインが従来の SWIFT / 銀行振込レールを代替・補完する動きが 2026 年に入り急速に加速している。新興国特化 PSP、送金事業者、欧州規制対応銀行、暗号資産取引所がそれぞれ異なる角度から参入しており、「誰がB2B越境決済インフラのレイヤーを押さえるか」が業界再編の焦点になっている。

---

## 全体像

参入プレイヤーは大きく4つのアプローチに分類できる。

**1. PSP による新興国特化フルスタック統合**
dLocal の「Stablecoin Full」は、ラテンアメリカ・アフリカ・アジア 44 か国以上で収納・ペイアウト・財務管理を単一 API で提供する。既存のローカルフィアットレールとステーブルコインを並列に扱い、FX 換算・照合・レポーティングを一体化したモデル。「ステーブルコイン対応 PSP」から「ステーブルコインをネイティブに持つ PSP」へのシフトを象徴する事例。

**2. B2B 送金プラットフォームによる埋め込み**
Veem は Stripe 傘下の Bridge をインフラに採用し、グローバルプラットフォーム・法人向けにステーブルコイン口座保有・送金機能を API で提供する。同社は Circle CPN ローンチパートナーでもあり、複数インフラを並走させるハイブリッド戦略をとっている。Bridge が PPSI（決済ステーブルコイン発行者）として機能するモデルは MoneyGram の MGUSD（Stellar 上で 2026-06-02 ローンチ）でも採用されており、Bridge の「ステーブルコイン発行プラットフォーム」としての地位が固まりつつある。

**3. 規制済み銀行インフラによる欧州 MiCA 対応**
Banking Circle は 2026 年 4 月に MiCA CASP ライセンスを取得し、USDC・USDG（Paxos）・自社発行 EUR ステーブルコイン EURI の 3 銘柄をカバーするステーブルコイン決済清算サービスをローンチした。EU 域内で「MiCA 準拠＋銀行ライセンス」のダブルライセンスを持ちながら PSP 向けにステーブルコイン清算を提供する最初の事例であり、欧州 PSP が自社開発なしに MiCA 対応を外注できるインフラが整いつつある。

**4. 暗号資産取引所によるインフラ垂直統合**
Kraken 親会社 Payward が 2026 年 5 月、香港拠点の B2B クロスボーダー決済インフラ企業 Reap Technologies を 6 億ドルで買収した。元 Stripe アジア太平洋代表が創業した Reap を取り込むことで、取引所が単なる売買の場からステーブルコイン決済の総合プロバイダーへと転換するトレンドが確立された。

**5. ネットワーク到達性（Reachability）の整備**
Notabene Flow は Travel Rule 準拠の payment link ベースで B2B ステーブルコイン決済を構成し、2026 年 6 月に既存ネットワーク上の数百の regulated institution に対して responder capabilities を network-wide rollout した。新しいレールを作るのではなく、既存の規制済みネットワーク上の「到達性」を上げる戦略であり、B2B ステーブルコイン普及のボトルネックが決済手段の存在よりも受け手側のネットワーク reach にあることを示している。

---

## 主要ノート

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-04-21 | [[2026-04-21_dLocal_stablecoin-full-emerging-markets]] | dLocal が新興国 44 か国で収納・ペイアウト・財務管理を単一 API 提供する「Stablecoin Full」を正式ローンチ |
| 2026-04-22 | [[2026-04-22_Veem-Bridge_stablecoin-accounts-launch]] | Veem が Bridge（Stripe）インフラを採用し、法人向けステーブルコイン口座・送金機能をローンチ発表 |
| 2026-04-22 | [[2026-04-22_MoneyGram-Stellar_usdc-latam-expansion]] | MoneyGram × Stellar の USDC ラテンアメリカ拡大 |
| 2026-04-27 | [[2026-04-27_BankingCircle_mica-stablecoin-settlement]] | Banking Circle が MiCA CASP ライセンス取得後、USDC・USDG・EURI 対応のステーブルコイン決済清算をローンチ |
| 2026-05-07 | [[2026-05-07_Kraken_reap-acquisition-stablecoin-payments-asia]] | Kraken 親会社 Payward が B2B クロスボーダー決済インフラ企業 Reap を 6 億ドルで買収 |
| 2026-06-02 | [[2026-06-02_MoneyGram_mgusd-stellar-launch]] | MoneyGram が Stellar 上で MGUSD ステーブルコインを本番ローンチ（発行体は Bridge） |
| 2026-06-04 | [[2026-06-04_Notabene_flow-responders-b2b-stablecoin-payments]] | Notabene Flow が数百の regulated institution に responder capabilities を rollout し到達性を強化 |

---

## 現状の論点

- **インフラ争奪の構図**：Bridge（Stripe）が PPSI として複数事業者のステーブルコイン発行を引き受けるモデルが台頭している。PSP・送金事業者は Bridge に乗るか、自前インフラを持つかの戦略選択を迫られる。
- **規制対応コストの外注化**：Banking Circle（MiCA CASP）や dLocal（44 か国ライセンスネットワーク）のように、規制対応コストをインフラプロバイダー側で吸収するモデルが増えている。一方で、VASP 規制と PSP 規制の二重適用リスクをどこが負うかは依然として不明確な国が多い。
- **到達性（Reachability）がボトルネック**：Notabene の事例が示すとおり、B2B ステーブルコイン決済の普及は決済手段の存在よりも「相手が既存口座からそのまま払えるか」で決まる。新しいネットワークを作るより既存の規制済みネットワークへの responder 組み込みのほうが普及速度が速い可能性が高い。
- **取引所の垂直統合リスク**：Kraken の Reap 買収に続き、他の大手取引所（Coinbase・OKX 等）による類似の決済インフラ買収が続く可能性がある。取引所がステーブルコイン B2B 決済インフラを押さえることで、従来 PSP の競合環境が激化する。
- **送金事業者の自社ステーブルコイン発行競争**：MoneyGram の MGUSD（Stellar）に続き、Western Union の USDPT（Solana）も 2026 年 5 月にローンチ済み。大手送金事業者が自社ブランドステーブルコインを発行する波が本格化しており、業界標準と相互運用性の確保が次の課題になる。

---

## 監視ポイント

- Bridge（Stripe）が PPSI として引き受けるステーブルコイン発行の件数・規模の拡大状況
- Banking Circle の EURI 発行残高と欧州 PSP による採用状況
- Notabene Flow の responder 数が数百から何千へ伸びるか、recurring / agentic billing 実績の開示
- Kraken × Reap の規制承認（HK・シンガポール）完了後の統合プロダクト内容
- MoneyGram MGUSD のグローバル展開タイムラインと Stellar 以外のチェーンへの展開
- MiCA CASP ライセンス取得事業者の欧州外での規制追従（日本・アジア）

---

## 関連ページ

- [[MOC_Stablecoin_Payments]]
- [[psp-merchant-readiness]]
- [[agent-payment-authorization]]
- [[CLARITY-Act]]
