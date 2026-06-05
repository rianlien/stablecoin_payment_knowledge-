---
title: "Stripe・Visa・Mastercard・Coinbase が新ステーブルコインコンソーシアム設立へ——Circle / Tether 市場支配に挑戦"
date: 2026-06-05
source: The Information / CoinDesk / CryptoBriefing
source_url: https://www.coindesk.com/business/2026/06/03/payment-giants-stripe-visa-mastercard-said-to-be-among-backers-of-soon-to-debut-stablecoin-platform
entity:
  - Stripe
  - Visa
  - Mastercard
  - Coinbase
  - Circle（影響）
  - Tether（影響）
category: stablecoin-payments
primary_category: stablecoin-payments
article_published_date: 2026-06-03
underlying_event_date: 2026-06-03
primary_source_date: 2026-06-03
tags:
  - stablecoin
  - stablecoin-payments
  - agentic-commerce
  - payment-rails
  - regulation
summary: "Stripe・Visa・Mastercard が共同で新ステーブルコインプラットフォームを近くローンチすると The Information が報道。Coinbase も参加を検討中。現在市場の 80% を占める Circle（USDC）と Tether（USDT）への挑戦者として、決済大手 3 社が一体型ステーブルコインインフラを構築する。公式名称・トークン詳細・準備資産構造は未開示。"
implications: "円決済プロトコルの標準をめぐる競争が加速。USDC 中心の現エコシステム（x402・CPN・AgentCore）が長期的に代替ステーブルコインへのシフトを強いられる可能性があるが、短期（2026 年）では現状維持。"
importance: High
confidence: Medium
follow_up: "公式アナウンス・コンソーシアム名・チェーン・準備資産構造の一次確認。Circle 株価・Coinbase 株価への影響確認。GENIUS Act 規制下での新ステーブルコイン発行スキームの確認。"
---

## 概要

Stripe・Visa・Mastercard が新たなステーブルコインプラットフォームを共同で近くローンチすると The Information が 2026 年 6 月 3 日に報道。Coinbase も参加を検討中とされる。現在市場の約 80% を占める Circle（USDC）と Tether（USDT）への挑戦として位置づけられており、決済ネットワーク・PSP・暗号資産取引所が一体化したステーブルコインエコシステムを構築する狙い。

## 何が起きたか

- The Information が複数の事情通取材をもとに報道。Stripe・Visa・Mastercard が新ステーブルコインプラットフォームを近く立ち上げる予定
- Coinbase は参加を「検討中（looking into）」の段階（CoinDesk 報道では Coinbase の参加は Stripe・Visa・Mastercard より確度が低い）
- 公式発表なし。コンソーシアム名・発行トークン・準備資産構造・展開チェーンはすべて未開示
- Coinbase・Stripe・Visa は取材に対しコメントを拒否。Mastercard は未回答
- 報道後、Circle（CRCL）株と Coinbase 株が下落

## 確認された事実

- 報道日：2026-06-03
- 情報源：The Information（複数の内部事情通）→ CoinDesk・CryptoBriefing・PYMNTS 等が追報
- 参加確報済み：Stripe・Visa・Mastercard
- 参加検討中：Coinbase（確定ではない）
- 各社の既存コミットメント：
  - Stripe：2024 年末に Bridge（ステーブルコインインフラ）を $11 億で買収済み
  - Mastercard：2026 年初頭に BVNK を買収済み。2026-06-03 に独立した 24/7 ステーブルコイン決済拡張も発表
  - Visa：9 チェーンへのステーブルコイン決済拡張（2026-04-29 ノート）、Replit への TAP 戦略出資（2026-05-28 ノート）
  - Coinbase：x402 開発元、Circle との USDC 共同設立の歴史を持つが、USDC 競合ステーブルコインへの参画は方針転換を意味する

## なぜ重要か

### 決済事業者視点

- 世界最大規模の決済ネットワーク 2 社（Visa・Mastercard）と最大の PSP（Stripe）が単独のステーブルコインコンソーシアムに入れば、加盟店・金融機関への普及速度は Circle や Tether が単独で達成できる速度を大幅に上回る
- 「加盟店が受け入れるステーブルコイン」の事実上の標準を、コンソーシアムが定義できる立場になる

