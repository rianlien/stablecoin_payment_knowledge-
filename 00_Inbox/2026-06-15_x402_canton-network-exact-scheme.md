---
title: "x402 に Canton Network の Exact Scheme 対応が追加——機関向けブロックチェーンで x402 決済が可能に"
date: 2026-06-15
source: GitHub x402-foundation/x402 issue #2551
source_url: https://github.com/x402-foundation/x402/issues/2551
entity: x402 Foundation / Digital Asset
category: machine-payments
primary_category: machine-payments
article_published_date: 2026-06-15
underlying_event_date: 2026-06-15
primary_source_date: 2026-06-15
tags:
  - x402
  - machine-payments
  - institutional-payments
  - Canton-Network
  - agentic-commerce
summary: "x402 プロトコルに Canton Network（Digital Asset の機関向けブロックチェーン）の exact scheme 対応が追加された（issue #2551 close、2026-06-15）。CIP-56 TransferFactory_Transfer を使い、ファシリテーターはレジャーへの「読み取り専用」アクセスで決済検証を行い、クライアント（参加機関）側が on-chain 送信する設計。Daml コントラクトによるプライバシー保護・ガス不要・機関向け決済要件を満たす。Goldman Sachs・SIX Group・Citi 等が参加する Canton ネットワークに x402 machine payments が接続したことを意味する。"
implications: "機関投資家・銀行が参加する Canton Network で x402 の都度課金 machine payments が利用可能になった。既存 Daml 契約インフラを活かしながら AI エージェント向けマイクロペイメントを導入できる。TradFi 機関がエージェント決済エコシステムに参加するルートが一つ加わった。"
importance: Medium
confidence: Medium
follow_up: "Canton Network 上で x402 決済を実際に採用する機関プレイヤーの動向、CIP-56 以外の Canton コントラクトとの互換性、Daml コントラクト＋x402 の共同ユースケース"
---

## 概要

x402 プロトコルの機関向けブロックチェーンへの展開として、Canton Network の exact scheme 対応が追加された（2026-06-15、GitHub issue #2551 close）。Canton Network は Digital Asset が開発した Daml ベースの機関向けブロックチェーンで、Goldman Sachs・SIX Group・BNP Paribas・Citigroup などが参加している。

## 何が起きたか

- x402-foundation/x402 の issue #2551「Exact scheme support on Canton Network」が 2026-06-15 にクローズ
- Canton Network 向けの exact scheme 実装が x402 コアリポジトリに統合された
- 決済フロー：クライアントが自分の Canton 参加ノードで CIP-56 `TransferFactory_Transfer` を実行 → `updateId`（更新 ID）を取得 → ファシリテーターが読み取り専用のレジャーアクセスで決済を検証 → レスポンスを返す
- ファシリテーターはオンチェーンへの送信コマンドを出さない（クライアント側の参加ノードが送信を担う）設計

## 確認された事実

- GitHub x402-foundation/x402 issue #2551 が 2026-06-15 にクローズ（一次情報）
- 実装は CIP-56（Canton Interoperability Protocol 第 56 号）の `TransferFactory_Transfer` コントラクトを使用
- Canton Network は Daml スマートコントラクト基盤で、参加者ごとにスコープされたコントラクト可視性（プライバシー保護）が特徴
- 対応アセット：CIP-56 に対応した任意のアセット（Canton Coin / Amulet を含む）
- ガス（手数料）モデル：ガス不要（Canton Network 自体にガス概念がない）

## なぜ重要か

### 決済事業者視点

- Canton Network は Goldman Sachs・SIX Group・BNP Paribas・Citi・ASX 等が参加する機関向けブロックチェーン。これら機関がエージェント決済を実施する場合、Canton 上で x402 が使えることは統合コストを大幅に下げる
- ファシリテーターが「読み取り専用」という設計は、既存の Canton コンプライアンス・プライバシーポリシーとの衝突を最小化する

### 加盟店視点

- 機関向けエコシステム（トークン化証券・機関間決済・CLO 等）に参加している事業者が x402 ペイウォールを Canton 上で実装できるようになる
- ガス不要なため、高頻度の小額 machine payment に向いた実装が可能

### プロダクト視点

- x402 が「パブリック EVM（Base・Arbitrum）」から「機関向けプライベートブロックチェーン（Canton）」へと展開を広げた重要ステップ
- Daml のコントラクト可視性（ステークホルダー単位）は GDPR・機関コンプライアンスに親和的で、EU の機関向けユースケースとの親和性が高い
- USDC 以外のアセット（機関発行トークン等）を x402 で流通させる先行事例になりうる

### 規制 / リスク視点

- Canton Network は規制当局との対話実績がある機関向けネットワーク。x402 が Canton に接続することで、規制当局からの見え方が「暗号資産投機ツール」から「機関決済インフラ」に近くなりうる
- CIP-56 の正式仕様は Canton / Digital Asset が管理しているため、x402 Foundation とデジタルアセット社の継続的な協調が必要

## 我々への示唆

- いま検討すべきこと:
  - Canton Network 参加機関（Goldman 等）がエージェント決済ユースケースを検討している場合、x402 Canton 実装を提案できる環境が整った
- 後で深掘りすべきこと:
  - 実際の Canton x402 ユースケース（機関間 API 課金・トークン化資産のエージェント取引等）の事例を収集する
  - CIP-56 対応アセット一覧と USDC の Canton 展開状況
- 今は優先度が低いこと:
  - Canton Network の非金融ユースケースへの x402 適用

## ありそうな示唆

- Canton Network への x402 対応は、x402 が「EVM／クリプトネイティブ」という認識を持つ機関向けに「既存 Canton インフラに統合可能」という訴求を可能にする。Digital Asset 社のセールス活動と組み合わさって、大手機関が Canton x402 パイロットを始める可能性がある

## 推測 / 監視ポイント

- Goldman Sachs / SIX Group 等 Canton 参加機関による x402 採用アナウンス
- Canton x402 の対応アセットが Canton Coin（Amulet）のみか USDC 等も含むか
- Digital Asset 社と x402 Foundation の公式パートナーシップ発表

## 未解決の論点

- Canton ファシリテーターの実装は x402 Foundation が提供するのか Digital Asset 社が独自提供するのか
- CIP-56 の更新（Canton のガバナンス変更）が x402 実装に与える影響

## 参考リンク

- 一次情報: [x402-foundation/x402 issue #2551（GitHub）](https://github.com/x402-foundation/x402/issues/2551)
- 補足情報: [Canton Network 公式サイト](https://www.canton.network/)

## 重要度
- Medium

## 確からしさ
- Medium（GitHub issue のクローズで確認。実際の Canton Network 参加機関による本番採用は未確認）
