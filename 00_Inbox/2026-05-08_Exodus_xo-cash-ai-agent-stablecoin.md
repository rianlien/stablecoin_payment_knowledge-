---
title: "Exodus が XO Cash をローンチ——AI エージェント向け初のステーブルコイン、AgentKit SDK でエージェントウォレットをワンコール発行・秘密鍵をユーザーが保持"
date: 2026-05-08
source: "GlobeNewswire / CoinTelegraph / AMBCrypto"
source_url: "https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/exodus-launches-xo-cash-as-the-first-stablecoin-built-for-ai-agents.html"
entity: "Exodus Movement / MoonPay / Monavate"
category: "agentic-commerce"
tags:
  - agentic-commerce
  - stablecoin
  - wallet
  - payments
summary: "Exodus Movement が 2026 年 5 月 8 日、AI エージェント専用設計の Solana ベースステーブルコイン『XO Cash』を正式ローンチ。付属の AgentKit SDK を使えばデベロッパーは API 1 回の呼び出しでエージェントウォレットを発行でき、AI エージェントが秘密鍵を持たずに支出ルール内でユーザーの Exodus Pay 残高から自律的に支払える設計。MoonPay・Monavate と連携して Visa 加盟店でのカード決済にも対応。USDC・USDT への自動コンバージョン機能付き。"
implications: "x402（API 従量課金）・Mastercard Agentic Ready（カードレール）に続き、非カストディアル型の『エージェント専用残高管理ステーブルコイン』という第三の設計パターンが登場した。ユーザーが秘密鍵を保持しながらエージェントに支出権を委任するモデルは、消費者向けウォレットとエージェント決済の安全な架け橋として注目に値する。"
follow_up: "XO Cash の準備金構成・発行体・レギュレーション対応（GENIUS Act 枠組み）、AgentKit の支出ルール強制がスマートコントラクト層か API 層か、MoonPay Monavate カードの地理的利用可能範囲、x402/MPP との相互運用性計画"
---

## 概要

ウォレット・取引所プロバイダーの Exodus Movement が 2026 年 5 月 8 日、AI エージェント専用設計のステーブルコイン「XO Cash」を正式ローンチした。Solana ブロックチェーン上で発行され、付属の AgentKit SDK を使えばデベロッパーはワン API コールでエージェントウォレットを発行でき、AI エージェントが秘密鍵を持たずにユーザーの Exodus Pay 残高から一定ルール内で自律的に支出できる仕組みを提供する。MoonPay・Monavate（Mastercard プリンシパルメンバー）との統合で Visa 加盟店でのデビットカード決済も対応。発表日と同日に XOCash.com と AgentKit ドキュメントが公開された。

## 何が起きたか

- **ローンチ日**：2026 年 5 月 8 日
- **発行体 / 開発元**：Exodus Movement, Inc.（NASDAQ 上場、ウォレット・取引所プロダクト）
- **ブロックチェーン**：Solana
- **提携先**：MoonPay（オンランプ・流動性）、Monavate（Mastercard プリンシパルメンバー、カード発行）
- **コア設計思想**：
  - AI エージェントが秘密鍵を「保持しない（non-custodial agent）」設計
  - エージェントはユーザーの Exodus Pay 残高から「支出ルールの範囲内で」自律的に支払いを実行
  - ユーザーが秘密鍵カストディを保持したまま、AIに消費権を付与する委任モデル
- **AgentKit SDK**：
  - シングル API コールでエージェントウォレットを発行
  - 支出ルールを設定可能：1 日あたり上限、加盟店制限、1 取引あたり上限、レートリミット
  - キーはユーザー側が保持し、エージェントには支出権のみが委任される
- **対応支払いレール**：
  - Solana 上のオンチェーン決済
  - Visa 加盟店でのデビットカード決済（MoonPay + Monavate が実行）
  - USDC・USDT への自動コンバージョン
- **公開済みリソース**：XOCash.com、AgentKit 開発者ドキュメント

## なぜ重要か

### 決済事業者視点

- XO Cash は「x402 によるオンチェーン API 従量課金」「MoonAgents Card によるカードネットワーク利用」に続く第三のエージェント決済モデルを提示した。それぞれの設計思想の違いは：
  - **x402**：API/MCP サーバー向け HTTP ネイティブの USDC 従量課金（アカウント不要）
  - **MoonAgents Card**：オンチェーン残高から直接 Mastercard 加盟店決済（カード形式）
  - **XO Cash / AgentKit**：ユーザーウォレット残高への委任支出権、非カストディアル、Visa 加盟店対応
