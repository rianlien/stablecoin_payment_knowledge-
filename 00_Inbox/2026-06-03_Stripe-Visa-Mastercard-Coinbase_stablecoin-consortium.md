---
title: "Stripe・Visa・Mastercard・Coinbase、共同ステーブルコインプラットフォーム設立を計画——The Information 報道"
date: 2026-06-03
source: "The Information / CoinDesk / CryptoBriefing / Yahoo Finance / CryptoAdventure"
source_url: "https://www.coindesk.com/business/2026/06/03/payment-giants-stripe-visa-mastercard-said-to-be-among-backers-of-soon-to-debut-stablecoin-platform"
entity: "Stripe / Visa / Mastercard / Coinbase / Circle / Tether"
category: "stablecoin-infrastructure"
primary_category: "stablecoin-payments"
article_published_date: 2026-06-03
underlying_event_date: 2026-06-03
primary_source_date: 2026-06-03
tags:
  - stablecoin
  - payments
  - regulation
  - agentic-commerce
  - machine-payments
summary: "2026 年 6 月 3 日、The Information が Stripe・Visa・Mastercard の 3 社がコンソーシアム型の新ステーブルコインプラットフォームを設立する計画を報道。Coinbase も参加を検討中とされる。目的は Circle・Tether が支配する $3,250 億のステーブルコイン市場への参入と、エージェント決済を含む決済インフラのデジタル化。各社からの公式確認はなし。Circle・Coinbase の株価は報道後に下落。"
implications: "確認されれば、これは agentic commerce の「決済レール競争」における最も重大な構造変化。Stripe（MPP）・Visa（TAP/ICC）・Coinbase（x402）は今後 agentic payments の標準プロトコルをそれぞれ推進しており、共通のステーブルコインインフラを持つことは三者の協調と競合の新たな関係性を生む可能性がある。"
importance: High
confidence: Medium
follow_up: "各社からの公式確認・発表のタイミング、新ステーブルコインの名称・ブロックチェーン基盤・準備金構造、Circle USDC・Tether USDT との競合 or 共存戦略、agentic commerce プロトコル（MPP・x402・TAP）との統合設計"
---

## 概要

2026 年 6 月 3 日、米テクノロジーメディア The Information が Stripe・Visa・Mastercard の 3 社による共同ステーブルコインプラットフォーム設立計画を独自報道した。Coinbase も参加を検討中とされる。各社は公式コメントを出しておらず、プラットフォームの名称・ブロックチェーン基盤・トークン詳細・準備金構造は一切未公開。

## 何が起きたか

- **The Information 報道（2026-06-03）**：Stripe・Visa・Mastercard が共同でステーブルコインプラットフォームを設立し、新たなステーブルコインを発行する計画。まもなくデビューと表現
- **Coinbase の立場**：参加を検討しているとされるが確認は取れていない。報道後に Coinbase 株価は下落
- **Circle 株価への影響**：Circle（ティッカー CRCL）の株価も報道後に下落——同社の USDC の将来的な競合脅威として市場が解釈
- **戦略的背景**：
  - Stripe：2024 年末に Bridge（ステーブルコインインフラ）を $11 億で買収済み
  - Mastercard：2026 年に BVNK（デジタルアセット PSP）を買収済み
  - Visa：Intelligent Commerce / Trusted Agent Protocol 等のエージェント決済インフラを整備中
  - Coinbase：x402 / Base MCP / Circle CPN 周辺に展開中
- **市場規模**：ステーブルコイン市場総額は $3,250 億（2026 年 6 月時点）、Circle（USDC）+ Tether（USDT）で約 80% を占有

## 確認された事実

- The Information による独自報道（一次ソース）
- CoinDesk・CryptoBriefing 等複数メディアが同日追随報道
- Circle・Coinbase の株価下落は事実（市場の反応として確認）
- Stripe の Bridge 買収・Mastercard の BVNK 買収は既知の事実

## なぜ重要か

### 決済事業者視点
- Stripe（MPP ＝ Machine Payments Protocol 推進）・Visa（TAP ＝ Trusted Agent Protocol）・Coinbase（x402）が共通のステーブルコインインフラを持てば、それぞれのエージェント決済プロトコルが「同一ステーブルコイン」を決済手段として使う設計になりうる
- 現在の Circle USDC・Tether USDT への依存から、大手決済企業の自社ステーブルコインへの移行が加速するシナリオが生まれる

