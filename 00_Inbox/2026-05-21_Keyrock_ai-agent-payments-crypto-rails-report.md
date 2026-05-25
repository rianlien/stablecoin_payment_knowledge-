---
title: "Keyrock、AI エージェント決済レポート発表——$73M・176M 件、98.6% が USDC、76% がカード手数料下限以下"
date: 2026-05-25
source: CoinDesk / Keyrock
source_url: https://www.coindesk.com/business/2026/05/21/crypto-rails-are-becoming-the-default-payment-layer-for-ai-agents-report-says
entity: Keyrock
category: research-report
primary_category: machine-payments
article_published_date: 2026-05-21
underlying_event_date: 2026-05-21
primary_source_date: 2026-05-21
tags:
  - machine-payments
  - agentic-commerce
  - stablecoin-infrastructure
  - x402
  - research
summary: "デジタル資産マーケットメーカー Keyrock が AI エージェント決済の定量分析レポートを発表（CoinDesk 掲載 2026-05-21）。過去 12 ヶ月（2025-05〜2026-04）のオンチェーンデータを分析し、エージェント決済は$73M・176M 件・平均$0.48、98.6% が USDC、76% がカードネットワークの最低手数料$0.30 を下回ることを定量化。Coinbase（x402）・Stripe（MPP / Tempo）・Google（AP2）・Visa が競合インフラを構築中。規制面では MiCA（7/1）・GENIUS Act（7/18）・EU AI Act（8/2）が数週間以内に施行されるが、機械間取引への直接規定はいずれも存在しない。"
implications: "「76% がカードの$0.30 手数料下限以下」という定量データは、エージェント決済でカードレールが構造的に経済合理性を失うことを裏付ける最初期の統計的証拠。USDC 集中（98.6%）は Circle の単一障害点リスクを浮き彫りにし、規制リスクも含む。"
importance: High
confidence: High
follow_up: "Keyrock レポート全文（一次資料）の入手と詳細分析、USDC 集中度が今後低下するか（AllUnity SEKAU、WSPN WUSD 等の参入で）、機械間取引に対する GENIUS Act / EU AI Act の補足規制案の動向、x402・MPP・AP2 の市場シェア推移"
---

## 概要

- マーケットメーカー Keyrock が AI エージェントによるオンチェーン決済の定量分析レポートを公開（CoinDesk が 2026-05-21 に報道）
- 過去 12 ヶ月（2025 年 5 月〜2026 年 4 月）で $73M・176M 件を集計、98.6% が USDC
- 76% の取引がカードネットワークの最低手数料（$0.30 固定）を下回り、従来決済レールの経済非合理性を定量化

## 何が起きたか

- Keyrock がオンチェーンデータ分析に基づく AI エージェント決済レポートを公表
- **主要統計**：
  - 総額：$73M超（12 ヶ月）
  - 件数：176M 件超
  - 平均取引サイズ：$0.48（安定化傾向）
  - USDC 比率：98.6%
  - カード最低手数料（$0.30）を下回る取引：76%
  - 典型的な取引レンジ：$0.01〜$0.10
- **競合インフラ状況**：Coinbase（x402 / Base）・Stripe（MPP / Tempo）・Google（AP2）・Visa が機械間決済インフラを並走して構築

## 確認された事実

- CoinDesk 記事 URL（coindesk.com/business/2026/05/21/）から 2026 年 5 月 21 日付の報道と確認
- Bitcoin News も同日数値（76% below Visa's $0.30 fee floor）を報道、複数媒体で裏どり済み
- Keyrock は欧州系デジタル資産マーケットメーカー。データはオンチェーンのオンパブリックデータに基づく分析と見られる（レポート全文未確認）

## なぜ重要か

### 決済事業者視点
- カードレールの最低手数料は機械間マイクロペイメントに対して構造的な障壁。76% という数値は「エージェント決済の大多数がカードを使えない」ことを意味し、ステーブルコインオンチェーン決済への移行の必然性を定量的に支持する最初期の業界データ

### 加盟店視点
- エージェントが$0.01〜$0.10 で API・データ・コンテンツを購入するモデルは、従来の課金単位（月額・年額サブスクリプション）を根本的に変える。加盟店は API 従量課金モデルへの移行準備が必要

### プロダクト視点
- 98.6% USDC 集中は、他のステーブルコイン（USDT・PYUSD・WUSD・SEKAU 等）が機械間決済市場でほぼ存在感ゼロであることを意味。USDC のデファクト地位は競合各社にとって参入障壁

### 規制 / リスク視点
- MiCA（2026-07-01 移行期終了）・GENIUS Act（2026-07-18 最終規則期限）・EU AI Act（2026-08-02 ハイリスク義務発効）が数週間以内に揃うが、いずれも機械間取引への直接規定を持たない——規制の空白が数ヶ月単位で続く

## 我々への示唆
- いま検討すべきこと:
  - 「76% がカード手数料下限以下」は自社のエージェント決済設計においてカードレールを除外する判断根拠として使える。ステーブルコインオンチェーンを第一選択とするアーキテクチャの方向性を早期に確定する
  - 98.6% USDC 集中に対して自社はどこまで許容するか——Circle の規制リスク・システムリスクを踏まえた分散方針の検討（USDC + EURC など）
- 後で深掘りすべきこと:
  - Keyrock レポート全文入手と詳細数値の確認（特に取引量の月次推移・プロトコル別内訳）
  - $73M という規模感の文脈化（x402 の年率 $600M 発表値との差分——集計対象・定義の違い）
- 今は優先度が低いこと:
  - 個別プロトコル（x402 vs. MPP vs. AP2）のシェア詳細——現状は USDC の支配が圧倒的で、プロトコル間の差分は二次的

## ありそうな示唆
- 12 ヶ月で $73M・176M 件は「実験規模」だが、Gartner の $15T（2028）・McKinsey の $3T〜$5T（2030）予測と並置すると、今後 2〜4 年で 3〜4 桁のスケールアップが必要になる。インフラボトルネックはウォレット管理・ID 認証・spend governance に移行する可能性が高い
- USDC 集中（98.6%）は Circle の規制ライセンス取得（PPSI）進捗と裏表の関係——GENIUS Act 最終規則後に PPSI 未認定ステーブルコインが排除されると逆に USDC 比率が上昇する可能性もある

## 推測 / 監視ポイント
- Keyrock レポートのデータソースが公開されれば、x402 / MPP / AP2 別のトランザクション内訳が判明するかもしれない
- 「機械間取引の規制空白」は 2026 年 7〜8 月の規制施行後に業界団体・当局がコメントを始める可能性——監視対象

## 未解決の論点
- $73M の集計対象は何か（x402 対応 API のみ？それとも全 AI エージェント起因オンチェーン転送？）
- 98.6% USDC は「Circle が発行した USDC のみ」か「USDC と USDC 由来のラップトークンを含む」か
- 176M 件のうち bot / テスト取引が占める割合

## 参考リンク
- 一次情報: [CoinDesk（2026-05-21）](https://www.coindesk.com/business/2026/05/21/crypto-rails-are-becoming-the-default-payment-layer-for-ai-agents-report-says)
- 補足情報: [Bitcoin News（2026-05-24）](https://news.bitcoin.com/keyrock-report-76-of-ai-agent-transactions-fall-below-visas-0-30-fee-floor/), [CryptoNews（2026-05-21）](https://cryptonews.net/news/finance/32911986/)

## 重要度
- High

## 確からしさ
- High（数値の一次ソースは Keyrock レポート全文、間接取材のみ確認済み）
