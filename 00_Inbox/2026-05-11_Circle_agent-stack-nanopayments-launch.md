---
title: "Circle、Agent Stack を正式ローンチ——Agent Wallets・Nanopayments（$0.000001 USDC、ガスゼロ）・Agent Marketplace を即日提供。USDC が機械間決済の基軸インフラへ"
date: 2026-05-11
source: "BusinessWire / Circle Press Room / Blockhead / PYMNTS"
source_url: "https://www.businesswire.com/news/home/20260511078086/en/Circle-Launches-AI-Infrastructure-to-Power-the-Agentic-Economy"
entity: "Circle Internet Group"
category: "agent-payments-infrastructure"
primary_category: "agentic-commerce"
article_published_date: 2026-05-11
underlying_event_date: 2026-05-11
primary_source_date: 2026-05-11
tags:
  - agent-payments
  - USDC
  - nanopayments
  - Circle
  - agentic-commerce
summary: "Circle が agents.circle.com で Agent Stack を正式ローンチ。Agent Wallets・Nanopayments（Circle Gateway）・Agent Marketplace・Circle CLI の 4 製品を即日提供。Nanopayments はガスゼロで $0.000001 USDC から送金可能な機械間高頻度決済プロトコル。"
implications: "USDC が AI エージェントの支払い基盤として Circle 自ら位置づけ。エージェントウォレット・ナノ決済・サービス発見マーケットプレイスが一体提供されることで、エージェント決済スタックのデファクト競争が本格化。"
importance: High
confidence: High
follow_up: "Arc ブロックチェーンの詳細仕様、$222M ARC トークンプレセールの用途と Circle の事業モデルへの影響、Agent Marketplace に登録されるサービスの種類と x402 / MCP との統合状況"
---

## 概要

2026 年 5 月 11 日、Circle Internet Group が **Circle Agent Stack** を正式ローンチした。AI エージェントが自律的に資金を保有・送受信・管理し、サービスを発見・購入できるインフラスイートで、`agents.circle.com` から即日利用可能。USDC 流通量は $77B、オンチェーン取引量は年率 $21.5T に達した段階での発表。

## 何が起きたか

- **Agent Wallets**：エージェントが USDC・ERC-20 トークンを自律保有・送受信できるポリシー制御ウォレット。パーミッションレスかつ支出上限設定可能
- **Nanopayments（Circle Gateway）**：ガスゼロで $0.000001 USDC から送金できる新プロトコル。高頻度・サブセント・機械間決済フロー向け設計
- **Agent Marketplace**：人間・AI エージェントが共にエージェント系サービスを発見・評価・統合できるキュレーテッドディレクトリ。エージェントがプログラマティックにサービスを発見し対価を支払う
- **Circle CLI**：エージェントが精密コマンドで金融アクションを実行できるコマンドラインインターフェース
- 同週、Circle は Arc ブロックチェーンを発表し、ARC トークンプレセールで $222M を調達

## 確認された事実

- 発表日：2026 年 5 月 11 日（BusinessWire 公式プレスリリース）
- agents.circle.com で即日提供開始（ローンチ確認済み）
- Nanopayments の最小送金単位：$0.000001 USDC、ガスゼロ
- CEO Jeremy Allaire 発言：「金融インフラは歴史的に人間向けに構築されてきた。エージェント自身が経済主体として参加できる環境を作る」
- USDC 流通量 $77B・オンチェーン取引量年率 $21.5T（2026 年 5 月時点）

## なぜ重要か

### 決済事業者視点

- USDC 発行体の Circle が自らエージェントウォレット・ナノ決済・マーケットプレイスを提供することで、エージェント決済の標準スタック競争が本格化する。PSP は Circle の API と AWS AgentCore / Coinbase x402 など複数スタックのどれを軸に据えるかの判断を迫られる
- Nanopayments の「$0.000001」設計は従来の決済手数料モデル（最低 $0.03 前後）と根本的に異なる。サブセント課金モデルが PSP のビジネス設計を変える可能性がある

