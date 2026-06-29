---
title: "MiCA CASP 移行期間終了（7/1）：EU 認可取引所はわずか約 230 社——未認可 80%+ が「ワイプアウト」、1,000 万人ユーザーが移行を迫られる"
date: 2026-06-29
source: "CoinDesk / Bitcoin Magazine / Finance Magnates"
source_url: "https://www.coindesk.com/policy/2026/06/29/europe-s-unlicensed-crypto-firms-face-wipeout-as-final-regulatory-deadline-falls"
entity: "ESMA / EU"
category: regulation
primary_category: regulation
article_published_date: 2026-06-29
underlying_event_date: 2026-07-01
primary_source_date: 2026-06-29
tags:
  - regulation
  - stablecoin
  - payments
  - psp
summary: "MiCA 移行期間の最終期日 2026-07-01 を 2 日後に控えた 2026-06-29 時点で、EU 全体での MiCA CASP 認可取得済み事業者は約 230 社のみ。EU 内に存在した約 3,000 以上の移行期免除 VASP のうち 80% 以上が認可未取得のまま EU サービスを停止する「ワイプアウト」状態に至った。ESMA は 4/17 声明で延長なしを明言しており、フランス・オランダは積極的な法執行を予告。欧州内で 1,000 万人超のユーザーが代替プラットフォームへの移行を余儀なくされる可能性がある。"
implications: "EU 内の暗号資産サービス提供が事実上 MiCA 認可 CASP 約 230 社による寡占体制に移行する。流動性・手数料・ユーザー接続性の再編が 7/1 以降に加速。Circle（MiCA EMT 認可済み）・Coinbase EU・Kraken EU・OKX EU の 4 社が EU ユーザー獲得競争の主軸となる。"
importance: High
confidence: High
follow_up: "7/1 以降の EU USDC スプレッド実測値、Coinbase EU・Kraken EU・OKX EU への流動性集中度、フランス AMF・オランダ AFM の法執行事例第 1 号、ESMA の MiCA 未認可事業者リスト公開"
---

## 概要

EU の Markets in Crypto-Assets 規制（MiCA）が移行期間を終了し、2026-07-01（明日）から全面施行される。2024 年時点で EU 各国に 3,000 以上存在した移行期免除 VASP（仮想資産サービス事業者）のうち、正規の MiCA CASP（Crypto-Asset Service Provider）認可を取得したのは約 230 社のみ。残る 80% 超が EU ユーザーへのサービス提供を停止しなければならず、1,000 万人以上のユーザーが代替プラットフォームへの移行を迫られている。

## 何が起きたか

- **2026-06-29**：CoinDesk が「Europe's unlicensed crypto firms face 'wipeout'」「Millions of EU users searching for new platform」の 2 本の報道記事を公表
- EU 全体の MiCA CASP 認可数：**約 230 社**（2026 年 6 月末時点）
- 移行前の EU VASP 登録数：**3,000 以上**（ポーランドだけで 1,400 超）
- 未認可比率：**80〜83%** が認可未取得のまま 7/1 を迎える見通し
- ESMA は **2026-04-17** の声明で「7/1 以降の延長は一切なし」「認可なき EU ユーザー向けサービスは EU 法違反」と明言
- フランス（AMF）とオランダ（AFM）がいち早く **積極的法執行** を予告
- 認可取得済みの主要 CASP（抜粋）：Coinbase EU、Kraken EU、OKX EU、Crypto.com EU（各 MiCA CASP 認可）
- Binance：ギリシャ申請撤回（6/24）→ EU ユーザーへのサービス停止通知（6/26）、7/1 から新規注文・入金・サインアップ・ステーキング停止

## 確認された事実

- OKX Europe CEO Erald Ghoos が「EU の約 3,000 社の移行期 VASP のうち 80% は（7/1 以降）継続しない」と発言（CoinDesk 取材）
- Swissborg 最高提携責任者 Alex Fazel が「1,000 万人以上がプラットフォームを乗り換えることになる」と発言
- ポーランドの移行期登録数が突出して多い（1,400+）——MiCA 前の登録規制が緩かった結果であり、多くが事実上ペーパーカンパニー的登録の可能性
- 欧州委員会・ESMA は延長を認めない立場を堅持（ESMA 2026-04-17 声明）
- ESMA は未認可事業者に対し「カスタマーへの明確なコミュニケーション・資産の安全な引き出し保証・最終クローズ期日の明示」を義務づけ
- MiCA CASP 認可取得の「壁」：EU 拠点設立、適格資本・流動性要件、ESMA 準拠の KYC/AML、技術審査——小規模事業者には事実上参入障壁

## なぜ重要か

### 決済事業者視点

