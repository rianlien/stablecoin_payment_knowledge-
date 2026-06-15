---
title: "Block / Cash App"
type: company
updated: 2026-06-15
category: payments
tags:
  - stablecoin
  - USDC
  - consumer-payments
  - agent-commerce-infrastructure
  - fintech
---

# Block / Cash App

Block（旧 Square）が運営する Cash App は、米国で約 6000 万 MAU を持つ最大規模の消費者向けフィンテックアプリ。2026 年 5 月より USDC 送受信機能を段階展開し、Solana・Ethereum・Polygon・Arbitrum 対応・手数料無料で一般消費者向けステーブルコインを主流決済手段に引き上げる動きを見せている。Stripe の Link ステーブルコイン仕様や MPP といったエージェント決済インフラとも接点を持つ可能性がある。

この vault では、Block / Cash App を「消費者向けステーブルコイン普及の最大規模ベクター、かつ AI エージェント決済への人間側エンドポイントになりうる企業」として追う。

---

## 現状の要約

### 何をしているか

- **USDC 段階展開（2026-05）**：Cash App の約 6000 万 MAU に対して USDC 送受信機能を段階展開。初回フェーズは約 25%（1500 万ユーザー）が対象、週内に全ユーザー展開を予定
- **マルチチェーン対応**：Solana・Ethereum・Polygon・Arbitrum に対応。着金 USDC は自動的に USD 残高に変換（ユーザーが暗号資産リテラシーを持たなくてよい設計）
- **手数料無料化**：USDC 送受信をすべて手数料ゼロ。本人確認済みユーザーに日次送金 $2,000・週次受取 $10,000 の上限を設定
- **CEO 路線転換**：Jack Dorsey はビットコイン偏重姿勢から転換し「ユーザー需要への対応」として USDC 対応を説明

### 見立て

Cash App の USDC 展開は、ステーブルコインが「クリプトネイティブの送金手段」から「主流フィンテックアプリの標準機能」へ移行する象徴的な出来事。Venmo・Zelle との競合ポジションで USDC を標準機能化することは、規制整備（GENIUS Act：2026-07-18 施行予定）前の「実績づくり」という戦略的側面も持つ。

エージェント決済の観点では、Cash App が USDC を受け付けられるようになったことで「AI エージェントが稼いだ収益をユーザーの Cash App 口座に USDC 送金する」シナリオが技術的に成立した。ただし現時点の実装はヒューマン向け UI ベースであり、エージェントからのプログラム的 API 送金（MCP Server 等）の対応は未確認。Stripe が Sessions 2026 で発表した Link エージェントウォレット・MPP・Shared Payment Tokens との接続性も今後の焦点になる。

---

## Inbox との紐付け

### ローンチ・発表

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-27 | [[2026-05-27_Block-CashApp_usdc-stablecoin-rollout-60m-users]] | 6000 万 MAU への USDC 段階展開開始。消費者向けステーブルコイン普及の最大規模事例 |

### 関連インフラ・エコシステム（接続可能性あり）

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-30 | [[2026-04-30_Stripe-Sessions-2026_stablecoin-expansion]] | Stripe の Link ステーブルコイン受け取り仕様。Cash App との直接連携ではないが、同じ消費者 USDC 受け取りのユースケースで参照モデルになる |
| 2026-04-30 | [[2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments]] | Stripe MPP・Link エージェントウォレット。Cash App が将来 API を公開した場合に、エージェント→Cash App への送金シナリオと比較検討が必要 |

---

## 監視ポイント

- **API / MCP Server 公開の有無**：エージェントから Cash App へ USDC をプログラム送金できるインターフェイスが公開されるか。公開されればエージェント→消費者の送金エンドポイントとして最大規模の受け皿になる
- **全 6000 万ユーザー展開の完了時期と NY 州解禁**：BitLicense 制約による NY 州除外の解消タイムライン
- **Cash App Pay（IRL 決済）との USDC 連携**：USDC 残高から実店舗・EC 支払いへの動線が整備されるか
- **Venmo / PayPal の追随タイムライン**：競合の類似機能対応が USDC 普及速度を左右する
- **x402 プロトコルとの互換性**：現時点で言及なし。Cash App が x402 エコシステムに参加するかどうか
- **GENIUS Act 対応（2026-07-18）**：PPSI 規制確定後の Cash App の対応方針・ライセンス取得状況

---

## 参考リンク

- [CoinDesk — Block kicks off Cash App's phased stablecoin roll out（2026-05-27）](https://www.coindesk.com/business/2026/05/27/block-kicks-off-cash-app-s-phased-stablecoin-roll-out-to-its-nearly-60-million-users)
- [The Block — Cash App lets users send USDC stablecoins on chains like Solana and Ethereum（2026-05-27）](https://www.theblock.co/post/402784/cash-app-lets-users-send-usdc-stablecoins-on-chains-like-solana-and-ethereum)
