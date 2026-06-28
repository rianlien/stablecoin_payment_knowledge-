---
title: "Binance、EU ユーザーに 7 月 1 日からのサービス停止を正式通知（2026-06-26）"
date: 2026-06-28
source: "CoinDesk / CryptoTimes / Euronews / DailyCoin"
source_url: "https://www.coindesk.com/policy/2026/06/26/binance-tells-eu-users-it-will-no-longer-provide-services-after-failing-to-secure-mica-license"
entity: "Binance"
category: "regulation / MiCA"
primary_category: "regulation"
article_published_date: 2026-06-26
underlying_event_date: 2026-06-26
primary_source_date: 2026-06-26
tags:
  - stablecoin
  - regulation
  - payments
  - MiCA
  - compliance
summary: "Binance が 2026-06-26 に EU ユーザーへメールで正式通知——7 月 1 日から新規注文・入金・サインアップ・ステーキング等の主要サービスを停止。ユーザー資産は安全でアクセス可能と明記し、7/1 までの引き出しは求めていない。次の申請先としてフランスを示唆。ギリシャ HCMC 申請撤回（6/24）の実運用上の確定版として位置づけられる。"
implications: "MiCA 7/1 施行と同時に、世界最大の暗号資産取引所が EU 市場から実質撤退。EU 内の USDC/EURC 流動性が MiCA 認可 4 社（Coinbase EU・Kraken・OKX・Crypto.com）に本格集中する。EU 向けオンランプ/オフランプの Binance 依存を持つ決済フローは代替経路への移行が不可避。"
importance: High
confidence: High
follow_up: "① 7/1 施行後の EU USDC スプレッド拡大の実態（Binance ボリューム脱落分の吸収先）② Binance のフランス AMF 申請タイムライン（AMF 審査は数ヶ月かかる見通し）③ EU ユーザーが Binance から他の MiCA 認可 CASP に資産を移送する実際の期間と規模"
---

## 概要

2026 年 6 月 26 日、Binance は EU 域内ユーザーに対してメールで正式通知を送り、MiCA ライセンスを 2026 年 6 月 30 日までに取得できないことを確認した上で、7 月 1 日からの主要サービス停止を宣言した。2026-06-24 のギリシャ HCMC への MiCA 申請撤回（[[2026-06-24_Binance_mica-greece-withdrawal-eu-limbo]] 参照）を受け、サービス停止の具体的内容・ユーザー資産の取り扱い・次の申請計画を初めて明示したものであり、Binance EU 退場の実運用上の最終確認となる。

## 何が起きたか

- **通知日**: 2026-06-26（EU ユーザーへのメール送付）
- **停止開始日**: 2026-07-01（MiCA 全面施行と同日）
- **停止されるサービス**: 新規注文・入金・新規ユーザー登録（サインアップ）・ステーキング商品
- **ユーザー資産の扱い**: 安全で引き続きアクセス可能と明記。「7/1 までに引き出せ」とは言っていない
- **影響国**: ポーランド・イタリア・スペイン・フランス等、旧国内登録（VASP 登録等）が MiCA 施行で無効となるすべての EU 加盟国
- **Binance のコメント**: "will not be granted a MiCA license by 30 June 2026"（Binance は EU には残ると表明し、フランスでの次の申請を示唆）
- **次のステップ**: フランス AMF への DASP 登録から MiCA CASP 申請への転換ルートを検討中（ただしフランス当局はパスポーティングに懸念を示しており、審査期間は数ヶ月以上）

## 確認された事実

- 6/24 のギリシャ申請撤回後、6/26 に EU ユーザー向けメール通知（CoinDesk・CryptoTimes・DailyCoin で複数確認）
- "Binance is not telling users to withdraw their funds by July 1" と明記——パニック引き出しを防ぐ意図
- 停止される主要サービス：新規注文・入金・サインアップ・ステーキング（継続できるサービスの詳細は未公開）
- Euronews（2026-06-25）および CoinDesk（2026-06-26）による一次報道を複数二次メディアが確認

## なぜ重要か

### 決済事業者視点

- Binance は EU 域内最大規模の USDC/EURC 取引量を持つプラットフォームだった。7/1 以降のサービス停止で EU 内の USDC 調達・変換（オンランプ/オフランプ）が制約される
- MiCA 認可 4 社（Coinbase EU・Kraken・OKX・Crypto.com）への流動性集中は当面スプレッドを拡大させる可能性。Circle が EU 向け流動性プロバイダー追加に動く動機が高まる