### 加盟店視点

- Agent Marketplace は加盟店・API プロバイダーが「エージェントに発見される」チャネルとして機能する。カタログ整備・機械読取メタデータを持つ加盟店への流入が増える
- x402 と組み合わせると HTTP レベルの自動決済が加盟店側でも実装可能になる

### プロダクト視点

- Agent Wallets のポリシー制御（支出上限・承認フロー）はユーザーがエージェントに「権限委任」する際の信頼設計の雛形になりうる
- Nanopayments は API 課金・AI トークン消費課金（Stripe × Tempo の流量課金と同方向）のインフラとして機能する可能性がある

### 規制 / リスク視点

- GENIUS Act 施行後（2027 年 1 月以降）の環境では、Circle の Agent Wallets がどの規制カテゴリに分類されるかが焦点。エージェントへの USDC 残高委託が「カストディ」に該当するかどうか
- ARC トークンプレセール $222M の性質（証券 / ユーティリティ）は CLARITY Act の市場構造規制対象になる可能性がある

## 我々への示唆

- いま検討すべきこと:
  - agents.circle.com の Agent Wallets API を実際に試し、既存エージェント決済フロー（MoonPay AgentKit・Exodus AgentKit 等）との比較評価を行う
  - Nanopayments の $0.000001 設計が API 課金・サブセント決済ユースケースに適用できるか確認する
- 後で深掘りすべきこと:
  - Agent Marketplace への登録プロセスとメタデータ要件——加盟店・API プロバイダーとしての対応可否
  - Arc ブロックチェーンと USDC の関係——Circle の技術スタック全体における Arc の位置づけ
- 今は優先度が低いこと:
  - ARC トークンの投資判断（Circle の決済事業への直接影響は不明）

## ありそうな示唆

- Circle が Agent Stack を提供することで、「USDC でエージェント決済 = Circle インフラ」というデファクト化が進む可能性がある。Stripe・Coinbase・AWS が類似インフラを構築中であり、今後 6〜12 か月でエージェント決済スタックのコモディティ化が起きると推測される
- Nanopayments の最小単位 $0.000001 は AI トークン単位での課金（GPT-4o 換算で約 $0.000003/token）とほぼ同スケール——AI API コストのパス・スルーが USDC 建てでリアルタイム決済できる設計になる

## 推測 / 監視ポイント

- x402 と Circle Nanopayments の関係：x402 の決済レールとして Circle Gateway が採用されるか
- AWS AgentCore Payments（既報：2026-05-07）・WSPN W Agent との差別化軸
- Agent Marketplace に登録されるエンタープライズ向けサービスの種類（B2B API 課金が主か、消費者向けが主か）

## 未解決の論点

- Nanopayments は EVM 上の独自プロトコルか、USDC の転送レイヤー改修か（技術実装の詳細が不明）
- ARC ブロックチェーンの合意機能・チェーン ID・既存 Circle CCTP との関係

## 参考リンク

- 一次情報: [BusinessWire プレスリリース（2026-05-11）](https://www.businesswire.com/news/home/20260511078086/en/Circle-Launches-AI-Infrastructure-to-Power-the-Agentic-Economy)
- 補足情報: [Circle 公式ブログ](https://www.circle.com/blog/introducing-circle-agent-stack-financial-infrastructure-for-the-agentic-economy) / [Blockhead（2026-05-12）](https://www.blockhead.co/2026/05/12/circle-launches-agent-stack-to-put-usdc-at-the-centre-of-machine-to-machine-payments) / [PYMNTS](https://www.pymnts.com/earnings/2026/circle-chases-agentic-growth-scale-stablecoin-infrastructure/)

## 重要度

- High

## 確からしさ

- High（BusinessWire 公式プレスリリース + 複数メディア確認）
