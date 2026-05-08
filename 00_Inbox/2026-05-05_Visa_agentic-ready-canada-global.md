---
title: "Visa Agentic Ready、カナダ主要 5 行に展開——TAP（Trusted Agent Protocol）ベースのエージェント決済テストインフラが北米本格化"
date: 2026-05-05
source: "Visa / GlobeNewswire / PYMNTS"
source_url: "https://www.globenewswire.com/news-release/2026/05/05/3287953/0/en/Visa-Expands-Agentic-Ready-Program-to-Canada-to-Advance-AI-Driven-Commerce.html"
entity: "Visa"
category: "agentic-commerce"
tags:
  - agentic-commerce
  - payments
  - psp
  - merchant
article_published_date: 2026-05-05
underlying_event_date: 2026-05-05
primary_source_date: 2026-05-05
summary: "Visa が 2026 年 5 月 5 日、AI エージェント決済テストプログラム「Visa Agentic Ready」をカナダに拡大。BMO・CIBC・RBC・Scotiabank・TD の主要 5 行が早期参加イシュアーとして参画。同日、Visa Canada × Wealthsimple が USDC ステーブルコイン清算パイロットも開始。Agentic Ready は現時点で米国・英国・欧州・LATAM・アジア太平洋（4 月 30 日ローンチ、50 社超）・カナダの 6 地域で稼働する。"
implications: "カードネットワークが発行銀行に対してエージェント発動決済の本番相当環境でのテストインフラを提供し始めた。TAP（Trusted Agent Protocol）の採用が主要国 G7 規模に拡大したことで、PSP・加盟店の「エージェント対応」が技術的義務に近い位置づけになりつつある。"
follow_up: "各地域の Agentic Ready 参加イシュア数・テスト取引量の公開、TAP 仕様のオープン化・相互運用性確認、AP2（FIDO Alliance）との統合計画、カナダでの USDC 清算パイロット（Wealthsimple）の拡張スケジュール"
---

## 概要

Visa は 2026 年 5 月 5 日、グローバルプログラム「Visa Agentic Ready」をカナダに展開した。カナダの早期参加イシュアーには BMO・CIBC・RBC・Scotiabank・TD の主要 5 行が名を連ねる。同日、Visa Canada と Wealthsimple が USDC ステーブルコイン清算パイロットも発表し、カナダにおけるエージェント決済・ステーブルコイン清算の両面が同時に整備される形となった。

Agentic Ready は現在、米国・英国・欧州・LATAM・アジア太平洋（2026-04-30 ローンチ、10 市場・50 社超）・カナダで稼働しており、グローバルな AI エージェント決済テストインフラとして機能している。

## 何が起きたか

**Visa Agentic Ready カナダ展開（2026-05-05）**

- **発表日**：2026 年 5 月 5 日（GlobeNewswire プレスリリース）
- **参加イシュア**：BMO、CIBC、RBC、Scotiabank、TD（カナダ最大手 5 行）
- **プログラムの内容**：
  - AI エージェントが発動した決済を、実際のカード・実在の加盟店を用いた管理環境でテスト
  - カード登録・トークン化・認証・取引承認の各フローを検証
  - エージェントが消費者・企業に代わって行動する場合の信頼・セキュリティ・制御機構を評価
  - 本番スケール前の運用上のギャップを特定
  - Visa・加盟店とともに、エージェント発動取引の実際の挙動を理解する協働環境を提供

- **プログラムの技術基盤**：Visa TAP（Trusted Agent Protocol）
  - エージェントの出所・正当性を暗号学的にリアルタイム検証
  - 署名付き HTTP メッセージでエージェントの意図・検証済みユーザー ID・支払い情報を送信
  - 既存のウェブインフラ上で動作するオープンフレームワーク
  - 正規エージェントと悪意のあるボットを区別する信頼レイヤーとして機能

- **グローバル展開状況**：
  - 先行：英国・欧州（20 社超）→ 米国 → LATAM・アジア太平洋（2026-04-30、50 社超、10 市場）→ カナダ（2026-05-05）
  - 今後も追加市場への展開予定

**Visa Canada × Wealthsimple USDC 清算パイロット（同日、2026-05-05）**

- Visa Canada と Wealthsimple（カナダの最大手フィンテック、AUM 1,000 億カナダドル）が USDC ステーブルコインでの清算義務履行パイロットを同日に開始
- Wealthsimple が特定の Visa Canada 向け清算義務を USDC で決済できる
- 24 時間 365 日対応・7 日間清算・流動性管理効率化が主要メリット
- Visa のグローバルステーブルコイン清算量（年率 70 億ドル）のカナダへの拡張として位置付け

## なぜ重要か

### 決済事業者視点

- カナダの G7 主要国システム上位 5 行が Agentic Ready に参加したことで、エージェント発動決済の「発行銀行による実環境テスト」が先進国金融機関の標準的プロセスになりつつある。PSP・PayFac は発行銀行のエージェント対応完了を前提としたプロダクト設計に移れる段階が近づいている
- Visa TAP が主要地域の発行銀行に普及することで、PSP 側に「TAP 対応エージェントからの取引のみ受け入れる」設定を実装できる環境が整う。TAP 未対応エージェントは拒否・リスク評価の対象になる可能性がある