### 加盟店視点

- EU 加盟店が Binance 経由で USDC を調達していた場合、7/1 以降は Coinbase EU または Kraken に切り替えが必要
- EU ドメインの PSP・FinTech が Binance API を使って stablecoin 決済バックエンドを構築している場合は即時の代替対応が必要

### プロダクト視点

- EU 向け x402 / AP4M のオンランプ経路に Binance を組み込んでいる設計は 7/1 以降機能不全になる。Coinbase Developer Platform（CDP）は MiCA 認可 Coinbase EU と接続しており、代替として最もクリーンな経路

### 規制 / リスク視点

- MiCA 7/1 全面施行の「実質的な初日」効果がここで確認された：世界最大の取引所が EU から実質撤退する形で MiCA の執行力が明示された
- フランスでの次の申請は、フランス AMF が MiCA CASP のパスポーティングに懸念を示しているため、承認まで数ヶ月以上かかる見通し。Binance が EU に戻るまでの空白期間は少なくとも 2026 年内続く

## 我々への示唆

- いま検討すべきこと:
  - EU 向け決済フロー・API バックエンドで Binance を利用しているすべての箇所を 7/1 00:00 CET（EU 現地時間）前に Coinbase EU・Kraken・OKX のいずれかに切り替える
  - EU ユーザー向け USDC オフランプの新規プロバイダー契約（KYC・API 接続・手数料確認）を 6/30 中に完了
- 後で深掘りすべきこと:
  - 7/1 以降の EU USDC スプレッドの実態観察（1 週間後に確認）
  - Binance フランス AMF 申請の進捗（承認タイムライン・条件）
  - Binance の EU ユーザー資産移転の規模（MiCA 認可取引所への資金流入データ）
- 今は優先度が低いこと:
  - Binance が EU に「戻る」シナリオの準備（フランス認可は 2026 年内は難しい見通し）

## ありそうな示唆

- Coinbase EU が最大の受益者になる構造は固まった。Coinbase Developer Platform（CDP）との接続が整っている事業者はそのまま使えるが、Kraken や OKX は API 仕様が異なるため移行コストがかかる
- EU のユーザーがポーランドや東欧の取引所（Bitfalls 等）に分散移動する可能性もあるが、MiCA 認可なしには規制リスクあり

## 推測 / 監視ポイント

- EU USDC スプレッドが 7/1 以降どの程度拡大するか（予測：短期的に 5〜15bp 拡大）
- Binance がフランス AMF 申請を正式発表する時期（Q3 2026？）
- Binance のユーザー向け「継続できるサービス」の詳細（ウォレット保管・閲覧のみ継続か）

## 未解決の論点

- 7/1 以降、既存 Binance EU ユーザーのポジション（保有 stablecoin）の扱い：引き出しのみ可能か、一定期間の清算猶予はあるか
- EU 各加盟国の金融規制当局（HCMC・BaFin・AMF 等）が Binance のサービス停止後に独自の強制措置を取るか

## 参考リンク

- 一次情報: [CoinDesk（2026-06-26）](https://www.coindesk.com/policy/2026/06/26/binance-tells-eu-users-it-will-no-longer-provide-services-after-failing-to-secure-mica-license)
- 補足情報: [CryptoTimes（2026-06-26）](https://www.cryptotimes.io/2026/06/26/binance-to-halt-eu-services-from-july-1-after-failing-to-secure-mica-license/) / [Euronews（2026-06-25）](https://www.euronews.com/business/2026/06/25/binance-to-halt-crypto-services-across-eu-countries-after-failing-to-secure-mica-approval) / [DailyCoin（2026-06-26）](https://dailycoin.com/binance-suspends-eu-services-after-mica-license-failure)

## 関連ノート

- [[2026-06-24_Binance_mica-greece-withdrawal-eu-limbo]]（前段：ギリシャ申請撤回——6/26 Brief 採録済み）
- [[2026-06-11_MiCA_july1-deadline-14-exchanges-eu]]（MiCA 14 社認可・USDT 排除の構造——6/11 Brief 採録済み）
- [[2026-06-16_Binance_mica-eu-exit-risk]]（HCMC 拒否報道——6/21 Brief 採録済み）

## 重要度

- High

## 確からしさ

- High（Binance の公式通知、複数メディアで確認）
