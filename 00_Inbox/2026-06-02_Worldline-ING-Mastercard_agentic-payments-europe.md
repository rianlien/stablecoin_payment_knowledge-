---
title: "Worldline・ING・Mastercard、欧州で本番 agentic payment フローを共同実装"
date: 2026-06-02
source: Worldline / GlobeNewswire
source_url: https://www.globenewswire.com/news-release/2026/06/02/3305397/0/en/worldline-worldline-and-ing-complete-a-live-end-to-end-european-agentic-payment-in-production-press-release.html
entity: Worldline / ING / Mastercard
category: agentic-commerce / payment-authorization / merchant-PSP-readiness
primary_category: payment-authorization
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - agentic-commerce
  - Worldline
  - Mastercard
  - payment-authorization
  - merchant-readiness
summary: "Worldline が 6 月 2 日、ING・Mastercard と組んで、欧州で AI エージェント起点の決済を本番実装したことを公表した。消費者は明示的承認を保持し、取引には agentic nature を示す識別子を持たせ、ING が認証・認可を担い、Worldline が issuing / acquiring の両プラットフォームで end-to-end 処理する。Mastercard は Agent Pay によるネットワーク側ガードレールを提供する"
implications: "『agentic commerce の本番受け入れ』がカードネットワーク、銀行、アクワイアラーの 3 者協調で具体化した。加盟店側の追加実装を最小化しつつ、明示的承認と agentic transaction 識別子を組み合わせる構成は、AP2 や Visa ICC と並ぶ欧州系の現実解として重要"
importance: High
confidence: High
follow_up: "利用可能国、加盟店対象範囲、明示的承認フローと agentic transaction 識別子の仕様、返金・チャージバック時の責任分担、PSD3/PSR との整合、Worldline 加盟店向け展開計画を確認する"
---

## 概要
- Worldline が 2026 年 6 月 2 日、ING と Mastercard と共同で agentic payment の本番実装を公表した
- 欧州大手アクワイアラー、銀行、カードネットワークが揃って「AI エージェントによる購入」を現実の決済フローとして扱い始めた点が重要

## 何が起きたか
- 消費者は AI エージェントによる購入に対し、最終購入判断の場面で明示的承認を保持する
- 取引には「agentic payment」であることを示す明示的識別子が付与され、ING が認証・認可を担う
- Worldline は加盟店側の受け入れと決済処理、ING は口座・銀行レール、Mastercard はトークン化と認証レイヤーを提供
- 公式説明では、利用者保護と frictionless checkout の両立を狙う設計として語られている

## 確認された事実
- Worldline 公式ブログの公開日は 2026-06-02
- 同記事内で ING と Mastercard の協業、consumer-driven approval、agentic transaction identifier が明記されている
- これは概念説明ではなく、Worldline が自社の「We are live with agentic payments in Europe」と記す本番稼働イベントとして扱われている

## なぜ重要か

### 決済事業者視点
- Agentic payment を支える責任分担が、銀行・ネットワーク・アクワイアラーの既存分業に沿って具体化された
- 加盟店が独自に AI エージェント対応を構築するのではなく、Worldline のような PSP/アクワイアラー経由で受け入れるモデルが見えてきた

### 加盟店視点
- 既存加盟店にとって重要なのは、agentic payment が新たな決済手段ではなく、既存カード受け入れに近いオペレーションで入ってくる可能性が高い点
- 認証と明示的承認が上流で処理されるなら、加盟店側は不正・認可失敗時の取扱いルール整備が優先課題になる

### プロダクト視点
- AI エージェントの権限委任を「明示的承認」と「agentic transaction 識別子」で成立させる構成は、AP2 の intent/mandate 系設計と比較価値が高い
- Consumer-facing wallet を前面に出さず、既存銀行・カード UX の延長で実装している点は、普及優先の設計として現実的

### 規制 / リスク視点
- 欧州では強い顧客認証、代理権限、返金責任の整理が避けられない。今回の実装は、規制適合を踏まえた先行パターンとして観察価値が高い
- ただし、具体的な liability split や dispute handling は未公開

## 我々への示唆
- いま検討すべきこと:
- 明示的承認、agentic transaction 識別子、merchant acceptance の 3 層を自社設計にどう対応づけるか整理する
  - Worldline 型の「既存加盟店導線を保ったままエージェント受け入れを足す」モデルを参照し、加盟店要件を再整理する
- 後で深掘りすべきこと:
- Mastercard Agent Pay と AP2 の相互運用可能性
  - 加盟店・PSP 向けオペレーション変更点（返金、取消、サポート導線）
- 今は優先度が低いこと:
  - 個別加盟店名の特定

## ありそうな示唆
- 欧州では、ステーブルコインや新規ウォレットより先に「既存カード・銀行・PSP の延長としての agentic payment」が拡がる可能性が高い

## 推測 / 監視ポイント
- Worldline がこの実装をどの加盟店カテゴリまで広げるか
- ING / Mastercard 側から追加仕様や導入事例が出るか
- agentic transaction 識別子が業界横断の標準化議論に接続するか

## 未解決の論点
- ユーザーはどの画面で承認条件を設定・確認するのか
- 継続課金や複数回購入をどう扱うのか
- dispute、refund、chargeback の責任分担はどうなるのか

## 参考リンク
- 一次情報:
  - [GlobeNewswire（2026-06-02）](https://www.globenewswire.com/news-release/2026/06/02/3305397/0/en/worldline-worldline-and-ing-complete-a-live-end-to-end-european-agentic-payment-in-production-press-release.html)
- 補足情報:
  - なし

## 重要度
- High

## 確からしさ
- High
