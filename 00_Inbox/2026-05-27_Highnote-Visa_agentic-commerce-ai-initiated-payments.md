---
title: "Highnote × Visa、Agentic Commerce 機能を共同ローンチ——B2B AI 決済の programmable credential 実装"
date: 2026-05-27
source: Finovate / The Paypers / FFNews
source_url: https://finovate.com/highnote-teams-up-with-visa-to-launch-agentic-commerce-capabilities/
entity: Highnote / Visa
category: agentic-commerce / merchant-PSP-readiness / payment-infrastructure
primary_category: merchant-PSP-readiness
article_published_date: 2026-05-27
underlying_event_date: 2026-05-27
primary_source_date: 2026-05-27
tags:
  - agentic-commerce
  - Visa
  - spending-mandate
  - agent-payments
  - B2B-payments
summary: "米国の発行・決済プラットフォーム Highnote が Visa Intelligent Commerce Connect を通じて Agentic Commerce 機能をローンチ。AI エージェントへのトークン化 credential 発行、定義済みスペンドルールと動的オーソリゼーションを組み合わせ、エージェント起点の B2B 決済（請求書処理・AP 自動化・ベンダー支払い）を実現"
implications: "Visa Intelligent Commerce Connect の実際の採用事例が登場。PSP / イシュアーが既存カードインフラ上でエージェント向け spending mandate を商品化する方法のリファレンスとして機能する"
importance: Medium
confidence: High
follow_up: "Highnote Agentic Commerce の初期導入顧客（B2B 企業）の事例、Visa Intelligent Commerce Connect の他パートナー（AWS・Mesh・Payabli 等）との機能比較、B2C への拡張計画"
---

## 概要
- 米国の issuing-as-a-service プラットフォーム Highnote が Visa と共同で Agentic Commerce 機能を 2026 年 5 月 27 日にローンチ
- Visa Intelligent Commerce Connect（2026 年 4 月 8 日発表）を API 統合経由で実装した初期採用事例のひとつ

## 何が起きたか
- Highnote の programmable payment インフラと Visa のトークン化・オーソリゼーション機能を組み合わせ
- 企業がソフトウェアエージェントへ payment credential を発行（provisioning）できる仕組みを提供
- エージェントは事前定義のスペンドルール・リアルタイム決裁ロジックの範囲内で取引を自律実行
- **初期ユースケース（B2B）**：
  - 請求書・買掛金（AP）の自動処理
  - ベンダー支払い
  - 業務支出管理
  - AI アシスト調達
- Highnote は Visa Intelligent Commerce Connect 経由でプロトコル・トークンボルト非依存の「オンランプ」として機能

## 確認された事実
- Finovate、The Paypers、FFNews、Finextra が独立して報道（2026-05-27）
- Visa Intelligent Commerce Connect 自体は 2026-04-08 発表（underlying event は 4 月だが、Highnote 採用は 5 月 27 日の新規イベント）
- 初期パイロット企業として Aldar、AWS、Diddo、Highnote、Mesh、Payabli、Sumvin が Visa から発表済み

## なぜ重要か

### 決済事業者視点
- Visa Intelligent Commerce Connect の「最初の実採用事例」が登場したことで、PSP・イシュアーが同インフラを導入する際の参照実装が生まれた
- Highnote のような issuing-as-a-service 事業者がエージェント向け credential 発行を標準機能化する流れが加速する可能性

### 加盟店視点
- Highnote-Visa の組み合わせによるエージェント決済は既存 Visa 加盟店の追加対応なしに機能する（既存 card acceptance インフラをそのまま利用）
- B2B 調達における自動化が一般化すると、サプライヤー側も「エージェントからの発注」を前提とした受注処理フローが必要になる

### プロダクト視点
- 「スペンドルール＋動的オーソリゼーション＋トークン化 credential」のセットが、AP2 の Payment Mandate と設計上の同期を持っている
- Highnote が Visa Intelligent Commerce Connect を「プロトコル非依存 on-ramp」として実装した点は、x402・MPP・AP2 の複数プロトコル並立環境での現実的な収束点を示している

### 規制 / リスク視点
- エージェント起点の B2B 取引における PCI DSS 準拠（credential の保持主体）、および代理権限の範囲をどう定義するかが今後の課題
- Visa の tokenization + dynamic auth は既存のチャージバック・不正利用フレームワークと互換性があるため、規制リスクが相対的に低い

## 我々への示唆
- いま検討すべきこと:
  - Highnote の issuing-as-a-service を通じてエージェント向け credential を発行するシナリオを、自社の agent spending mandate 実装オプションとして評価
  - Visa Intelligent Commerce Connect API の仕様確認——Highnote 以外のイシュアー経由でも同機能にアクセスできるか
- 後で深掘りすべきこと:
  - B2B AP 自動化の事例が出揃った段階で、エージェント決済の B2B ユースケースへの適用性を再評価
- 今は優先度が低いこと:
  - Highnote 固有のプラットフォーム仕様（自社が Highnote を直接使う予定がなければ）

## ありそうな示唆
- 他の issuing-as-a-service 事業者（Lithic、Marqeta 等）が同様の機能を追随し、エージェント向け card credential 発行が業界標準機能になる可能性が高い

## 推測 / 監視ポイント
- Highnote Agentic Commerce が B2C（消費者向け）に拡張されるか
- Mastercard Agent Pay との比較で、Visa Intelligent Commerce Connect の採用率がどの程度になるか

## 未解決の論点
- エージェントが定義済みルールを逸脱した取引を試みた場合の処理（decline のみか、ユーザー確認フローがあるか）

## 参考リンク
- 一次情報:
  - [Finovate（2026-05-27）](https://finovate.com/highnote-teams-up-with-visa-to-launch-agentic-commerce-capabilities/)
  - [The Paypers（2026-05-27）](https://thepaypers.com/payments/news/highnote-and-visa-launch-agentic-commerce-payment-capabilities)
- 補足情報:
  - [FFNews（2026-05-27）](https://ffnews.com/newsarticle/paytech/highnote-collaborates-with-visa-on-agentic-commerce-for-ai-initiated-payments)
  - [Finextra（2026-05-27）](https://www.finextra.com/pressarticle/109937/highnote-and-visa-collaborate-on-agentic-commerce)

## 重要度
- Medium

## 確からしさ
- High