### 加盟店視点

- Stripe の Bridge インフラ・Visa の TAP 認証・Mastercard の 24/7 決済との統合が実現すれば、加盟店は既存の Stripe / Visa / Mastercard 契約のまま新ステーブルコインへ移行できる可能性がある
- 現在 UCP・x402・MPP などで前提とされている USDC が将来的に代替されるリスクが生じる

### プロダクト視点

- x402（Coinbase）・CPN（Circle）・MPP（Stripe/Tempo）はいずれも USDC を基軸としている。コンソーシアムが発行するステーブルコインが x402 / MPP の対応通貨に加わるのか、または代替するのかが設計上の分岐点
- Stripe が MPP と Bridge の両方を持ちつつ、コンソーシアムにも参加するのであれば、MPP の「デフォルト通貨」が変わる可能性がある

### 規制 / リスク視点

- GENIUS Act（米国）および MiCA（EU）の PPSI 規制下でコンソーシアムステーブルコインをどう位置づけるかは未確認
- 既存の USDC / USDT への市場集中リスクを分散する政策面では歓迎されうる
- Coinbase が参加する場合、自社が共同創設した USDC（Circle）の競合ステーブルコインに資金・技術を注ぐことになり、規制当局・パートナーからの注目を集める

## 我々への示唆

- いま検討すべきこと:
  - 自社プロダクトが特定ステーブルコイン（USDC 等）にハードコードされている場合、マルチステーブルコイン設計への移行コストを概算する
  - コンソーシアムの公式発表を待って、発行チェーン・準備資産・GENIUS Act 適合性を確認し、自社統合の優先度を評価する
- 後で深掘りすべきこと:
  - 公式発表後に、コンソーシアムステーブルコインと USDC の機能比較（流動性・決済速度・対応チェーン・規制適合性）を実施
  - Stripe が MPP とコンソーシアムステーブルコインをどう整合させるかの仕様確認
- 今は優先度が低いこと:
  - コンソーシアム名・トークン詳細が非公開である段階での技術選定変更は時期尚早

## ありそうな示唆

- 「コンソーシアムステーブルコインと USDC の共存」が最初の数年間のシナリオ（すべての参加企業が既に USDC に深いコミットメントを持つため）
- Coinbase が最終的に参加する場合、x402 の「デフォルト通貨」がコンソーシアムステーブルコインに変わる可能性があるが、移行には 1〜2 年のエコシステム整備が必要

## 推測 / 監視ポイント

- コンソーシアムの公式ローンチ発表（2026 年夏〜秋と推定）
- Circle の対抗措置（新機能・シェア防衛策）
- GENIUS Act 最終規則（7/18 デッドライン）との関係——コンソーシアムが GENIUS Act 準拠 PPSI として登録するかどうか
- Coinbase の正式参加 / 不参加の最終決定

## 未解決の論点

- コンソーシアムステーブルコインの発行主体（誰が PPSI ライセンスを取得するか）
- 準備資産の構成と管理主体
- 展開チェーン（Bridge は多チェーン対応実績あり。Solana・Base・Ethereum が有力候補）
- Coinbase 参加の条件（x402 対応・USDC との関係整理）

## 参考リンク

- 一次情報: [The Information（2026-06-03）](https://www.theinformation.com/briefings/stripe-visa-mastercard-coinbase-form-consortium-issue-new-stablecoin)（ペイウォール）
- 補足情報: [CoinDesk（2026-06-03）](https://www.coindesk.com/business/2026/06/03/payment-giants-stripe-visa-mastercard-said-to-be-among-backers-of-soon-to-debut-stablecoin-platform), [CryptoBriefing（2026-06-03）](https://cryptobriefing.com/stripe-visa-mastercard-coinbase-stablecoin-consortium/), [PYMNTS（2026-06-03）](https://www.pymnts.com/cryptocurrency/2026/mastercard-and-visa-back-stealth-stablecoin-platform/)

## 重要度

- High

## 確からしさ

- Medium（複数の独立したメディアが報道しており信頼性は高いが、公式確認がないため Medium とする）