### 加盟店視点

- Visa カードを受け入れる加盟店は間接的に、TAP 認証済み AI エージェントからの決済を受け入れることができる環境に移行しつつある
- エージェント発動取引に対するチャージバック・紛争・返金のフローが発行銀行のテスト環境で検証されることで、加盟店リスクの実態が明らかになっていく

### プロダクト視点

- Visa TAP と Google AP2（FIDO Alliance 寄贈、2026-04-28）・x402（Linux Foundation）の三者の役割分担が鮮明になりつつある：
  - **x402**：HTTP 402 ベースの USDC マイクロ決済（API・MCP サーバー等）
  - **AP2（FIDO Alliance）**：エージェント認証・認可・ Verifiable Intent の国際標準化
  - **Visa TAP**：既存カードレールにおけるエージェント発動取引の信頼検証
- エージェント決済プロダクトを設計する場合、「オンチェーン USDC（x402/AP2）」と「オフチェーン Visa/Mastercard（TAP）」の両方への対応が事実上必要になる可能性がある

### 規制 / リスク視点

- 主要 G7 金融機関がエージェント決済テストに参加することで、規制当局（カナダ金融機関監督庁 OSFI 等）のエージェント決済に関する監督指針策定が加速する可能性がある
- Visa Agentic Ready のテスト環境で特定された「運用上のギャップ（operational gaps）」が AML・KYC 規制と関連する可能性が高く、発行銀行が見つけた問題点が業界標準ガイドラインの素材になりうる

## 我々への示唆

- いま検討すべきこと:
  - Visa TAP の仕様（GitHub: visa/trusted-agent-protocol）を確認し、自社エージェントが TAP 認証済みとして識別される実装計画を立案する
  - カナダ市場向けに「Agentic Ready 参加発行銀行との取引が発生した場合」のエージェント決済フロー設計を検討する
- 後で深掘りすべきこと:
  - TAP と AP2（FIDO Alliance）の技術的統合ロードマップ（両者は補完的か、重複しているか）
  - Agentic Ready のテスト環境で検出された課題・修正事例（Visa が公開した場合）
  - カナダ USDC 清算パイロット（Wealthsimple）の拡張スケジュールとエージェント決済との連携可能性
- 今は優先度が低いこと:
  - 各地域の Agentic Ready 参加数の詳細カウント（全体像が明らかになってから評価）

## 未解決の論点

- Visa TAP と AP2（FIDO Alliance）・x402 は技術的に統合できるか？三者のどのレイヤーが標準化されるか？
- Agentic Ready の「管理された本番相当環境」でのテスト結果は外部に公開されるか？
- TAP 未対応エージェントからの決済は発行銀行によって自動拒否される設計になるか？
- カナダ OSFI（金融機関監督庁）はエージェント発動取引に独自の監督要件を設けるか？

## 参考リンク

- 一次情報:
  - [GlobeNewswire — Visa Expands Agentic Ready Program to Canada（2026-05-05）](https://www.globenewswire.com/news-release/2026/05/05/3287953/0/en/Visa-Expands-Agentic-Ready-Program-to-Canada-to-Advance-AI-Driven-Commerce.html)
  - [Visa ニュースルーム — Global Expansion of Agentic Ready Program](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22341.html)
  - [GlobeNewswire — Visa Canada × Wealthsimple USDC Settlement Pilot（2026-05-05）](https://www.globenewswire.com/news-release/2026/05/05/3287937/0/en/visa-canada-and-wealthsimple-pilot-stablecoin-settlement-in-canada.html)
  - [GitHub — Visa Trusted Agent Protocol（TAP）仕様](https://github.com/visa/trusted-agent-protocol)
- 補足情報:
  - [PYMNTS — Visa Expands Agentic Ready Program to LatAm and Asia](https://www.pymnts.com/visa/2026/visa-expands-agentic-ready-program-to-latam-and-asia/)
  - [Fintech.ca — Visa Launches Agentic Ready, Taps Wealthsimple for Stablecoin Pilot](https://www.fintech.ca/2026/05/06/visa-launches-agentic-ready-wealthsimple-stablecoin-pilot/)
  - [BNN Bloomberg — Visa Canada and Wealthsimple Pilot Stablecoin Settlement](https://www.bnnbloomberg.ca/press-releases/2026/05/05/visa-canada-and-wealthsimple-pilot-stablecoin-settlement-in-canada/)
  - [関連ノート：Google AP2 FIDO Alliance 寄贈（2026-04-28）](2026-04-28_Google_ap2-fido-alliance.md)
  - [関連ノート：Visa ステーブルコイン清算 9 チェーン（2026-04-29）](2026-04-29_Visa_stablecoin-settlement-9chains-7b.md)
  - [関連ノート：x402 Foundation Linux Foundation 移管（2026-04-02）](2026-04-02_x402-Foundation_linux-foundation-launch.md)

## 重要度

- Medium

## 確からしさ

- High（GlobeNewswire 公式プレスリリース、Visa ニュースルーム、複数メディア一致）
