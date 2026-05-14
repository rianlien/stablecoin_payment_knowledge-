---
title: "MOC: AIエージェント決済スタック 6層構造"
date: 2026-05-08
type: moc
tags:
  - agentic-commerce
  - protocol
  - payments
  - stablecoin
  - x402
source: https://zenn.dev/komlock_lab/articles/agent-payments-stack-2026
---

# AIエージェント決済スタック — 6層構造フレームワーク

> 出典: [エージェントが払う仕組み — AIエージェント決済の6層構造（小原 / Zenn）](https://zenn.dev/komlock_lab/articles/agent-payments-stack-2026)

AIエージェントが自律的に支払いを行うインフラ全体を6つのレイヤーで整理した体系図。個々のニュースを横断して理解するための基軸として使う。

---

## 6層構造

| レイヤー | 役割 | 主要プレイヤー |
|---------|------|--------------|
| **L0** 決済基盤 | チェーン・ネットワーク | Base、Solana、Polygon、Tempo |
| **L1** ウォレット・鍵管理 | エージェント向け署名・資産管理 | Coinbase Agentic Wallets、MoonPay OWS、Privy |
| **L2** ルーティング・抽象化 | クロスチェーン・法定通貨変換 | Bridge、Circle CCTP、BVNK |
| **L3** 決済プロトコル | 支払いトリガー・フロー定義 | x402、MPP、ACP、AP2、ERC-8183 |
| **L4** ガバナンス・認可 | 権限委任・コンプライアンス | ERC-8004、Visa Intelligent Commerce、Mastercard |
| **L5** アプリケーション | ユースケース | DeFi運用、マーケットプレイス、インフラ調達 |

---

## L3 プロトコル比較

### x402（Coinbase）
- **粒度**: 1リクエスト単位（API呼び出しごと）
- **仕組み**: HTTPステータスコード 402 を活用。リクエスト→支払い→レスポンスがワンサイクル
- **特性**: 即時決済、ステートレス、既存APIに後付けで統合可能
- **規模**: Base上で月間 **75M トランザクション**（2026年4月時点）
- 関連ノート: [[2026-04-02_x402-Foundation_linux-foundation-launch]] / [[2026-04-21_Coinbase-x402_agentic-market-launch]]

### MPP（Stripe × Tempo）
- **粒度**: セッションベース（複数マイクロペイメントをまとめて処理）
- **仕組み**: セッション中の累積コストを後払い精算。ステーブルコイン＆カード対応
- **特性**: Visa が公式サポート。法定通貨圏との接続を重視
- 関連ノート: [[2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments]] / [[2026-05-06_RedotPay-Tempo_mpp-agentic-payments-launch]]

### ACP — Agent Checkout Protocol（OpenAI × Stripe）
- **粒度**: EC チェックアウト単位
- **仕組み**: SharedPaymentToken（SPT）でカード番号を非開示のまま条件付き支払いを実現
- **特性**: ユーザーが事前承認→エージェントが自動実行。カード決済インフラをそのまま活用

### AP2 — Agentic Payments Protocol v2（Google）
- **粒度**: 認可フレームワーク（金額・用途・期限の委任）
- **仕組み**: Mandate（委任状）でエージェントへの支払い権限を細粒度に制御
- **特性**: 60以上の組織が協働開発。標準化・相互運用性を重視
- 関連ノート: [[2026-04-28_Google_ap2-fido-alliance]]

### ERC-8183（Agentic Commerce）
- **粒度**: エージェント間オンチェーンコマース
- **仕組み**: ジョブ発注→エスクロー→成果検証→自動決済のフルサイクル
- **特性**: 人間の介在なしにエージェント同士がサービスを売買
- 関連ノート: [[ERC-8183_Agentic-Commerce]]

---

## 垂直統合の競争構造

| 企業 | 統合レイヤー | 戦略 |
|------|------------|------|
| **Coinbase** | L0(Base) + L1(Wallets) + L3(x402) | オンチェーン一気通貫 |
| **Stripe** | L0(Tempo) + L2(Bridge) + L3(MPP/ACP) | 法定通貨圏との橋渡し |
| **Google** | L3-L4(AP2) | 標準化・認可フレームワーク定義 |
| **Visa / Mastercard** | L4 | 既存信頼ネットワークをエージェント認可に拡張 |

各社が「自社スタックで垂直統合を完結させる」方向で動いており、プロトコルの一本化は未確定。

企業別の現在地は [[MOC_Companies]] / [[Stripe]] / [[Coinbase]] で追う。

---

## 重要統計

- エージェント決済の **98.6% が USDC 建て**（2026年時点の観測値）
- x402 は Base 上で月間 **75M トランザクション**

---

## 鍵管理アプローチ（L1）

1. TEE / エンクレーブ型（ハードウェア分離）
2. MPC 分散署名（単一障害点の排除）
3. ローカル暗号化保存
4. ハードウェアウォレット連携
5. スマートコントラクトウォレット（ERC-4337 等）

---

## 現状の課題

- **認可基準の未整備**: エージェントにどこまで権限を委ねるかの設計が未成熟
- **標準の分散**: x402・MPP・ACP・AP2 が並立し、勝者未定
- **ユースケースの具体化**: インフラは整備中だが、明確なビジネスモデルはまだ探索段階

---

## 関連ノート一覧

### ニュースノート（/00_Inbox/）
- [[2026-04-02_x402-Foundation_linux-foundation-launch]]
- [[2026-04-21_Coinbase-x402_agentic-market-launch]]
- [[2026-04-28_Google_ap2-fido-alliance]]
- [[2026-04-30_Mastercard_q1-2026-agent-to-agent-payments]]
- [[2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments]]
- [[2026-05-01_MoonPay_moonagents-card-mastercard-ai-agents]]
- [[2026-05-05_Solana-GoogleCloud_pay-sh-x402-agent-payments]]
- [[2026-05-06_RedotPay-Tempo_mpp-agentic-payments-launch]]
- [[2026-05-07_AWS_bedrock-agentcore-payments-x402]]

### プロトコルノート（/04_Protocols/）
- [[ERC-8004_Trustless-Agents]]
- [[ERC-8183_Agentic-Commerce]]