- 委任支出権モデルは消費者向けウォレット（秘密鍵保持者）とエージェント自律支出を組み合わせる点でユニーク。エンドユーザーへの信頼確保が必要な B2C 決済でのエージェント導入に特に有効な設計

### プロダクト視点

- AgentKit の「シングル API コールでエージェントウォレット発行」という開発者体験は、既存ウォレット PSP との統合コストを下げる強みがある
- 支出ルールをユーザーが設定できる点は、「エージェントが使いすぎるリスク」に対する消費者保護設計として重要な考え方。カードの支出上限と同様の UX を AI エージェントに拡張したモデル
- Exodus の既存ウォレット ユーザーベース（EXOD 株式会社、NASDAQ 上場）との相乗効果が見込める

### 規制 / リスク視点

- XO Cash は新規ステーブルコインであり、GENIUS Act（米国）の準備金・許認可要件への対応が必要。発行体・準備金構成・監督当局の詳細は現時点で不明
- 非カストディアル設計は規制対応コストを下げる可能性があるが、ユーザーがエージェントに資金を委任する構造が「マネートランスミッション」に該当するかどうかの法的解釈は未確定
- MoonPay + Monavate（Mastercard）経由のカード決済はカードネットワークの KYC/AML 要件に準拠しているが、XO Cash 自体の規制位置づけが明確化されるまでリスクが残る

## 我々への示唆

- いま検討すべきこと:
  - AgentKit の技術仕様（API エンドポイント、ウォレット発行フロー、支出ルール設定方法）を確認し、自社エージェント決済プロダクトの設計候補として評価
  - x402・MPP・AgentKit の 3 つのエージェント決済モデルを比較分析し、自社のユースケース（B2C / B2B / API 課金）に最も適合するものを選択する判断軸を整理
- 後で深掘りすべきこと:
  - XO Cash の準備金構成・発行体・GENIUS Act 対応状況（新規ステーブルコインのコンプライアンス詳細）
  - AgentKit の支出ルール強制がスマートコントラクト層（オンチェーン）か API 層（オフチェーン）かの確認（セキュリティ上の重要ポイント）
  - MoonPay + Monavate カードの地理的利用可能範囲と、MoonAgents Card（MoonPay + Monavate の別プロダクト）との差別化
- 今は優先度が低いこと:
  - USDC/USDT 自動コンバージョンの詳細（スワップコスト、スリッページ）

## 未解決の論点

- XO Cash の準備金構成・発行体は誰で、GENIUS Act 枠組みでどう位置づけられるか？
- AgentKit の支出ルール強制はスマートコントラクトベースかアプリケーション層ベースか？（セキュリティモデルに影響）
- MoonAgents Card（MoonPay, 5 月 1 日発表）との機能的差異は何か？（両者ともに MoonPay + Monavate を使用）
- XO Cash ↔ USDC/USDT 変換はどのルートで行われるか（自社 DEX / 外部 AMM / 手動リバランス）？

## 参考リンク

- 一次情報:
  - [GlobeNewswire — Exodus Launches XO Cash as the First Stablecoin Built for AI Agents（2026-05-08）](https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/exodus-launches-xo-cash-as-the-first-stablecoin-built-for-ai-agents.html)
  - [XOCash.com](https://www.xocash.com/)
- 補足情報:
  - [CoinTelegraph — Exodus launches AI agent-focused stablecoin on Solana（2026-05-08）](https://cointelegraph.com/news/exodus-launches-ai-agent-focused-stablecoin-on-solana)
  - [Let's Data Science — Exodus launches XO Cash stablecoin for AI agent payments](https://letsdatascience.com/news/exodus-launches-xo-cash-stablecoin-for-ai-agent-payments-71c45b19)
  - [AMBCrypto — Exodus launches XO Cash as AI agents become crypto's next payments battleground](https://ambcrypto.com/exodus-launches-xo-cash-as-ai-agents-become-cryptos-next-payments-battleground/)
  - [関連ノート：MoonPay MoonAgents Card（2026-05-01）](2026-05-01_MoonPay_moonagents-card-mastercard-ai-agents.md)
  - [関連ノート：AWS AgentCore Payments x402（2026-05-07）](2026-05-07_AWS_bedrock-agentcore-payments-x402.md)
  - [関連ノート：Coinbase Agentic.market × x402（2026-04-21）](2026-04-21_Coinbase-x402_agentic-market-launch.md)

## 重要度

- Medium

## 確からしさ

- High（GlobeNewswire 公式プレスリリースあり）
