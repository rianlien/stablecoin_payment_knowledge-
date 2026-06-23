---
title: "Opera MiniPay、Visa デビットカードをローンチ——Gnosis Pay 経由でステーブルコイン残高を 175M 加盟店で利用可能に"
date: 2026-06-23
source: PR Newswire（Opera）/ CoinTelegraph / CryptoNews
source_url: https://www.stocktitan.net/news/OPRA/mini-pay-launches-visa-debit-card-to-connect-stablecoin-users-in-qtonsflxih8z.html
entity: Opera（MiniPay）/ Visa / Gnosis Pay
category: merchant-PSP-readiness / stablecoin-payments
primary_category: merchant-PSP-readiness
article_published_date: 2026-06-23
underlying_event_date: 2026-06-23
primary_source_date: 2026-06-23
tags:
  - stablecoin
  - merchant-readiness
  - card-rails
  - consumer-payments
  - gnosis-pay
summary: "Opera の MiniPay（Celo 上のセルフカストディアル・ステーブルコインウォレット、16M+ ウォレット・65 カ国以上）が Gnosis Pay をテクニカルイネーブラーとして Visa デビットカードをローンチ。欧州・アフリカ・東南アジア・中南米の対象市場でステーブルコイン残高を 175M 以上の Visa 加盟店・Apple Pay/Google Pay 経由で使用可能に。月額・年会費なし。USDC・USDT・Tether Gold（XAUt0）でのキャッシュバック。"
implications: "16M ウォレット規模のステーブルコイン保有者に Visa カードレールへのアクセスを開放。Gnosis Pay の『ブロックチェーン上の残高→Visa カード決済』変換インフラが新興国の大規模ユーザーに初めて本格展開。MiCA 7/1 直前の欧州ローンチにより USDT 利用可否が焦点。"
importance: Medium
confidence: High
follow_up: "欧州市場での USDT vs USDC 利用可否（MiCA 7/1 後のスコープ）、Monavate の規制管轄（カード発行体の所在国）、Gnosis Pay インフラの他ウォレットへの展開可能性、Apple Pay / Google Pay での実際の認証フロー"
---

## 概要

Opera の MiniPay は 2026 年 6 月 23 日、Gnosis Pay をテクニカルイネーブラーとして Visa デビットカード（MiniPay Card）をローンチした。MiniPay の 16M+ ユーザーがステーブルコイン残高を Visa 加盟店（175M 以上）・Apple Pay / Google Pay 対応加盟店で直接使用できる。カード発行は Monavate が担当し、Gnosis Pay が MiniPay のオンチェーンステーブルコイン残高を Visa 決済へ変換する。

## 何が起きたか

- **MiniPay Card ローンチ（2026-06-23）**：Opera の MiniPay が Visa デビットカード（デジタル）をリリース
- **対応市場**：欧州・アフリカ・東南アジア・中南米の「選択された市場」（46 カ国での Visa 加盟店決済に対応）
- **技術構成**：
  - MiniPay ウォレット（Celo ブロックチェーン）
  - Gnosis Pay（テクニカルイネーブラー・プログラムマネージャー）
  - Monavate（規制準拠のカード発行体）
  - Visa（グローバルカードネットワーク）
- **ユーザー規模**：16M+ ウォレット・65 カ国以上
- **費用**：月額・年会費なし
- **キャッシュバック**：Tether Gold（XAUt0）・USDT・USDC（対象市場限定）
- **決済手段**：Apple Pay・Google Pay 対応
- **加盟店側**：決済は地元通貨で受け取り、Crypto 対応不要（Gnosis Pay が変換）

## 確認された事実

- ローンチ日：2026-06-23
- 技術インフラ：Gnosis Pay（Ethereum ベースの L2 / デビットカードインフラ）が MiniPay の Celo 上ステーブルコイン残高を Visa に接続
- Monavate は英国の規制準拠カード発行体
- 対応チェーン：Celo（MiniPay 自体は Celo ネイティブ）
- 対応ステーブルコイン：USDC・USDT・Celo ステーブルコイン（cUSD 等）

## なぜ重要か

### 決済事業者視点

- Gnosis Pay がステーブルコインウォレットと Visa ネットワークを接続するホワイトラベルインフラとして機能していることが大規模に実証された。類似インフラを他のウォレットプロバイダーや PSP が採用する際の参照事例
- Monavate（英国カード発行体）が EU / アフリカ / 東南アジア向けにも Visa デビットカードを発行する設計は、グローバルカード発行プラットフォームとしての展開可能性を示す

