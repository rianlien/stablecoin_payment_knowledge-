---
title: "Exodus、AI エージェント専用ステーブルコイン「XO Cash」と AgentKit をローンチ——MoonPay・Monavate と連携し Mastercard 加盟店決済に対応"
date: 2026-05-08
source: "GlobeNewswire / CryptoBriefing / Exodus 公式"
source_url: "https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/Exodus-Launches-XO-Cash-as-the-First-Stablecoin-Built-for-AI-Agents.html"
entity: "Exodus"
category: "agentic-commerce"
tags:
  - stablecoin
  - agentic-commerce
  - payments
  - wallet
summary: "Exodus Movement（NYSE: EXOD）は 2026 年 5 月 8 日、AI エージェント専用に設計した初のステーブルコイン「XO Cash」と、開発者向けの「AgentKit」SDK をローンチ。Solana 上で稼働し、MoonPay と Monavate（Mastercard プリンシパルメンバー）と組んで Visa・Mastercard 加盟店での直接決済に対応。エージェントは秘密鍵を保有せず Exodus Pay 残高から支出。ユーザーが日次上限・取引上限・許可加盟店・レートリミットを設定可能。決済時は自動的に USDC または USDT に変換し、手数料ゼロで実行される。"
implications: "Exodus は AI エージェントが「秘密鍵不要・ユーザー設定の支出ルール付き」でステーブルコイン決済を行う実用モデルを具体化した。MoonAgents Card（MoonPay、5 月 1 日発表）と同じ技術スタック（MoonPay + Monavate）を採用しており、AI エージェントの Mastercard 加盟店決済インフラが収束しつつある。"
follow_up: "AgentKit の API 仕様と統合コスト、XO Cash の米国以外への展開タイムライン、USDC/USDT 自動変換のネット決済フローとガスコスト負担、MoonAgents Card との機能差異"
---

## 概要

暗号資産ウォレット企業の Exodus Movement（NYSE: EXOD）が 2026 年 5 月 8 日、AI エージェントを第一の想定ユーザーとして設計したステーブルコイン「XO Cash」と、エージェント向けウォレット発行ツール「AgentKit」を GlobeNewswire 公式プレスリリースで発表・ローンチした。Solana 上で稼働し、MoonPay と Monavate（Mastercard プリンシパルメンバー）との連携により Visa・Mastercard 対応加盟店での決済が可能。

## 何が起きたか

**XO Cash の基本設計**
- チェーン：Solana（65,000 TPS、手数料ゼロ台）
- 目的：AI エージェントが人間の介入なしに自律的に決済するための専用ステーブルコイン
- 決済時変換：XO Cash で支払いを指示すると USDC または USDT に自動変換——加盟店はステーブルコインの種類を意識しない
- 取引手数料：ゼロ

**セキュリティ設計**
- エージェントは秘密鍵を保有・管理しない
- Exodus Pay 残高からエージェントが直接支出する設計（エージェントは「支出権限」のみを持つ）
- ユーザーが以下のルールをいつでも更新可能：
  - 日次支出上限（daily limit）
  - 1 取引あたりの上限（per-transaction cap）
  - 許可加盟店リスト（allowed merchants）
  - レートリミット（rate limits）

**AgentKit（開発者向け SDK）**
- 単一の API コールでエージェントにウォレットを発行
- 開発者は既存のエージェントフレームワークに XO Cash 決済を追加統合可能
- 高頻度・自動化された決済（マイクロペイメント・API 従量課金等）に最適化

**加盟店接続インフラ**
- パートナー：MoonPay（インフラ統合）+ Monavate（Mastercard プリンシパルメンバー、リアルタイム清算）
- Monavate がオンチェーン残高の充当とカード承認をリアルタイムで実行
- Visa・Mastercard の全加盟店での利用が可能
- 非カストディアル設計（エージェントも中間業者も資産を保管しない）

