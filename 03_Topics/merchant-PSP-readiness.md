---
title: "加盟店・PSP のエージェントコマース対応"
type: topic
updated: 2026-06-29
tags:
  - merchant-readiness
  - PSP
  - agentic-commerce
  - stablecoin-payments
  - payment-infrastructure
---

# 加盟店・PSP のエージェントコマース対応

PSP（決済サービス提供者）と加盟店が AI エージェント起点の取引・ステーブルコイン決済に対応するための製品・インフラの整備状況。エージェントが「何で・どう・何まで払えるか」という問いへの答えが PSP ごとに異なる形で具体化されている。

---

## 問題の本質 / 背景

AI エージェントが人間に代わって購買・決済を実行するエージェントコマースでは、PSP と加盟店の既存インフラに 3 つの課題が生じる：

1. **支払い手段の多様化**：カード・ステーブルコイン・BNPL 等をエージェントが安全に選択・実行できる仕組みが必要
2. **認証・認可の再設計**：エージェントのアイデンティティ確認と支出権限の委任（spending mandate）の標準化が未解決
3. **事後処理の欠如**：ステーブルコイン決済の「返金・チャージバック」機能がカード決済と比べて未整備

PSP 各社は独自の API スイート・SDK・プロトコル対応でこれらを解決しようとしており、2026 年前半に主要発表が相次いだ。

---

## 主要アプローチ / 動向

### Adyen Agentic

Adyen が 2026-06-16 に発表したエンタープライズ向けエージェントコマース API スイート。3 層構成：

- **Agentic Feed**：商品カタログ・価格・在庫のリアルタイムデータを AI エージェントに配信
- **Agentic Cart**：既存のチェックアウト・税務・フルフィルメント・OMS を会話型コマースに接続
- **Agentic Payments**：エージェント起点トランザクションの認証・トークンポータビリティ・リスク管理

American Express・Mastercard・Salesforce・Visa をエコシステムパートナーに迎え、米国エンタープライズ加盟店向けにリミテッドアベイラビリティで開始。既存 Adyen 統合を再構築せずにエージェントコマースチャネルを追加できる設計。

| 日付 | ノート |
|---|---|
| 2026-06-16 | [[2026-06-16_Adyen_agentic-commerce-api-suite]] |

### Stripe Shared Payment Tokens（SPT）× BNPL

Stripe が提供する SPT（Shared Payment Tokens）は、AI エージェントが顧客の代わりに取引を開始する際に決済認証情報を直接露出せずに支払いを実行する仕組み。2026-06-16 に Zip US が SPT のサポートを発表し、エージェント起点取引で Zip の BNPL（後払い）オプションが利用可能になった。Klarna・Affirm に加え Zip が対応したことで、主要 BNPL 3 社が Stripe エージェントコマースに揃った形。

| 日付 | ノート |
|---|---|
| 2026-06-16 | [[2026-06-16_Zip-Stripe_shared-payment-tokens-agentic]] |

### Fireblocks Flow

Fireblocks が 2026-06-02 に公開した PSP・フィンテック向け stablecoin acceptance プロダクト。ウォレット生成・KYB/KYC・オフランプ・法定通貨建て精算・コンプライアンスを一体化し、PSP が加盟店に stablecoin acceptance を自社商品として提供できるインフラを提供。OTL（Open Transaction Layer）との統合で複雑な multi-step payment flow にも対応。

| 日付 | ノート |
|---|---|
| 2026-06-02 | [[2026-06-02_Fireblocks_flow-stablecoin-acceptance-psp-fintech]] |

### Circle Refund Protocol

Circle が `circlefin/refund-protocol` で提供する非カストディアル・アービター仲裁型ステーブルコイン返金プロトコル。受取側が資金管理権を保持したまま第三者アービターが紛争を仲裁する 3 者モデル。ステーブルコイン決済の「送ったら取り戻せない」という加盟店採用障壁に対応しようとするもの。ただし 2026-06-18 リリース時点でアービターが他ユーザー資金を引き出せる脆弱性が報告されており、修正開発中のため本番採用は外部監査完了後が前提。

| 日付 | ノート |
|---|---|
| 2026-06-18 | [[2026-06-18_Circle_refund-protocol-release]] |

### Highnote × Visa Intelligent Commerce Connect

Highnote（米国 issuing-as-a-service プラットフォーム）が Visa Intelligent Commerce Connect を通じて Agentic Commerce 機能をローンチ（2026-05-27）。AI エージェントへのトークン化 credential 発行、定義済みスペンドルールと動的オーソリゼーションを組み合わせ、エージェント起点の B2B 決済（請求書処理・AP 自動化・ベンダー支払い）を実現。Visa Intelligent Commerce Connect 採用の初期実装事例として機能。

| 日付 | ノート |
|---|---|
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-ai-initiated-payments]] |

---

## 監視ポイント

- **Adyen Agentic の GA 移行とグローバル展開タイムライン**：Agentic Payments レイヤーの stablecoin 対応（USDC/EURC）有無
- **Stripe SPT の拡張**：stablecoin レール（USDC）の SPT 対応（BNPL 3 社揃った次ステップ）
- **Circle Refund Protocol の脆弱性修正と外部監査完了**：本番採用可能になる時期
- **Fireblocks Flow の採用 PSP 事例**：実際にどの PSP が採用し、どの加盟店に展開するか
- **Highnote の B2C 拡張**：B2B AP 自動化から消費者向けへの展開計画

---

## 関連ノート

| 日付 | ノート | 位置づけ一行 |
|---|---|---|
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-ai-initiated-payments]] | Visa Intelligent Commerce Connect 採用の初期実装——B2B エージェント決済への spending mandate 付与 |
| 2026-06-02 | [[2026-06-02_Fireblocks_flow-stablecoin-acceptance-psp-fintech]] | Fireblocks Flow——PSP が加盟店に stablecoin acceptance を商品提供するインフラ |
| 2026-06-16 | [[2026-06-16_Adyen_agentic-commerce-api-suite]] | Adyen Agentic 3 層 API スイート——エンタープライズ加盟店の既存フローにエージェントコマースを追加 |
| 2026-06-16 | [[2026-06-16_Zip-Stripe_shared-payment-tokens-agentic]] | Zip × Stripe SPT——エージェント起点の BNPL 取引を実現、支払い手段多様化の先行事例 |
| 2026-06-18 | [[2026-06-18_Circle_refund-protocol-release]] | Circle 非カストディアル返金プロトコル——stablecoin 決済の加盟店採用障壁（返金不可）に対応（脆弱性修正中） |