### 加盟店視点

- 加盟店は何もしなくても MiniPay ユーザー（16M+）が Visa 加盟店で支払える。「ステーブルコイン決済対応」を宣言しなくても既存の Visa 端末で受け取れる設計

### プロダクト視点

- **Gnosis Pay インフラの意義**：オンチェーン残高 → Visa カード決済という変換を決済タイミングでリアルタイム実行する設計は、エージェントが法人口座の仮想カードから支払う設計に応用可能。エージェントが Gnosis Pay 型のインフラを通じて Visa 加盟店に支払うシナリオは技術的に既存の延長線上にある
- **アフリカ・東南アジアへの展開規模**：MiniPay はアフリカ向け展開を先行させており（Celo はアフリカ向け低コスト決済を標榜）、新興国でのステーブルコインカード利用の大規模実証例になる

### 規制 / リスク視点

- **MiCA 7/1 直前の欧州ローンチ**：MiniPay Card が欧州でも提供される場合、USDT が対応通貨に含まれているかどうかは MiCA 下での法的リスクになる。MiCA 施行後、欧州での USDT 利用は事実上禁止。USDC のみ対応に限定するか、欧州を対象外にする必要がある
- Gnosis Pay 自体は EVM ベースの L2（GnoChain）上に構築されており、ブロックチェーン清算と Visa ネットワーク間の接続点が規制対象となる可能性（VASP / 決済機関）

## 我々への示唆

- いま検討すべきこと:
  - Gnosis Pay インフラの技術スペックを確認する。ステーブルコインウォレット→Visa カードの変換設計はエージェント向け法人仮想カードの参照モデルとして評価価値がある
  - MiCA 7/1 後、欧州向けに USDT を組み込んだカード設計をするプロダクトが USDT を除外する必要が生じることを前提に設計を見直す
- 後で深掘りすべきこと:
  - Gnosis Pay のオンチェーン → Visa 変換のレイテンシーと手数料構造（エージェント支払いへの応用可能性の評価軸）
  - Monavate のカード発行スコープ（地域別の発行可否・規制管轄）
- 今は優先度が低いこと:
  - MiniPay への直接統合（現時点ではコンシューマー向けウォレット）

## ありそうな示唆

- Gnosis Pay 型のオンチェーン残高→Visa カード変換インフラは、AI エージェントが法人ウォレットの残高から Visa 加盟店に支払うシナリオのインフラレイヤーとして機能しうる。Mastercard AP4M（カードネットワーク側からエージェントをクレデンシャル化）と Gnosis Pay（ウォレット側からエージェントに Visa カードを発行）は「同じカードレール上での支払い」だが設計の起点が逆になる

## 推測 / 監視ポイント

- MiCA 7/1 施行後に MiniPay の欧州ユーザーが USDT キャッシュバックにアクセスできなくなる対応（USDC 単独化・地域別スコープ分離）
- Gnosis Pay インフラが他のウォレットプロバイダー（Coinbase Wallet・MetaMask 等）に展開されるかどうか
- MiniPay の MiCA 準拠状況（アセット参照型トークン・電子マネートークン規制の適用可能性）

## 未解決の論点

- 欧州市場における USDT キャッシュバックの MiCA 適法性（USDT は MiCA 未認可 EMT）
- Gnosis Pay が使用する GnoChain（旧 xDai）上での清算と Visa ネットワーク間の規制上の位置づけ（英国 FCA / EU MiCA での VASP 定義）
- Apple Pay / Google Pay での認証フローがウォレットベースのオンチェーン署名とどう接続されるか

## 参考リンク

- 一次情報: [Opera プレスリリース via StockTitan（2026-06-23）](https://www.stocktitan.net/news/OPRA/mini-pay-launches-visa-debit-card-to-connect-stablecoin-users-in-qtonsflxih8z.html)
- 補足情報: [CoinTelegraph via TradingView（2026-06-23）](https://www.tradingview.com/news/cointelegraph:2f050dc7e094b:0-opera-s-minipay-launches-visa-debit-card-for-stablecoin-spending/) / [CryptoNews（2026-06-23）](https://cryptonews.net/news/market/33053961/)

## 重要度

- Medium

## 確からしさ

- High（複数メディアで 2026-06-23 ローンチ確認済み）
