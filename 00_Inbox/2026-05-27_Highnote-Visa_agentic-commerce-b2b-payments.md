---
title: "Highnote × Visa、B2B 向けエージェンティックコマース決済機能を正式ローンチ——AI 起点の請求書・調達・支出管理を対象"
date: 2026-05-27
source: "The Paypers / Finovate / Yahoo Finance / Financial IT"
source_url: "https://thepaypers.com/payments/news/highnote-and-visa-launch-agentic-commerce-payment-capabilities"
entity: "Highnote / Visa"
category: "agentic-commerce"
primary_category: "agentic-commerce"
article_published_date: 2026-05-27
underlying_event_date: 2026-05-27
primary_source_date: 2026-05-27
tags:
  - agentic-commerce
  - agent-payments
  - payment-authorization
  - merchant-readiness
  - B2B
summary: "Highnote と Visa が 2026 年 5 月 27 日、AI エージェントによる B2B 決済を対象としたエージェンティックコマース機能を正式ローンチ。Visa Intelligent Commerce Connect（ICC）インターフェースを通じて構築され、AI エージェントがトークン化されたクレデンシャルとプログラマブルな支出ルールの範囲内で請求書処理・仕入先支払い・調達業務・運営費管理を自動実行できる。企業は AI エージェントが発生させた支出についてリアルタイムの可視性と監査証跡を維持できる設計。AP2（FIDO Alliance）と Visa Intelligent Commerce の B2B 応用の先例事例。"
implications: "Visa のカードネットワーク × Highnote のプログラマブル決済インフラ × AI エージェントという組み合わせにより、人間が手動で承認していた B2B 支出ワークフローが自律的な AI 実行に移行する具体的な製品が登場した。エンタープライズ向けにおける Visa ネットワーク × エージェント支払い認証の参照モデルが形成された。"
importance: High
confidence: High
follow_up: "Highnote Agentic Commerce の採用第一号企業、Visa ICC の技術仕様（支出ルール表現形式・認証フロー）、AP2 FIDO Alliance の B2B 支出マンデートとの関係、Mastercard Agent Pay との B2B 競合比較"
---

## 概要

2026 年 5 月 27 日、決済プログラマビリティ企業 Highnote と Visa が共同でエージェンティックコマース決済機能を正式ローンチした。Visa Intelligent Commerce Connect（ICC）上に構築されており、AI エージェントが企業の B2B 支出ワークフロー（請求書処理、仕入先支払い、運営費管理、AI 支援調達）を自律的に実行できるようになる。

本ローンチは Visa ICC（2026 年 4 月 8 日発表）のパイロットパートナーだった Highnote が、商用製品として正式リリースした事例。

## 何が起きたか

- **ローンチ内容**：Highnote Agentic Commerce——Visa ICC インターフェースを通じた AI 起点の B2B 決済機能

- **コア機能**：
  - トークン化されたクレデンシャル（Visa ネットワーク）を AI エージェントに付与
  - プログラマブルな支出ルール（金額上限・取引相手ホワイトリスト・時間枠）を設定
  - ダイナミック認可ロジック（リアルタイムで支出ルールを評価）
  - 支払いライフサイクル全体でのリアルタイム可視性と監査証跡

- **対象ユースケース（B2B）**：
  - 請求書処理・支払自動化（AP automation）
  - 仕入先・サプライヤーへの支払い
  - 運営費管理（operational spend management）
  - AI 支援調達（AI-assisted procurement）
  - 業種特化型の自律決済エクスペリエンス

- **設計原則**：AI エージェントが設定された支出ルールの範囲内であれば「ソフトウェアが直接実行」する。従来は人間の手動承認が必要だったワークフローを自動化しつつ、企業が可視性・監査性を維持できる構造。

## 確認された事実

- 発表日：2026 年 5 月 27 日（The Paypers, Finovate, Yahoo Finance, Financial IT が同日報道）
- Highnote は決済プログラム構築のための PaaS 企業（Visa パートナー）
- Visa Intelligent Commerce Connect は 2026 年 4 月 8 日に Visa が発表した「エージェンティックコマースへの単一統合経路」インターフェース
- Visa ICC のパイロットパートナーには Aldar・AWS・Diddo・Highnote・Mesh・Payabli・Sumvin が含まれていた
- Highnote は Visa のトークン化・認可機能と自社のプログラマブル決済インフラを組み合わせた設計を採用
- B2B に特化した初期ユースケース設計（消費者向けは後続）

## なぜ重要か

### 決済事業者視点

