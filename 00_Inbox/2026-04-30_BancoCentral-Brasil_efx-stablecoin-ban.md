---
title: "ブラジル中央銀行、eFX クロスボーダー決済でのステーブルコイン・暗号資産決済を禁止（決議 561 号）"
date: 2026-04-30
source: CoinDesk / The Block / BanklessTimes
source_url: https://www.coindesk.com/policy/2026/05/02/brazil-s-central-bank-bans-stablecoin-and-crypto-settlement-in-cross-border-payments
entity: Banco Central do Brasil
category: 規制
tags:
  - regulation
  - stablecoin
  - payments
summary: "ブラジル中央銀行（BCB）は 2026 年 4 月 30 日、規制対象の電子外国為替（eFX）システムにおけるステーブルコインおよびビットコイン等の暗号資産による決済を禁止する決議 561 号を公布した。施行は 2026 年 10 月 1 日。Wise・Nomad・Braza Bank など eFX バックエンドにステーブルコイン決済レールを利用していた企業が影響を受ける。個人によるステーブルコインの売買・保有は引き続き可能。"
implications: "ブラジルは月間 60〜80 億ドルの仮想資産移転の約 90% をステーブルコインが占める市場であり、ラテンアメリカ最大の規制逆風。ステーブルコインを用いた eFX バックエンドの代替モデルが必要になる一方、BCB 認可済み事業者経由の正規チャネルへの移行が進む見通し。"
follow_up: "10 月 1 日施行後の実態変化、Wise・Nomad 等の代替決済レール対応状況、BCB が認可拒否した場合の市場への影響"
---

## 概要

ブラジル中央銀行（Banco Central do Brasil, BCB）は 2026 年 4 月 30 日に決議第 561 号を公布し、国内規制対象の電子外国為替（eFX）プロバイダーが海外送金の決済手段としてステーブルコイン・ビットコイン等の暗号資産を使用することを禁止した。施行は 2026 年 10 月 1 日で、既存の無認可事業者は 2027 年 5 月 31 日までに BCB の認可申請を行う義務が課される。

## 何が起きたか

**決議 561 号の主要内容**
- eFX プロバイダーと海外カウンターパーティ間の決済は、外国為替取引または非居住者のブラジルレアル建て口座（non-resident BRL account）を通じた手段のみに限定
- ステーブルコイン・ビットコイン等の暗号資産を eFX バックエンドの決済手段として使用することを禁止
- 新規追加として、国内外の金融・資本市場投資に関連する送金も eFX で取り扱い可能に（上限 1 万ドル/取引）
- 送金上限は非 EC プラットフォーム連携のデジタル決済ソリューションでも 1 万ドル/取引

**現状の市場規模と影響**
- ブラジルの暗号資産移転額は月間 60〜80 億ドルで推移しており、そのうち約 90% をステーブルコインが占める（BCB 内部データ）
- BCB が懸念するのは ステーブルコイン送金による租税回避・マネーロンダリング監視の困難化
- 直接影響を受ける主要企業：Wise、Nomad、Braza Bank など eFX バックエンドにステーブルコイン決済を組み込んでいたフィンテック
- 個人投資家によるステーブルコインの購入・保有・移転は引き続き合法

**施行・移行スケジュール**
- 2026 年 10 月 1 日：新規ルール施行
- 2027 年 5 月 31 日：無認可 eFX 事業者の BCB 認可申請期限

## なぜ重要か

### 決済事業者視点
- ラテンアメリカ最大市場のブラジルで eFX スタックにステーブルコインを組み込んでいた PSP・フィンテックは、10 月 1 日までに代替決済レールを用意する必要がある
- BCB 認可を取得している正規ルート（大手銀行の SWIFT/SPEI ルートや認可済みの外国為替ブローカー）への回帰を迫られる
- MoneyGram × Stellar（USDC LatAm 拡大）や dLocal のステーブルコイン拡大に逆風。ただし eFX という特定の規制カテゴリに限定される点に注意

### 加盟店視点
- ブラジル向けの海外送金・クロスボーダー決済を USDT/USDC で提供していた加盟店プラットフォームは受け入れ経路の再設計が必要
- B2B 決済における「ステーブルコインで送って現地通貨で受け取る」モデルの制約が増す

### プロダクト視点
- ブラジル向けオフランプでステーブルコインを活用している場合、代替手段（BCB 認可 eFX プロバイダーとの連携、または P2P 非規制チャネルへの移行）を評価する必要がある
- ブロックチェーン側の取引は禁止対象外のため、L1/L2 上の送金プロトコル自体は影響なし。問題はラストマイルのフィアット着金

### 規制 / リスク視点
- 今後、アルゼンチン・コロンビア・チリ等の LatAm 諸国でも類似の規制議論が広がる可能性がある（ブラジルが先例となる）
- IMF・BIS の「ステーブルコインは国内通貨の代替手段として監視強化が必要」という立場と整合する規制強化の流れ
- ブラジル政府は「クリプト規制の先進国」を目指す方針を取ってきた（2023 年仮想資産法施行）が、今回の措置はそのバランス調整

## 我々への示唆

- いま検討すべきこと:
  - ブラジルへのクロスボーダー送金・決済フローにステーブルコイン eFX バックエンドを使用しているか確認し、10 月 1 日施行前に代替案を用意
  - BCB 認可済み eFX プロバイダーとの連携可否をパートナーシップチームに確認
- 後で深掘りすべきこと:
  - 決議 561 号の「non-resident BRL account」経由ルートの実務的なコスト・スピード比較
  - Wise・Nomad の対応方針が公表されたら、業界の標準的な代替モデルとして参照
- 今は優先度が低いこと:
  - ブラジルの個人向けステーブルコイン利用（保有・取引）は禁止されていないため、コンシューマー向けウォレット機能への影響は限定的

## 未解決の論点

- eFX の定義に入らない P2P ステーブルコイン送金（直接ウォレット間移転）は今回の禁止対象外だが、BCB が今後これも規制対象に加えるかどうか
- Wise 等が eFX ライセンスではなく別の認可類型で送金サービスを継続できるかどうか
- ブラジルにおけるリアル建て CBDC（Drex）との関係性：Drex の普及を促進するための eFX チャネル閉鎖という政策意図の有無

## 参考リンク

- 一次情報: [CoinDesk — Brazil's central bank bans stablecoin and crypto settlement in cross-border payments (2026-05-02)](https://www.coindesk.com/policy/2026/05/02/brazil-s-central-bank-bans-stablecoin-and-crypto-settlement-in-cross-border-payments)
- 一次情報: [The Block — Brazil central bank prohibits crypto use in regulated cross-border payments (2026-05-02)](https://www.theblock.co/post/399713/brazil-central-bank-prohibits-crypto-use-in-regulated-cross-border-payments-under-new-fx-rules)
- 補足情報: [BanklessTimes — Brazil's Central Bank Bars Crypto from Regulated eFX Cross-Border Transfers (2026-05-01)](https://www.banklesstimes.com/articles/2026/05/01/brazils-central-bank-bars-crypto-from-regulated-efx-cross-border-transfers/)
- 関連ノート: [MoneyGram × Stellar USDC LatAm 拡大（2026-04-22）](./2026-04-22_MoneyGram-Stellar_usdc-latam-expansion.md)
- 関連ノート: [dLocal ステーブルコイン全新興国展開（2026-04-21）](./2026-04-21_dLocal_stablecoin-full-emerging-markets.md)

## 重要度

- High

## 確からしさ

- High（CoinDesk・The Block による一次報道、BCB 公式決議 561 号に基づく）