### 加盟店視点
- Stripe・Visa・Mastercard の三社が同一ステーブルコインを発行すれば、加盟店はこれら 3 社と既存契約があれば自動的に新ステーブルコイン対応になる可能性がある——導入コストの大幅な低下

### プロダクト視点
- MPP（Stripe）・TAP（Visa）・x402（Coinbase）が共通の決済手段（新コンソーシアムステーブルコイン）を採用するシナリオでは、「プロトコルの違い」よりも「どのステーブルコインを使うか」が設計上の主要変数になる
- USDC ベースで設計しているプロダクトは、将来的な切り替えコストを考慮した柔軟な設計が必要になる可能性

### 規制 / リスク視点
- コンソーシアム型ステーブルコインは GENIUS Act 下で「複数の PPSI が共同発行体として認定されるか」という新しい法的問題を提起する
- 独占禁止法：Stripe・Visa・Mastercard・Coinbase が同一のステーブルコインを共同発行することに対して、規制当局（DOJ・FTC・欧州委員会）が審査を行う可能性がある

## 我々への示唆
- いま検討すべきこと:
  - USDC（Circle）・USDT（Tether）への依存設計のリスク評価——コンソーシアムステーブルコインが市場に出た場合の切り替えコストを今から想定しておく
  - 各社の公式発表を待ちながら、発表後に迅速に技術仕様を確認できる体制を整える（ブロックチェーン基盤・SDK・API の公開タイミング）
- 後で深掘りすべきこと:
  - プラットフォーム詳細が公開された際の x402 / MPP / TAP との統合設計——既存 agentic commerce プロトコルとの整合性
  - GENIUS Act 下でのコンソーシアム型 PPSI 認定の法的可否
- 今は優先度が低いこと:
  - The Information 単独報道であり公式確認前の詳細推測（ブロックチェーン選択・準備金比率等）

## ありそうな示唆
- Stripe が Bridge 経由でステーブルコインインフラを持ち、Mastercard が BVNK を持ち、Visa が独自エージェント認証を持つという三社の既存投資の延長線上として、共同プラットフォームは戦略的に自然
- コンソーシアムステーブルコインが具体化すれば、Circle の USDC は「中立インフラ」から「競合製品」に位置づけが変わる

## 推測 / 監視ポイント
- **公式発表のタイミング**：The Information は「まもなくデビュー」と表現。正式発表があり次第、詳細を精査する
- **Coinbase の参加/不参加**：Coinbase が参加すれば x402 と新コンソーシアムステーブルコインの統合が現実になる。不参加でも x402 / Base エコシステムへの影響は大きい
- **Circle の対応**：競合ステーブルコインの登場に対して Circle が USDC の普及促進を加速するか、または何らかのコンソーシアム参加の動きを取るか

## 未解決の論点
- 新ステーブルコインの名称・ブロックチェーン基盤・準備金構造は一切不明
- コンソーシアム型ステーブルコイン発行体は GENIUS Act の PPSI 認定において「共同発行体」として扱われるか？
- Mastercard が BVNK 買収で得たインフラをコンソーシアムに持ち込むのか、それとも独自に運用するのか？

## 参考リンク
- 一次情報:
  - [The Information（2026-06-03、有料）](https://www.theinformation.com/briefings/stripe-visa-mastercard-coinbase-form-consortium-issue-new-stablecoin)
  - [CoinDesk（2026-06-03）](https://www.coindesk.com/business/2026/06/03/payment-giants-stripe-visa-mastercard-said-to-be-among-backers-of-soon-to-debut-stablecoin-platform)
- 補足情報:
  - [CryptoBriefing（2026-06-03）](https://cryptobriefing.com/stripe-visa-mastercard-coinbase-stablecoin-consortium/)
  - [Yahoo Finance / 元記事](https://finance.yahoo.com/markets/crypto/articles/visa-mastercard-collaborate-stablecoin-platform-130900834.html)
  - [FinanceFeeds（2026-06-03）](https://financefeeds.com/stripe-visa-and-mastercard-near-stablecoin-platform-launch/)
  - [PYMNTS.com（2026-06-03）](https://www.pymnts.com/cryptocurrency/2026/mastercard-and-visa-back-stealth-stablecoin-platform/)

## 重要度
- High

## 確からしさ
- Medium（The Information による単独報道。各社公式確認なし。株価反応は事実だが、The Information の報道が確度の高い根拠。公式発表まで推測扱いが適切）
