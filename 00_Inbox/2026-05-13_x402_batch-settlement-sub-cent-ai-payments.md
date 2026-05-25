---
title: "x402 バッチ決済対応——$0.0001 以下の AI マイクロペイメントを実現"
date: 2026-05-13
source: CoinTelegraph / Cryptopolitan
source_url: https://cointelegraph.com/news/coinbase-launches-x402-batch-settlement-ai-payments
entity: Coinbase / Base / x402 Foundation
category: protocol
primary_category: protocol / agentic-commerce
article_published_date: 2026-05-13
underlying_event_date: 2026-05-13
primary_source_date: 2026-05-13
tags:
  - x402
  - agent-payments
  - micropayments
  - protocol
  - Base
summary: "Base 開発者 Jesse Pollak が x402 プロトコルのバッチ決済（Batched Settlement）対応を発表。買い手がオンチェーン・エスクローに ERC-20 トークンを預け、リクエスト毎にオフチェーン・バウチャーに署名し、売り手が後で複数の支払いを一括オンチェーン決済できる仕組みを追加。1 コール $0.0001 未満の AI 向けマイクロペイメントが経済的に成立。"
implications: "コンピュートや推論の per-call 課金を AI エージェントが直接支払うコスト構造が成立し、x402 の AI インフラ課金ユースケースが大幅に拡張される。Stripe Tempo のストリーミング決済モデルと競合するポジションが明確化。"
importance: High
confidence: Medium
follow_up: "バッチ決済の公式仕様書（x402 GitHub）・ERC-20 エスクロー設計の詳細・Coinbase CDP SDK での実装 API を確認。TradingView / Cryptopolitan の二次報道は確認済み、一次情報（Coinbase 開発者ブログ / Jesse Pollak X ポスト）は未直接確認。"
---

## 概要
- Base 開発者 Jesse Pollak が 2026 年 5 月 13 日、x402 プロトコルへのバッチ決済（Batched Settlement）対応追加を発表
- バッチ決済により 1 コール $0.0001 以下の支払いが経済的に実行可能になり、AI エージェントが推論・コンピュートリソースに per-call で直接支払うユースケースを解放

## 何が起きたか
- Base / Coinbase がオンチェーンエスクロー + オフチェーンバウチャー方式のバッチ決済を x402 に追加
- 仕組み：①買い手が ERC-20 トークン（USDC 等）をオンチェーンエスクローに預託 → ②リクエスト毎に署名付きオフチェーンバウチャーを生成 → ③売り手はバウチャーを即時検証してサービスを提供 → ④複数の支払いを蓄積し後から単一のオンチェーントランザクションで一括決済
- 発表時点の x402 累積実績：169M 件以上の支払い、59 万人以上の買い手、10 万件以上の売り手サービス

## 確認された事実
- 発表者：Jesse Pollak（Base コアチーム）、2026-05-13
- バッチ決済の主目的：$0.0001 未満の per-call 支払いを経済的に実現し、ブロックチェーン手数料を多数の取引に分散させる
- 対象ユースケース：AI エージェントが推論・コンピュート・API を per-call で支払う課金モデル
- プロトコルの現在のネットワーク：Base・Ethereum・Solana（SDK：TypeScript・Python・Go・Java）
- x402 は Coinbase と Cloudflare が共同運営する x402 Foundation により管理。Linux Foundation 傘下で Stripe・AWS・Google・Visa・Circle・Solana Foundation 等 20 社超がサポート
- 二次報道（CoinTelegraph・Cryptopolitan・TradingView News）による確認。一次情報（Coinbase 開発者ブログ / Jesse Pollak 投稿）は直接未確認

## なぜ重要か

### 決済事業者視点
- x402 の課金単位がセント以下（$0.0001〜$0.000001）に拡張されたことで、PSP が AI インフラ課金（推論・コンピュート・MCP サーバーアクセス）の決済ミドルウェアとして関与できる範囲が広がる
- バッチ決済はオフチェーン処理後にオンチェーン一括決済するため、既存の ISO 20022 / カード決済のバッチ処理概念と構造的に類似しており、PSP の理解・実装コストが低い可能性がある

### 加盟店視点
- SaaS API・コンテンツ課金・MCP サーバー等で「リクエスト単位の微細な従量課金」が実装可能になる。サブスクリプション/プリペイドに依存していた価格設定を per-call モデルに移行できる
- バウチャー方式で即時サービス提供 → 後で一括決済のため、オフライン決済（航空機内 API・エッジ推論）への応用可能性がある

