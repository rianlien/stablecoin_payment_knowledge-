---
title: "Crossmint、Visa Intelligent Commerce ベースの Agentic Cards API を公開"
date: 2026-06-02
source: Crossmint
source_url: https://www.crossmint.com/announcement/agentic-cards-api-launch-visa-basistheory
entity: Crossmint / Visa / Basis Theory
category: payment-authorization / agent-identity / agentic-commerce
primary_category: payment-authorization
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - Crossmint
  - Visa
  - payment-authorization
  - agent-identity
  - agentic-commerce
summary: "Crossmint が 6 月 2 日、Visa Intelligent Commerce と Basis Theory を使った Agentic Cards API を公開した。対象は eligible US-issued Visa カードで、ユーザーは tokenized credential と spend limits を agent に付与できる。Basis Theory が vaulted credential layer を担い、agent 環境から生カード情報を分離する"
implications: "4 月の Visa Intelligent Commerce 発表や 5 月の Highnote 事例に続き、開発者がすぐ使える card credential API が出た。agent payments で課題だった『カード情報をどう scoped credential にするか』に対し、tokenization と PCI vault を組み合わせた実装リファレンスが具体化した"
importance: High
confidence: High
follow_up: "対象 issuer 範囲、merchant acceptance 条件、ユーザー承認フロー、返金・chargeback 時の責任分担、Visa 以外ネットワーク対応を確認する"
---

## 概要
- Crossmint が 2026 年 6 月 2 日、agentic card payments 用の API を公開した
- card number を agent に渡さず、tokenized credential と spend control で agent に支払い権限を与える構成が明示された

## 何が起きたか
- 開発者は eligible US-issued Visa の credit / debit card を agent system に接続できる
- エンドユーザーは Visa Intelligent Commerce Connect を通じて tokenized credential を作成する
- spend limits を設定し、agent には scoped permission のみを渡す
- Basis Theory が PCI Level 1 / SOC 2 の vault layer として機密決済情報を agent 環境から切り離す
- Crossmint は lobster.cash でも同機能を利用可能にし、Claude Code や OpenClaw などの agent platform で使えることを打ち出した

## 確認された事実
- Crossmint 公式 announcement の公開日は 2026-06-02
- 公式文面で Visa Intelligent Commerce と Basis Theory の利用、eligible US-issued Visa cards 対応、spend limits、vaulted credential handling が明記されている
- 開発者向け docs 公開と lobster.cash への組み込みも同日案内されている

## なぜ重要か

### 決済事業者視点
- agentic payments の論点は「エージェントが払えるか」より「どう credential を安全に渡すか」にある。Crossmint はその credential packaging を API 商品として切り出した
- issuer approval と card-network-compatible な tokenization を前提にしており、既存カード網の中で agent authorization を実装する導線が強まった

### 加盟店視点
- 加盟店から見ると新しい支払い手段を追加するより、既存 Visa acceptance 上で agent からの purchase が増える構図に近い
- そのため加盟店実装よりも、agent transaction の識別、返品、顧客サポート設計のほうが重要になる

### プロダクト視点
- tokenized credential、vault、spend limit を組み合わせた構成は、agent identity と payment authorization を同時に扱う参照実装になる
- x402 や stablecoin rail と違い、既存 consumer card をそのまま agent に持たせられるため、普及初期の friction を下げやすい

### 規制 / リスク視点
- PCI vault を agent 環境から分離する設計は、agent 開発者が生カード情報を扱うリスクを下げる
- 一方で、issuer ごとの許容範囲、ユーザー同意取得、dispute handling の詳細はまだ限定的

## 我々への示唆
- いま検討すべきこと:
  - agent payment 権限を card token と spending mandate の組み合わせで表現できるか整理する
  - vault provider と agent runtime を分離する設計を標準案として比較する
- 後で深掘りすべきこと:
  - Crossmint docs の承認フローと permission scope
  - Visa Intelligent Commerce Connect との責任分界
- 今は優先度が低いこと:
  - lobster.cash 固有の UX 詳細

## ありそうな示唆
- agentic commerce 初期は stablecoin wallet より先に、既存カードを安全に agent 化する API 層が導入を牽引する可能性がある

## 推測 / 監視ポイント
- 他の wallet / orchestration provider が同様の vaulted card credential API を出すか
- Visa 以外ネットワークや non-US issuer へ拡張されるか
- agent transaction identifier や explicit approval とどう接続されるか

## 未解決の論点
- issuer approval 条件の開示範囲
- recurring / subscription 型の agent spend をどう扱うか
- merchant 側で agent-originated card transaction をどう識別するか

## 参考リンク
- 一次情報:
  - [Crossmint Announcement（2026-06-02）](https://www.crossmint.com/announcement/agentic-cards-api-launch-visa-basistheory)
  - [Crossmint Docs](https://docs.crossmint.com/agents/overview)
- 補足情報:
  - [PR Newswire（2026-06-02）](https://www.prnewswire.com/news-releases/crossmint-launches-agentic-cards-api-using-visa-intelligent-commerce-and-basis-theory-302786624.html)

## 重要度
- High

## 確からしさ
- High
