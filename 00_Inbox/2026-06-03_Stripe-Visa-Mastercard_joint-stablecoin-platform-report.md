---
title: "報道: Stripe・Visa・Mastercard が共同ステーブルコインプラットフォームを準備中、Coinbase も参加検討"
date: 2026-06-04
source: "CoinDesk / PYMNTS / CryptoBriefing"
source_url: "https://www.coindesk.com/business/2026/06/03/payment-giants-stripe-visa-mastercard-said-to-be-among-backers-of-soon-to-debut-stablecoin-platform"
entity: "Stripe, Visa, Mastercard, Coinbase"
category: "stablecoin-payments"
primary_category: "payment-rails"
article_published_date: 2026-06-03
underlying_event_date: 2026-06-03
primary_source_date: 2026-06-03
tags:
  - stablecoin-payments
  - payment-rails
  - agentic-commerce
  - visa
  - mastercard
summary: >
  CoinDesk が 2026 年 6 月 3 日、Stripe・Visa・Mastercard が共同ステーブルコインプラットフォームを近日中に公開する予定と報道。Coinbase も参加を検討中。3 社はいずれもコメントを拒否。プラットフォームの名称・詳細は未公表。
implications: >
  決済ネットワーク大手 3 社が共同でステーブルコイン決済プラットフォームを構築するとなれば、現行のフィアット決済インフラとステーブルコインレールを統合する動きとして業界史上最大規模の転換点になりうる。ただし現時点では未確認報道であり、各社がコメントを拒否している点に留意。
importance: High
confidence: Low
follow_up: "各社の公式発表（名称・仕様・ローンチ日）、Coinbase の参加可否確認、x402 / MPP / Agent Pay との統合設計の有無"
---

## 概要

2026 年 6 月 3 日、CoinDesk が Stripe・Visa・Mastercard が共同ステーブルコインプラットフォームを近日中に立ち上げる予定と報道した。Coinbase も参加を検討中とされる。3 社は CoinDesk のコメント求めに応じず、Mastercard も締切までに回答しなかった。

## 何が起きたか

- **報道日時**：2026 年 6 月 3 日（CoinDesk 一次報道）
- **参加報道企業**：Stripe（Bridge 所有）、Visa、Mastercard（BVNK 買収済み）、Coinbase（参加検討中）
- **プラットフォームの目的**：ステーブルコイン決済ネットワークの拡張
- **公式コメント**：Coinbase・Stripe・Visa はコメント拒否、Mastercard は回答なし
- **プラットフォームの詳細**：名称・仕様・ローンチ日のいずれも未公表

## 各社のステーブルコイン関連既存動向

| 企業 | 直近のステーブルコイン関連動向 |
|------|-------------------------------|
| Stripe | Bridge 買収（$1.1B、2024 年末）。Stripe Bridge が MoneyGram MGUSD の発行体に（2026-06-02）。x402・MPP・UCP 実装パートナー |
| Visa | ステーブルコイン連携カードプログラム 160 件超。ステーブルコイン決済の年間換算額 $70 億（Q2 2026 決算）。9 チェーンに対応。 |
| Mastercard | BVNK 買収（$1.8B）。エージェント決済（Agent Pay）・Verifiable Intent。欧州全 MC イシュアーが Agent Pay 対応 |
| Coinbase | x402 プロトコル、Base ネットワーク、CPN（Circle Payments Network 隣接）。x402 累計 1 億件 |

## 確認された事実

- CoinDesk が 3 社の共同プラットフォーム準備を報道（信頼性の高いメディア）
- 各社はコメント拒否（確認も否定もしていない）
- PYMNTS・CryptoBriefing・Bitcoin.com 等の複数媒体が追報
- プラットフォームの具体的な内容（名称・スコープ・技術仕様）は不明

## なぜ重要か

### 決済事業者視点

- Stripe（UCP 実装 PSP・Bridge 所有）× Visa（Intelligent Commerce・Agentic Ready）× Mastercard（Agent Pay・BVNK）が共同でステーブルコイン決済プラットフォームを構築するとすれば、3 社それぞれの既存エージェント決済インフラが統合・相互運用される可能性を示す
- PSP としては、この統一プラットフォームへのアクセス方法を早期に把握することが競争上重要

### 加盟店視点

- 3 社の共同プラットフォームが実現すれば、加盟店は単一の統合でステーブルコイン・エージェント決済を受け入れられる可能性がある
- 現在の UCP（Shopify × Google × Stripe）エコシステムと結びつくかどうかが設計上の重要な分岐点

### プロダクト視点

- x402（Coinbase）× MPP（Stripe）× Agent Pay（Mastercard）× Intelligent Commerce（Visa）という現行の断片化した 4 スタックが統一プラットフォームに収束する可能性と、それぞれが独立したままこのプラットフォームに接続する可能性の両方を想定して設計する

### 規制 / リスク視点

- 3 大決済ネットワークによる共同ステーブルコインプラットフォームは、米国 DOJ の反トラスト調査の対象になりうる
- GENIUS Act の PPSI 要件との整合（誰が PPSI として登録されるか）が規制上の構造問題を提起する

## 我々への示唆

- いま検討すべきこと:
  - 公式発表を待ちながら、プラットフォームが x402・MPP・UCP とどのように関係するかを整理するフレームワークを用意する
- 後で深掘りすべきこと:
  - 公式発表後すぐに技術仕様・接続要件・ローンチタイムラインを確認する
  - 競合プラットフォーム（Circle CPN・Coinbase エコシステム）への影響を評価する
- 今は優先度が低いこと:
  - 未確認報道の段階で実装対応を開始すること

## ありそうな示唆

- 3 社の共同プラットフォームが実現すれば、既存のエージェント決済スタック（x402・MPP・Agent Pay・Intelligent Commerce）の統合を加速させる「決済インフラの Windows モーメント」になりうる
- 競合する Circle（CPN）・Coinbase（x402）へのプレッシャーが高まり、Circle が参加を求められる可能性もある

## 推測 / 監視ポイント

- 公式発表のタイミング（Money 20/20 Europe 期間中？それとも別のイベント？）
- プラットフォームは USDC 中心か、複数ステーブルコイン対応か
- Coinbase の最終的な参加可否——参加すれば x402 と統一プラットフォームの関係が決まる
- GENIUS Act 規制の文脈でどのように位置づけられるか（PPSI か非 PPSI か）

## 未解決の論点

- このプラットフォームはエージェント決済（Agent Pay・x402）とどのように接続するのか？
- Stripe Bridge（MoneyGram MGUSD の発行体）がプラットフォームの発行インフラを担うのか？
- プラットフォームへの参加要件は開放型か、クローズド型か？

## 参考リンク

- 一次情報: [CoinDesk（2026-06-03）](https://www.coindesk.com/business/2026/06/03/payment-giants-stripe-visa-mastercard-said-to-be-among-backers-of-soon-to-debut-stablecoin-platform)
- 補足情報: [PYMNTS](https://www.pymnts.com/cryptocurrency/2026/mastercard-and-visa-back-stealth-stablecoin-platform/) / [CryptoBriefing](https://cryptobriefing.com/stripe-visa-and-mastercard-close-launching-joint-stablecoin-platform/) / [Bitcoin.com](https://news.bitcoin.com/report-payments-giants-visa-mastercard-and-stripe-back-stablecoin-platform-for-faster-payments/)

## 重要度

- High

## 確からしさ

- Low（全社がコメント拒否、プラットフォーム詳細不明）