### プロダクト視点
- Stripe Tempo（ストリーミング決済 × Metronome、2026-04-30 Sessions 2026 発表）と直接競合するポジション：Tempo は「トークン消費量連動のリアルタイムストリーミング課金」、x402 バッチ決済は「per-call オフチェーンバウチャー + オンチェーン一括」。前者はフィアット/ステーブルコイン両対応、後者はオンチェーン USDC 専用
- Circle Nanopayments（$0.000001 USDC、ガスフリー、2026-04-29 メインネット）との競合・補完関係：Nanopayments は Circle 独自インフラ（Arc 上）、x402 バッチ決済は開放プロトコルとして複数チェーンで動作

### 規制 / リスク視点
- バウチャーを多数蓄積して一括決済する場合、決済フロー内で大量の未決済債務（floating liabilities）が生じる可能性がある。GENIUS Act の準備金要件・e-money 規制との整合性を確認する必要がある
- EU のオフチェーンバウチャーは e-money 相当として MiCA の適用を受ける可能性がある

## 我々への示唆
- いま検討すべきこと:
  - x402 バッチ決済 vs Circle Nanopayments vs Stripe Tempo の技術・コスト・エコシステムの 3 軸比較。AI トークン課金・API マイクロ課金の自社ユースケースに最適なスタックを選定するための技術評価を開始する
  - x402 の公式バッチ決済仕様書（GitHub: coinbase/x402）を確認し、ERC-20 エスクロー設計と EVM 非対応チェーン（Solana）での実装差分を把握する
- 後で深掘りすべきこと:
  - バッチ決済のオフチェーンバウチャーが MiCA（EU）・GENIUS Act（米）の e-money 定義に該当するかどうかの法的分析
  - x402 バッチ決済の最初の本番採用事例（AWS AgentCore・Cryptorefills が採用するかどうか）の確認
- 今は優先度が低いこと:
  - バッチ決済の非 EVM チェーン（Solana）への対応状況——現時点では EVM（Base・Ethereum）中心とみられる

## ありそうな示唆
- バッチ決済の登場でAI推論サービス（OpenAI API・Anthropic API・ローカル LLM）が x402 を標準課金レールとして採用する動機が生まれる。「per-token 課金 = x402 バッチ決済」という事実上の標準が形成される可能性がある
- Circle Nanopayments（Arc 上、ガスゼロ、$0.000001）との比較では、x402 バッチ決済は「オープンプロトコル × 既存 EVM チェーン上」という差別化ポジション。どちらを選ぶかは「Circle エコシステムへの依存度」と「マルチチェーン対応の重要性」で決まる

## 推測 / 監視ポイント
- x402 Foundation が AWS AgentCore・Circle Agent Stack と共同でバッチ決済の相互運用性を整備するかどうか
- x402 のバッチ決済が Stripe Tempo の「ストリーミング決済」競合として位置づけられるかどうか——Stripe の x402 Foundation サポート会員としての立場との矛盾が生じる可能性
- Solana 上での x402 バッチ決済実装（USDC on Solana + Solana Programs でのエスクロー）がいつリリースされるか

## 未解決の論点
- バッチ決済の公式仕様書 URL と実装ガイドの場所
- ERC-20 エスクローコントラクトの監査状況（公開 audit report があるか）
- バウチャー蓄積期間中のデフォルトリスク管理（買い手がエスクローを引き出した場合の売り手保護）

## 参考リンク
- 一次情報: [Coinbase x402 ドキュメント](https://docs.cdp.coinbase.com/x402/welcome) / Jesse Pollak（Base）による X 発表（2026-05-13、直接 URL 未確認）
- 補足情報:
  - [CoinTelegraph（2026-05-13）](https://cointelegraph.com/news/coinbase-launches-x402-batch-settlement-ai-payments)
  - [Cryptopolitan（2026-05-13）](https://www.cryptopolitan.com/base-adds-batch-settlement-to-x402/)
  - [CoinLaw（2026-05-13）](https://coinlaw.io/coinbase-x402-launches-ai-payment-upgrade/)

## 重要度
- High

## 確からしさ
- Medium（複数の二次報道で確認済み。一次情報：Coinbase 開発者ブログ / Jesse Pollak X ポストは直接未確認）
