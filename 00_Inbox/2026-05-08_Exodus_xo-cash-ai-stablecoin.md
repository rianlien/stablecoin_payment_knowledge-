---
title: "Exodus、AI エージェント専用ステーブルコイン「XO Cash」を Solana でローンチ——AgentKit SDK で Visa 加盟店支払いも可能に"
date: 2026-05-08
source: "GlobeNewswire / Decrypt / Crypto Briefing"
source_url: https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/Exodus-Launches-XO-Cash-as-the-First-Stablecoin-Built-for-AI-Agents.html
entity: Exodus
category: agentic-commerce
tags:
  - stablecoin
  - agentic-commerce
  - wallet
  - payments
summary: "Exodus Movement（NYSE: EXOD）が 2026 年 5 月 8 日、AI エージェント専用ステーブルコイン「XO Cash」を Solana 上で正式ローンチ。MoonPay・Monavate と組み、エージェントが XO Cash 残高から USDC/USDT に自動変換してオンチェーン API 決済・Visa 加盟店カード決済の両方を手数料ゼロで実行できる。AgentKit SDK により 1 回の API 呼び出しでエージェントウォレットの発行と Visa デビットカードの発行が可能。"
implications: "MoonAgents Card（MoonPay × Monavate）と同一インフラを使いながら、Exodus ブランドの AI 専用ステーブルコインとして差別化。エージェント向け「専用通貨」の登場は、USDC など汎用ステーブルコインとの棲み分けや相互変換が常態化することを示す。"
follow_up: "XO Cash の実取引量・エージェント採用状況、MoonAgents Card との機能差（非カストディアル設計の違い）、XO Cash の USDC/USDT 変換レートと手数料、他エージェントフレームワーク（LangChain・CrewAI 等）との統合状況"
---

## 概要

Exodus Movement, Inc.（NYSE American: EXOD）が 2026 年 5 月 8 日、AI エージェントを対象に設計したステーブルコイン **XO Cash** を Solana 上でローンチ。同日、エージェント向け開発者ツールキット **AgentKit SDK** も公開した。

- **ブロックチェーン**：Solana
- **インフラパートナー**：MoonPay（決済インフラ）、Monavate（Mastercard プリンシパルメンバー→今回は Visa ネットワーク対応）
- **想定ユーザー**：開発者が AI エージェントに XO Cash ウォレットを発行し、エージェントが自律的に決済を実行
- **自動変換**：支払い先が USDC/USDT を要求する場合、XO Cash から自動変換（手数料ゼロ）

## 何が起きたか

- **AgentKit SDK**：API 1 回の呼び出しでエージェント専用ウォレットを発行。エージェントは秘密鍵を保持せず、Exodus Pay 残高から支出
- **Visa デビットカード発行**：同 API でエージェント専用 Visa デビットカードを発行可能。Monavate 経由で任意の Visa 加盟店での決済に対応
- **支出制限**：1 日の上限・1 回の上限・許可加盟店・レート制限などをユーザーが設定し、随時変更可能
- **変換フロー**：エージェントが XO Cash を保持し、USDC/USDT を要求するサービスに支払う際は単一トランザクションで自動変換
- **MoonAgents Card との関係**：同一の MoonPay × Monavate インフラを使うが、XO Cash は Exodus ブランドの専用通貨として独自のウォレット体系を持つ

## なぜ重要か

### 決済事業者視点

- エージェント向け「専用ステーブルコイン」の登場は、汎用 USDC/USDT に加えて、特定エコシステム内でのブランド付きステーブルコインが乱立するリスクを示す。PSP は複数のエージェント向けステーブルコインを受け入れるか、USDC 自動変換を前提とした設計が必要になりうる
- Monavate 経由で Visa ネットワークを利用することで、x402（オンチェーン API 課金）・MoonAgents Card（Mastercard 加盟店）に加えて、Visa 加盟店での自律決済の第三のルートが整った

### 加盟店視点

- エージェントが Visa 加盟店でのリアルタイム決済を実行できるため、既存の POS インフラへの追加設定不要で AI エージェントからの購買が発生しうる
- XO Cash はオンチェーンのため、加盟店決済前後のオンチェーン履歴が完全に追跡可能

### プロダクト視点

- AgentKit SDK の設計——「1 API 呼び出しでウォレット発行 + カード発行」——は、エージェント向け決済機能の実装コストを極限まで下げる。PSP・PayFac がエージェント向けサブウォレット機能を提供する際の参照アーキテクチャになりうる
- エージェントが秘密鍵を持たない設計はセキュリティリスクを低減するが、親ウォレット（Exodus Pay）への依存が生じる

### 規制 / リスク視点

- AI エージェントが自律的に Visa 決済を実行する際の AML 監視・KYT フローは未明。エージェントの支出限度・加盟店制限はウォレット設定で管理するが、規制機関の監督対象は発行体（Exodus/Monavate）か、エージェントオーナー（開発者）か、論点として残る
- GENIUS Act の PPSI 要件に XO Cash がどう位置付けられるか（USDC/USDT への自動変換ステーブルコインの規制分類）は今後の論点

## 我々への示唆

- いま検討すべきこと:
  - AgentKit SDK の API 仕様を確認し、自社エージェント決済プロダクトへの組み込み可否を検討
  - XO Cash（Exodus エコシステム）・MoonAgents Card（MoonPay）・AgentCore Payments（AWS/Coinbase）の 3 者の技術スタックを比較し、自社が統合する優先順位を整理
- 後で深掘りすべきこと:
  - XO Cash の実採用事例・取引量データが公開されたタイミングで評価
  - Visa vs Mastercard ネットワークの使い分け（MoonAgents Card は Mastercard、XO Cash は Visa）が市場でどう機能するか
- 今は優先度が低いこと:
  - Exodus（EXOD）の株式投資的な観点（ビジネス評価には関係するが直接のプロダクト統合決定要因ではない）

## 未解決の論点

- XO Cash が「ステーブルコイン」として GENIUS Act 上どう規制されるか（USDC/USDT に自動変換するラッパーとしての法的性格）
- Monavate が MoonAgents Card（Mastercard）と XO Cash（Visa）の両方をサポートする技術的な整合性
- エージェントの Visa 決済が 3DS・強い顧客認証（SCA）の対象になるかどうか
- XO Cash の流動性（USDC との交換レート・スリッページ・時間帯別の可用性）

## 参考リンク

- 一次情報:
  - [GlobeNewswire 公式プレスリリース（2026-05-08）](https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/Exodus-Launches-XO-Cash-as-the-First-Stablecoin-Built-for-AI-Agents.html)
- 補足情報:
  - [Decrypt（2026-05-08）](https://decrypt.co/366677/western-union-usdpt-stablecoin-solana-anchorage-digital)
  - [Crypto Briefing（2026-05-08）](https://cryptobriefing.com/exodus-xo-cash-stablecoin-ai-agents-solana/)
  - [gncrypto.news - XO Cash SDK 解説（2026-05-08）](https://www.gncrypto.news/news/exodus-xo-cash-sdk-solana-ai-visa-payments/)
  - [関連ノート: MoonPay MoonAgents Card（2026-05-01）](./2026-05-01_MoonPay_moonagents-card-mastercard-ai-agents.md)
  - [関連ノート: AWS AgentCore Payments x402（2026-05-07）](./2026-05-07_AWS_bedrock-agentcore-payments-x402.md)

## 重要度

- Medium

## 確からしさ

- High（GlobeNewswire 公式プレスリリースに基づく）