**類似製品との比較**
- MoonPay「MoonAgents Card」（5 月 1 日発表）と同じ MoonPay + Monavate スタックを採用
- 違い：XO Cash は Exodus エコシステム経由・AgentKit SDK 付き。MoonAgents Card は MoonPay ダイレクトプロダクト

## なぜ重要か

### 決済事業者視点
- AI エージェントによる「Mastercard/Visa 加盟店での直接支払い」インフラが MoonPay + Monavate スタックで具体化した。PSP はエージェント決済を受け入れる際にどの認証・照合プロセスを変更する必要があるかを検討するタイミング
- AgentKit の API でエージェント向けウォレット発行が簡素化される——PSP がエージェント決済機能を自社プロダクトに追加する際の統合コストが下がる

### 加盟店視点
- 加盟店側は通常の Mastercard/Visa 決済として処理できる。エージェントが「誰の」代理で決済しているかの照合（KYC/AML）をどう行うかは未解決

### プロダクト視点
- 「秘密鍵をエージェントに持たせない・ユーザー設定のスペンドルール付き」というセキュリティ設計は、エージェント決済における守衛モデル（guardian model）の参照設計として機能する
- AgentKit という SDK の存在は、エージェント決済インフラが「パッケージ化 → 普及」の段階に移ったことを示す

### 規制 / リスク視点
- エージェントが自律的に Mastercard/Visa 加盟店で決済する場合の AML・OFAC スクリーニング責任主体は未明確（エージェント発行者 Exodus か、Monavate か、MoonPay か）
- 非カストディアル設計は規制上の「資金保管」義務を回避するための設計と見られるが、当局の解釈次第で MTL（送金業免許）要件が発生しうる

## 我々への示唆

- いま検討すべきこと:
  - AgentKit の API ドキュメントを確認し、自社エージェント決済プロダクトへの統合可能性・コストを技術評価
  - MoonAgents Card（MoonPay）と XO Cash（Exodus）の機能・コスト・規制面の差異を比較し、自社でエージェント向けカード発行機能を追加する際の最短経路を特定
- 後で深掘りすべきこと:
  - XO Cash × USDC/USDT 自動変換のネット清算フロー（Monavate の清算タイミング・ガスコスト負担構造）
  - エージェント決済における KYC/AML 責任の所在——Exodus・MoonPay・Monavate それぞれの役割分担
- 今は優先度が低いこと:
  - XO Cash の投資・保有目的での評価（決済ツールとして設計されており、保有ユーティリティは限定的）

## 未解決の論点

- XO Cash の米国以外での展開タイムライン（英国・EU・LATAM・アジア）
- AgentKit の月次利用コスト・API レートリミット
- エージェントが「許可加盟店リスト」以外の加盟店で誤決済しようとした場合の挙動
- USDC/USDT への自動変換レート・スプレッドの仕組み

## 参考リンク

- 一次情報: [GlobeNewswire 公式プレスリリース（2026-05-08）](https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/Exodus-Launches-XO-Cash-as-the-First-Stablecoin-Built-for-AI-Agents.html)
- 補足情報: [CryptoBriefing（2026-05-08）](https://cryptobriefing.com/exodus-xo-cash-stablecoin-ai-agents-solana/)
- 補足情報: [blockchain.news](https://blockchain.news/news/exodus-xo-cash-stablecoin-ai-payments-solana)
- 関連ノート: [MoonPay MoonAgents Card（2026-05-01）](./2026-05-01_MoonPay_moonagents-card-mastercard-ai-agents.md)
- 関連ノート: [AWS Bedrock AgentCore Payments × x402（2026-05-07）](./2026-05-07_AWS_bedrock-agentcore-payments-x402.md)
- 関連ノート: [ERC-8183 Agentic Commerce](../04_Protocols/ERC-8183_Agentic-Commerce.md)

## 重要度
- High

## 確からしさ
- High（GlobeNewswire 公式プレスリリース・複数メディア報道による）
