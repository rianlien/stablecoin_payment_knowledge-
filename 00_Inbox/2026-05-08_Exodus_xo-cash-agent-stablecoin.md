---
title: "Exodus が AI エージェント専用ステーブルコイン「XO Cash」と AgentKit SDK をローンチ"
date: 2026-05-08
source: "GlobeNewswire / Bitcoin Magazine / The Block"
source_url: "https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/Exodus-Launches-XO-Cash-as-the-First-Stablecoin-Built-for-AI-Agents.html"
entity: "Exodus Movement / MoonPay / Monavate"
category: "agentic-commerce"
tags:
  - agentic-commerce
  - payments
  - wallet
  - stablecoin
summary: "Exodus Movement（NYSE: EXOD）が 2026 年 5 月 8 日、AI エージェント専用ステーブルコイン「XO Cash」と開発者向け SDK「AgentKit」を正式ローンチ。エージェントは秘密鍵を保持せずに Exodus Pay 残高から MoonPay・Monavate 基盤の Visa 加盟店向けデビットカードで支払いを実行。ユーザーが上限・加盟店ホワイトリスト等の支出ルールを設定し、決済時に USDC/USDT に自動変換する。"
implications: "エージェント向けの「鍵なし決済 + 規則付きカード」モデルが Solana 上で実用化された。MoonAgents Card（MoonPay/Monavate）と同じインフラ上に構築されており、エージェント用デビットカードが汎用インフラ化しつつある。"
follow_up: "XO Cash の発行体・準備金構造・規制認可状況、米国展開における MSB 登録対応、AgentKit と他エージェントフレームワーク（LangChain・CrewAI 等）との連携状況"
---

## 概要

Exodus Movement, Inc.（NYSE American: EXOD）が 2026 年 5 月 8 日、AI エージェント向けステーブルコイン「XO Cash」と開発者向け SDK「AgentKit」を正式ローンチした。Solana ブロックチェーン上で稼働し、MoonPay・Monavate との連携でエージェントが Visa 加盟店でリアルタイム決済できるデビットカードも提供する。エージェントは秘密鍵を自身で管理せず、ユーザーが設定した支出ルールの範囲内で自律的に決済を実行できる。

## 何が起きたか

- **発表日**：2026 年 5 月 8 日（GlobeNewswire 公式プレスリリース）
- **underlying_event_date**：2026-05-08
- **article_published_date**：2026-05-08
- **発行元**：Exodus Movement, Inc.（NYSE American: EXOD）
- **ブロックチェーン**：Solana
- **インフラパートナー**：MoonPay（ウォレット・カードインフラ）/ Monavate（Mastercard プリンシパルメンバー、カード発行）

### XO Cash の主な仕様

- エージェントは秘密鍵を保持せず、オーナーの Exodus Pay 残高から支出する（非カストディアル設計のまま、エージェントへの鍵露出を回避）
- 決済時に USDC または USDT へ自動変換（ガス・取引手数料なし）
- ユーザーが設定可能な支出ルール：
  - 1 日あたりの上限額
  - トランザクションあたりの上限
  - 許可加盟店のホワイトリスト
  - レートリミット（頻度制限）
  - ルールはいつでも更新可能

### AgentKit SDK

- API 1 回の呼び出しでエージェント専用ウォレットを作成
- エージェントウォレットから API 1 回でデビットカードを発行
- カードは Visa 加盟店全般で利用可能
- ウォレットに設定した支出ルールがカード決済にも自動適用
- Exodus Pay と同じカードインフラ（MoonPay + Monavate）を共用

## なぜ重要か

### 決済事業者視点

- MoonPay・Monavate が構築した「オンチェーン資金 → リアルタイム Visa カード決済」インフラが Exodus にも提供されており、同一アーキテクチャが MoonAgents Card（MoonPay 直接提供）・XO Cash（Exodus 経由）の 2 サービスとして展開されている。エージェント向けデビットカードが汎用プラットフォーム化しつつある
- ゼロ手数料モデルは大量・高頻度なエージェント決済（API コール単位等）に最適化されている

### 加盟店視点

- 既存の Visa 決済インフラで対応可能であり、加盟店側が特別な対応をしなくても AI エージェントからの購入を受け入れられる
- 一方で機械読み取り可能なカタログ・API 化がなければエージェントは商品を発見できず、到達範囲は限られる

### プロダクト視点

- 「エージェントが鍵を持たず支出ルールで制約される」設計は、ユーザーの委任意図（delegated intent）を明示的に表現するアーキテクチャとして有望。PSP が承認条件をインフラ層で強制するモデルの具体例
- AgentKit の「シングル API コール」設計は開発者フリクションを最小化し、エージェント向けウォレット・カード発行の参入障壁を大幅に下げる

### 規制 / リスク視点

- XO Cash の発行体・準備金構造・規制認可状況が不明。Exodus がマネー・トランスミッター登録等の必要な許認可を取得しているかの確認が必要
- ユーザー設定の支出ルールによる制御は実効性の高い消費者保護手段だが、ルール外の取引が発生した場合の責任分界が不明

## 我々への示唆

- いま検討すべきこと:
  - MoonPay + Monavate インフラが「エージェント用デビットカードの白ラベル基盤」として他社にも提供されているか確認し、同様の仕組みを自社プロダクトに組み込む検討を始める
  - XO Cash・MoonAgents Card・Oobit Agent Cards（Visa）の 3 モデルを比較し、エージェント向けカード決済の設計標準として整理する
- 後で深掘りすべきこと:
  - XO Cash の発行体ライセンス・準備金の透明性（発行保証構造）
  - AgentKit の対応エージェントフレームワーク（LangChain・CrewAI・OpenAI Assistants 等）と、x402 との統合可能性
  - Monavate の Mastercard プリンシパルメンバー資格がカード発行コスト・ルールにどう影響するか
- 今は優先度が低いこと:
  - Exodus 自体の取引所・ウォレット事業との連携詳細（今回の論点外）

## 未解決の論点

- XO Cash は誰が発行しているか？Exodus 自身か、パートナー経由か？準備金管理はどのエンティティが行うか？
- 米国での MSB（送金業者）登録・州別マネー・トランスミッター免許の状況は？
- AgentKit は x402 プロトコルと統合可能か？API 課金（Pay.sh・AgentCore）との組み合わせは想定されているか？
- エージェントのカード利用に対して、Visa の不正検知システムはどう反応するか（AI エージェント特有の使用パターンへの適応）？

## 参考リンク

- 一次情報:
  - [GlobeNewswire — Exodus Launches XO Cash as the First Stablecoin Built for AI Agents（2026-05-08）](https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/Exodus-Launches-XO-Cash-as-the-First-Stablecoin-Built-for-AI-Agents.html)
  - [Trust Wallet Agent Kit ブログ（参考）](https://trustwallet.com/blog/announcements/introducing-the-trust-wallet-agent-kit-twak-your-ai-agent-can-now-act-on-crypto)
- 補足情報:
  - [Bitcoin Magazine — Exodus Launches Agent Kit](https://bitcoinmagazine.com/news/trust-wallet-launches-agent-kit)
  - [関連ノート：MoonPay MoonAgents Card Mastercard AI エージェント（2026-05-01）](2026-05-01_MoonPay_moonagents-card-mastercard-ai-agents.md)
  - [関連ノート：Oobit Agent Cards USDT Visa（2026-04-30）](2026-04-30_Oobit_agent-cards-usdt-visa.md)

## 重要度

- High

## 確からしさ

- High（GlobeNewswire 公式プレスリリースに基づく）
