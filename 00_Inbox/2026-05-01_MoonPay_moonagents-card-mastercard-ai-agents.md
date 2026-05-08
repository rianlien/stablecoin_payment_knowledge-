---
title: "MoonPay、AI エージェント向け仮想 Mastercard デビットカード「MoonAgents Card」を発表 — Solana USDC でステーブルコイン即時決済"
date: 2026-05-01
source: "PR Newswire / The Block / BanklessTimes"
source_url: "https://www.prnewswire.com/news-releases/moonpay-announces-moonagents-card-enabling-ai-agents-to-spend-stablecoins-anywhere-mastercard-is-accepted-302760128.html"
entity: "MoonPay / Mastercard / Monavate"
category: "payments"
tags:
  - agentic-commerce
  - payments
  - wallet
  - stablecoin
summary: "MoonPay が 2026 年 5 月 1 日、AI エージェントが Mastercard 加盟店でステーブルコインを直接支払える仮想デビットカード「MoonAgents Card」を発表。USDC on Solana をオンチェーン残高から直接使用し、決済時に Monavate がリアルタイムでオンチェーン資金調達とカード承認を実行。ウォレットカストディの移転なし。UK・LATAM で先行提供、米国・EU は今後対応予定。"
implications: "AI エージェントがカード決済ネットワーク（Mastercard）を通じてオフチェーンの実世界加盟店で支払いを行えるインフラが初めて提供された。x402 ベースの機械間決済とは補完的な存在で、実世界の加盟店・サービスへのアクセスを AI エージェントに開く。"
follow_up: "米国・EU 展開タイムライン、対応ステーブルコインの拡張（USDT・EURC 等）、Monavate の Visa ルートとの比較、他 PSP による類似プロダクト展開"
---

## 概要

フィンテック企業 MoonPay が 2026 年 5 月 1 日、AI エージェント向け仮想 Mastercard デビットカード「MoonAgents Card」を発表した。Mastercard の規制準拠メンバーである Monavate と共同開発し、USDC on Solana のオンチェーン残高から直接、Mastercard 加盟店での決済を可能にする。ウォレットの管理権は移転せず、スマートコントラクトが支出を都度承認する非カストディアル設計を採用。ローンチウォレットパートナーは Exodus Movement で、MoonPay CLI 経由で UK・LATAM にて提供開始。

## 何が起きたか

- **発表日**：2026 年 5 月 1 日
- **提供元**：MoonPay（Monavate と共同開発）
- **商品名**：MoonAgents Card（仮想 Mastercard デビットカード）
- **対応ステーブルコイン**：USDC on Solana（現時点）
- **決済の仕組み**：
  1. ユーザー（または AI エージェント）がスマートコントラクトにオンチェーン残高へのアクセスを承認
  2. 決済時、Monavate がオンチェーン資金調達とカード承認をリアルタイムで実行
  3. ウォレットカストディは MoonPay・Monavate 側に移転しない
  4. 承認はいつでも取り消し可能
- **技術基盤**：Monavate（Visa・Mastercard・Discover ネットワークのプリンシパルメンバー）
- **ローンチ地域**：UK・LATAM（MoonPay CLI 経由）。米国・EU は今後対応予定
- **ローンチウォレットパートナー**：Exodus Movement
- **背景**：Mastercard の Crypto Partner Program（2026 年 3 月 11 日発表、85 以上のパートナーに Binance・Circle・PayPal・Ripple・Gemini 等を含む）の延長線上に位置づけられる

## なぜ重要か

### 決済事業者視点

- AI エージェントが Mastercard 加盟店（数千万店舗）でオンチェーン USDC を使って支払えるインフラが初めて提供された。従来、エージェント決済は x402 ベースのオンチェーン API 決済に限られていたが、オフチェーン加盟店への拡張が可能になった
- PSP として重要なのは、Monavate がオンチェーン資金調達とカード承認を同時に処理するアーキテクチャ。従来のカード決済フロー（承認→清算→決済）にオンチェーン決済を組み込む設計の先行事例として参考価値がある

### プロダクト視点

- AI エージェントが「物理世界の加盟店」で支払いを行えるようになることで、ホテル予約・フライト手配・SaaS サービス購入等の高額取引への応用が現実に近づく（AWS AgentCore が目指す「大型トランザクション」と同じ方向）
- 非カストディアル設計（ウォレット移転なし・随時取消可能）は AI エージェントへのアクセス権限管理のモデルとして参考になる

### 規制 / リスク視点

- UK・LATAM 先行提供で米国 GA は未定。CLARITY Act のステーブルコイン規制確定後に米国展開が加速する可能性がある
- 「AI エージェントがカードを持つ」ケースの KYC 要件・不正利用責任所在は法的に未確定

## 我々への示唆

- いま検討すべきこと:
  - MoonAgents Card のアーキテクチャ（Monavate 経由のオンチェーン資金調達 + カード承認）を参考に、自社エージェント決済プロダクトにおけるオフチェーン加盟店対応の設計を検討する
  - UK・LATAM の先行展開地域で試験的な利用ケースを評価する
- 後で深掘りすべきこと:
  - 米国・EU での展開タイムラインと規制対応方針
  - USDC on Solana 以外のステーブルコイン（USDT・EURC 等）対応の予定
  - Monavate の決済フロー詳細（オンチェーン清算のタイミング・ガス費負担主体）
- 今は優先度が低いこと:
  - Mastercard Crypto Partner Program の全パートナー詳細（必要時に個別確認）

## 未解決の論点

- AI エージェントが MoonAgents Card で誤った・不正な取引を行った場合の責任は誰が負うか？
- Monavate の Mastercard ルートとは別に Visa ルートへの拡張はあるか？
- MoonPay CLI とは何か？デベロッパー向け API で AI エージェントに直接発行するための仕組みか？
- 米国での提供開始時期はいつか？CLARITY Act の最終化と連動するか？

## 参考リンク

- 一次情報:
  - [PR Newswire — MoonPay Announces MoonAgents Card（2026-05-01）](https://www.prnewswire.com/news-releases/moonpay-announces-moonagents-card-enabling-ai-agents-to-spend-stablecoins-anywhere-mastercard-is-accepted-302760128.html)
- 補足情報:
  - [The Block — MoonPay launches stablecoin debit card for AI agents on Mastercard（2026-05-01）](https://www.theblock.co/post/399716/moonpay-stablecoin-debit-card-ai-agents-mastercard)
  - [BanklessTimes — MoonPay Launches Stablecoin Debit Card for AI Agents on Mastercard（2026-05-01）](https://www.banklesstimes.com/articles/2026/05/01/moonpay-launches-stablecoin-debit-card-for-ai-agents-on-mastercard/)
  - [Genfinity — MoonPay MoonAgents Card ローンチ詳細](https://genfinity.io/2026/05/01/moonpay-moonagents-card-ai-agents-solana-mastercard-stablecoins/)
  - [関連ノート：Visa ステーブルコイン清算 9 チェーン拡大（2026-04-29）](2026-04-29_Visa_stablecoin-settlement-9chains-7b.md)
  - [関連ノート：Stripe Sessions 2026 ステーブルコイン拡大（2026-04-30）](2026-04-30_Stripe-Sessions-2026_stablecoin-expansion.md)

## 重要度

- Medium

## 確からしさ

- High