- EU 向けステーブルコイン決済フロー（特に USDC・EURC）のオンランプ・オフランプが **Coinbase EU / Kraken EU / OKX EU** の 3 強体制に集約される
- EU 内 USDC の流動性が Binance（最大手の一つ）喪失により短期的にスプレッド拡大（5〜20bp 程度のリスク）
- EU 向けサービスで Binance API を使っていた PSP・アグリゲーターは **6/30 中に代替 CASP に切り替え完了** しなければ 7/1 から機能停止

### 加盟店視点

- EU 域内の法人が暗号資産・ステーブルコインを受け取る際の法的な交換窓口が一気に絞られる
- MiCA CASP を通じない P2P または未認可ウォレット経由での受け取りは、法的グレーゾーン化する可能性

### プロダクト視点

- x402 / AP4M 実装において「EU ユーザー向けのオンランプ」は MiCA 認可 CASP 経由のみが法的に安全な経路となる
- EU 拠点の AI エージェントが stablecoin 決済を行う場合、接続先 CASP の MiCA 認可確認が要件化される

### 規制 / リスク視点

- 7/1 以降、EU 向けサービスを継続する未認可事業者は EU 法違反となり、年間売上高の **12.5%** を上限とする罰金リスクを負う
- フランス・オランダが法執行を予告しており、7/1 直後に第 1 号の執行事例が出る可能性がある——これが業界全体の警戒水準を決める
- EU 内の USDC 流動性が寡占体制に移行することで、Coinbase が EU 内 stablecoin インフラを事実上コントロールするリスクが生まれる（規制リスクの集中）

## 我々への示唆

- いま検討すべきこと:
  - **【本日中】EU 向け暗号資産サービス（x402 オンランプ・ステーブルコイン受け取り）での Binance API 依存を全て Coinbase EU / Kraken EU に切り替え完了**
  - EU 向けサービスのオンランプ・オフランプで利用している CASP の MiCA 認可ステータスをリスト化し、7/1 施行後も継続可能であることを確認
- 後で深掘りすべきこと:
  - 7/1 以降の EU USDC スプレッド実測値——寡占体制によるスプレッド上昇が持続的であれば代替策（EUR ステーブルコイン等）の評価が必要
  - Binance の次の EU 認可申請先（フランス AMF）の進捗——仮に数ヶ月以内に認可取得すれば流動性は回復する
  - ポーランド・東欧の未認可 VASP 廃業の実態と、それらのユーザーが移行する先の把握（スプレッド・流動性への影響の深刻度評価）
- 今は優先度が低いこと:
  - EU 内のマイナー CASP（230 社中の小規模事業者）の詳細リスト収集

## ありそうな示唆

- Coinbase EU と Kraken EU が EU 最大の stablecoin 流動性プロバイダーとなることで、CDP（Coinbase Developer Platform）への EU 向けプロジェクトの統合圧力が高まる
- OKX EU は EU 内の USDC 市場よりもアジア系ユーザー獲得に注力する可能性があり、純粋な EU 内流動性はほぼ Coinbase EU・Kraken の 2 強になるかもしれない

## 推測 / 監視ポイント

- 7/1〜7/7 の EU USDC 出来高分布（Coinbase EU・Kraken・OKX の比率変化）
- フランス AMF・オランダ AFM の第 1 号法執行事例の公表タイミングと対象事業者
- Binance の AMF 申請進捗——フランス規制当局のスタンス（CASP 審査に要する期間は平均 6〜12 ヶ月）

## 未解決の論点

- MiCA CASP 約 230 社の内訳（国別・サービス種別）——Circle・Coinbase の EMT 認可と CASP 認可の関係整理
- 未認可事業者が 7/1 以降も「非 EU 法人」として EU ユーザーにサービスを提供し続けるケースへの ESMA の対処方針
- 日本・アジアの規制当局が EU MiCA 施行後の域外ステーブルコイン流入をどう評価するか

## 参考リンク

- 一次情報:
  - [ESMA MiCA 規制ページ（ESMA 公式）](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)
- 補足情報:
  - [CoinDesk「Europe's unlicensed crypto firms face 'wipeout'」（2026-06-29）](https://www.coindesk.com/policy/2026/06/29/europe-s-unlicensed-crypto-firms-face-wipeout-as-final-regulatory-deadline-falls)
  - [CoinDesk「10 million EU users searching for new platform」（2026-06-29）](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu)
  - [Bitcoin Magazine（2026-06-29）](https://bitcoinmagazine.com/news/european-esma-unlicensed-crypto)
  - [Finance Magnates（2026-06-29）](https://www.financemagnates.com/cryptocurrency/regulation/europes-crypto-market-after-july-1-who-stays-who-leaves-and-what-changes-under-mica/)

## 重要度

- High

## 確からしさ

- High