- Visa ネットワーク上でエージェントが請求書・仕入先支払いを自律実行できる製品が商用化された。PSP が B2B 加盟店に「エージェント決済受け入れ」を提案する際の具体的な製品例として機能する。
- ダイナミック認可ロジック（リアルタイム判定）は、スタティックな支出上限では対応できない企業支出の柔軟性要件を満たすためのアーキテクチャとして重要。

### 加盟店視点

- B2B 調達・AP 自動化の文脈では、AI エージェントが購入決定から支払い実行まで一貫して担当するシナリオが現実化した。仕入先企業はエージェント発行の支払いを Visa ネットワーク経由で受け取れる。
- 加盟店の「エージェント決済対応」として、Visa ICCを通じた認証・認可が使えることで、既存の Visa 加盟店インフラを大幅な変更なしに活用できる可能性がある。

### プロダクト視点

- 「支出ルール設定 → エージェントが自律実行 → 企業が監査」という三層構造は、CFES ガイドライン（2026-05-13）の「認可範囲 × 責任帰属 × 可視性」フレームワークの実装例として参照価値がある。
- Mastercard Agent Pay（B2C 中心）vs. Highnote/Visa（B2B 中心）という役割分担が浮かび上がってきた。

### 規制 / リスク視点

- Visa ネットワーク上のトークン化クレデンシャルを AI エージェントに付与する設計は、GENIUS Act 下での「AI エージェントに対する決済手段の委任」の一つの規制適合モデルとして解釈できる可能性がある。
- ただし「エージェントが支払いを起動する主体」の法的責任帰属（企業 vs. エージェント vs. Highnote vs. Visa）は依然として未解決。

## 我々への示唆

- いま検討すべきこと:
  - Highnote Agentic Commerce の「支出ルール表現形式」——金額上限・取引相手ホワイトリスト以外にどのルールが定義できるか。自社エージェント設計の承認ロジックに流用できるかを確認する
  - B2B 加盟店（API・SaaS・データプロバイダー）向けに Highnote/Visa ルートでエージェント決済受け入れを提案できるか評価する
- 後で深掘りすべきこと:
  - Highnote Agentic Commerce と Mastercard Agent Pay の B2B 機能の比較（支出ルール設定の柔軟性・認証スキーム・国際展開）
  - Visa ICC の「動的認可ロジック」の技術仕様——AP2 の FIDO Mandate との相互運用性
- 今は優先度が低いこと:
  - Highnote 社の詳細（PaaS 料金体系・既存顧客）——今は参照アーキテクチャとして評価することが優先

## ありそうな示唆

- Highnote/Visa の B2B ローンチは、エージェンティックコマースが「コンシューマー向けショッピング（Google Universal Cart, AP2）」と「B2B 企業支出自動化（Highnote/Visa, Mastercard Agent Pay）」に分岐して発展していることを示す。B2B セグメントは取引単価が高く、コンプライアンス要件が厳しいため、Visa ネットワークの信頼性が競争優位になる。

## 推測 / 監視ポイント

- Highnote Agentic Commerce が大手企業の AP 部門で採用される事例が出るか（B2B 導入の最初の定量実績）
- Visa ICC が非 Visa カードネットワーク（Mastercard・Amex 等）のクレデンシャルもサポートするかどうか
- Visa ICC の動的認可ロジックと AP2 FIDO Alliance の「Human Not Present」フローの設計的な整合性確認

## 未解決の論点

- Highnote Agentic Commerce がオンチェーン（ステーブルコイン）決済もサポートするか（現状は Visa カードネットワーク経由と推測）
- 「エージェントが支出ルール内で自律実行」の場合、従来型の Visa 不正取引申告フローはどう機能するか——チャージバック主体の問題
- AP2 FIDO Alliance の B2B 支出マンデートとの統合計画の有無

## 参考リンク

- 一次情報: [The Paypers（2026-05-27）](https://thepaypers.com/payments/news/highnote-and-visa-launch-agentic-commerce-payment-capabilities)
- 補足情報: [Finovate（2026-05-27）](https://finovate.com/highnote-teams-up-with-visa-to-launch-agentic-commerce-capabilities/)
- 補足情報: [Yahoo Finance / Businesswire（2026-05-27）](https://uk.finance.yahoo.com/news/highnote-collaborates-visa-agentic-commerce-100100644.html)
- 補足情報: [Financial IT（2026-05-27）](https://financialit.net/news/artificial-intelligence/highnote-collaborates-visa-agentic-commerce-ai-initiated-payments)
- 関連: [Visa Intelligent Commerce Connect 発表（2026-04-08）](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22276.html)

## 重要度

- High

## 確からしさ

- High（The Paypers, Finovate, Yahoo Finance 等の複数媒体で同日確認）
