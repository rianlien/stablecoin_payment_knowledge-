---
title: "Stripe・Visa・Mastercard が新ステーブルコイン連合を計画、Coinbase も参加を検討——The Information 報道"
date: 2026-06-03
source: The Information / CoinDesk / CryptoBriefing
source_url: https://www.coindesk.com/business/2026/06/03/payment-giants-stripe-visa-mastercard-said-to-be-among-backers-of-soon-to-debut-stablecoin-platform
entity: Stripe / Visa / Mastercard / Coinbase
category: stablecoin-payments
primary_category: stablecoin-payments
article_published_date: 2026-06-03
underlying_event_date: 2026-06-03
primary_source_date: 2026-06-03
tags:
  - stablecoin
  - Stripe
  - Visa
  - Mastercard
  - payment-rails
summary: "The Information が2026年6月3日に報道。Stripe・Visa・Mastercard の3社が新たなステーブルコイン発行プラットフォームを共同で計画しており、Coinbase も参加を検討中と複数の内部関係者が証言した。プロジェクトは初期段階で、正式名称・トークン詳細・準備金構造はいずれも未公開。"
implications: "Circle（USDC）と Tether（USDT）が合計約80%のシェアを持つ3250億ドル規模のステーブルコイン市場に、既存決済ネットワーク3社が連合で参入する構図。エージェント決済インフラとして採用される場合、既存ステーブルコイン（USDC・USDT）との競合・共存の構図が大幅に変わりうる。"
importance: High
confidence: Low
follow_up: "公式発表・プラットフォーム名・トークン詳細・準備金設計・発行体の確定、Coinbase の参加可否（Circle USDC との収益分配契約との関係）、GENIUS Act 準拠設計かどうか"
---

## 概要
- The Information（2026-06-03 報道）：Stripe・Visa・Mastercard がステーブルコイン発行プラットフォームを共同で計画。Coinbase も参加を検討中
- 情報源: 計画を知る複数の匿名関係者
- 現時点では初期段階——名称・トークン詳細・準備金構造すべて未公開

## 何が起きたか
- The Information が内部関係者複数からの情報として「Stripe・Visa・Mastercard が近く公開予定の新ステーブルコインプラットフォームの支援者」と報道
- Coinbase は参加を「検討中」と位置付け——決定には至っていない（Circle USDC との収益分配契約が影響要因）
- 各社の既存ステーブルコイン投資:
  - Stripe: 2024年末に Bridge（ステーブルコインインフラ）を11億ドルで買収
  - Mastercard: 2026年に BVNK（ステーブルコイン企業）を買収、同週に常時稼働ステーブルコイン決済拡張を発表
  - Visa: 2026年4月に9チェーンへのステーブルコイン決済パイロット拡張を発表
- ステーブルコイン市場全体: 3,250 億ドル超、Circle + Tether で約80%

## 確認された事実
- 報道日: 2026-06-03（The Information / CoinDesk）
- 確認情報元: 計画を知る複数の匿名関係者（一次発表なし）
- プロジェクト状況: 初期段階
- 名称・トークン・準備金: 未公開
- Coinbase の参加: 検討中（決定なし）

## なぜ重要か

### 決済事業者視点
- Stripe・Visa・Mastercard の3社が共同でステーブルコインを発行する場合、既存カードネットワーク全体をカバーする分散インフラが生まれる可能性
- 既存 Circle USDC・Tether に依存した決済インフラへの影響度が高い

### 加盟店視点
- 決済ネットワーク（Visa・Mastercard）が直接発行するステーブルコインは、加盟店にとって「フィアット同等」として扱いやすい設計になる可能性
- Stripe の Bridge インフラを活用した発行なら、既存 Stripe 加盟店への普及速度が高い

### プロダクト視点
- エージェント決済の spending mandate や認可フレームワーク（AP2・TAP）との統合設計が今後の焦点
- 新ステーブルコインが x402 や MPP で使用可能かどうかは現時点で不明

### 規制 / リスク視点
- GENIUS Act 準拠設計（federally qualified nonbank または depository subsidiary）かどうかが最重要点
- 既存発行体（Circle・Tether）は新参入者を「デファクト規制強化」として受け取る可能性

## 我々への示唆
- いま検討すべきこと:
  - Circle USDC との関係を見直す前に、公式発表を待つ（現時点では匿名報道のみ）
  - Coinbase の参加可否が USDC エコシステムに与える影響を暫定的にシナリオ設計しておく
- 後で深掘りすべきこと:
  - 正式発表後: 準備金設計（US Treasuries 100%か）・発行体（誰が GENIUS Act 上の「permitted issuer」か）・対応ブロックチェーン
  - エージェント決済プロトコル（x402・AP2）との対応状況
- 今は優先度が低いこと:
  - 既存 USDC インフラの置き換え計画（正式発表前は不要）

## ありそうな示唆
- Stripe（MPP・Bridge）+ Visa（TAP・VIC）+ Mastercard（Agent Pay・BVNK）の3社がそれぞれエージェント決済インフラを独自整備している状況で、ステーブルコイン発行でも連合を組むことは、既存カードネットワーク勢力が暗号資産決済レールを取り込む大きな一手になる
- Coinbase が参加する場合、Circle USDC との関係が複雑になる——Circle IPO（2026年想定）のタイミングとの関係も注目

## 推測 / 監視ポイント
- 正式発表のタイミング（数週間〜数ヶ月）
- Coinbase の最終的な参加可否とその条件
- Circle の株価・市場反応（報道翌日に下落が観測された）
- GENIUS Act 準拠の発行体構造

## 未解決の論点
- 誰が技術的な発行体（permitted issuer）になるか
- Stripe Bridge が発行インフラを担うか
- 既存の USDC・USDT との相互運用性
- 新ステーブルコインのユースケース（消費者向けか B2B 向けか、エージェント向けか）

## 参考リンク
- 一次情報（報道）: CoinDesk（2026-06-03）https://www.coindesk.com/business/2026/06/03/payment-giants-stripe-visa-mastercard-said-to-be-among-backers-of-soon-to-debut-stablecoin-platform
- 補足: CryptoBriefing https://cryptobriefing.com/stripe-visa-mastercard-coinbase-stablecoin-consortium/
- 補足: The Paypers https://thepaypers.com/crypto-web3-and-cbdc/news/stripe-visa-and-mastercard-reportedly-plan-joint-stablecoin-platform
- 補足: PYMNTS https://www.pymnts.com/cryptocurrency/2026/mastercard-and-visa-back-stealth-stablecoin-platform/

## 重要度
- High

## 確からしさ
- Low（複数の匿名関係者による報道、公式発表なし）
