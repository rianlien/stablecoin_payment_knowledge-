---
title: "AllUnity、SEK ステーブルコイン SEKAU を 6 月ローンチ予定・x402 対応エージェント決済インフラも発表"
date: 2026-05-25
source: CoinDesk / The Block
source_url: https://www.coindesk.com/business/2026/05/20/germany-s-allunity-plans-swedish-krona-stablecoin-pushes-into-ai-agentic-payments
entity: AllUnity
category: stablecoin-issuer
primary_category: agentic-commerce
article_published_date: 2026-05-20
underlying_event_date: 2026-05-20
primary_source_date: 2026-05-20
tags:
  - stablecoin-issuer
  - MiCA
  - agentic-commerce
  - x402
  - Europe
summary: "ドイツの AllUnity（DWS・Flow Traders・Galaxy Digital の JV、BaFin 規制）が、スウェーデンクローナ連動ステーブルコイン SEKAU を MiCA フレームワーク下で 2026 年 6 月にローンチ予定。同時に AI エージェント開始取引を x402 標準で受け入れ、現地銀行口座に直接精算する「Agentic Payments」インフラも発表。ユーロ・スイスフラン連動に続く 3 通貨目の欧州規制ステーブルコイン。"
implications: "MiCA 準拠の非 USD ステーブルコインが x402 決済に対応したことで、欧州企業が USDC への依存なしにエージェント決済を受け入れる選択肢が生まれる。Keyrock 報告では現在 98.6% が USDC であり、欧州規制当局が USD ステーブルコインの流通を制限した場合の代替軌道として注目。"
importance: Medium
confidence: High
follow_up: "SEKAU の BaFin 最終認可時期、Agentic Payments の x402 ファシリテーターが Coinbase CDP か独自実装か、SEKAU の精算チェーン（Ethereum / AllUnity 独自か）、Swedish Digital Krona との競合 / 協調関係、欧州 PSP による Agentic Payments 採用事例"
---

## 概要

- AllUnity（ドイツ、DWS・Flow Traders・Galaxy Digital の合弁、BaFin 規制）が 2026 年 5 月 20 日に SEKAU（スウェーデンクローナ連動ステーブルコイン）の 6 月ローンチ計画を発表
- 同時に、AI エージェントが開始する取引を x402 標準で受け入れ、現地銀行口座にセトルする「Agentic Payments」インフラも発表
- AllUnity はすでに EUR ステーブルコイン（EURCV / EURALLУ）とスイスフラン連動ステーブルコインを発行しており、SEKAU は 3 通貨目

## 何が起きたか

- **SEKAU（SEK 連動ステーブルコイン）**：スウェーデンクローナ準備金で完全裏付け、MiCA フレームワーク下で発行。BaFin 最終承認待ちで 2026 年 6 月の debut を目標
- **Agentic Payments インフラ**：Coinbase の x402 標準を使い、AI エージェントが開始した取引を受け入れ、現地銀行口座に直接精算。デジタルサービス・オンラインコンテンツ・データ販売の加盟店を対象
- 欧州の「USD 依存脱却」戦略の一環と位置づけ。DWS（独Deutsche Asset Management）が主要投資家として関与

## 確認された事実

- AllUnity は BaFin 規制下で運営。EUR・CHF 連動ステーブルコインをすでに発行済み（出典：CoinDesk・The Block）
- Agentic Payments は Coinbase の x402 標準を採用と明示（出典：The Block、2026-05-20）
- 精算先は「現地銀行口座」——フィアット出金の仕組みを内包した統合型インフラ
- CoinDesk URL（coindesk.com/business/2026/05/20/）から 5 月 20 日の記事であることを確認

## なぜ重要か

### 決済事業者視点
- 欧州向けデジタルサービス加盟店が MiCA 準拠の非 USD ステーブルコインで x402 決済を受け入れる最初期の商用事例になりうる。USDC に集中するエージェント決済市場でのリスク分散の参照事例

### 加盟店視点
- デジタルサービス・コンテンツ・データ販売に特化した初期対象。フィジカル在庫不要・即時配送のユースケースから x402 普及が始まる傾向と一致

### プロダクト視点
- x402 ファシリテーターが Coinbase CDP（Base・Solana・Polygon・Arbitrum・World）を使うか AllUnity 独自実装かで、決済フローの設計が変わる。SEKAU がどのチェーンで精算されるかが未確認

### 規制 / リスク視点
- MiCA 下（BaFin 規制）で発行する非 USD ステーブルコインが x402 に対応した先行例。MiCA の電子マネートークン（EMT）規制と x402 プロトコルの整合性が欧州展開の法的試金石になる可能性

## 我々への示唆
- いま検討すべきこと:
  - SEKAU の 6 月ローンチを注視。MiCA 準拠ステーブルコインで x402 が動く実績が生まれれば、欧州事業者への x402 提案において規制適合の参照事例として使える
- 後で深掘りすべきこと:
  - AllUnity Agentic Payments の技術スタック（x402 ファシリテーター実装、チェーン選択、精算ルート）
  - SEKAU が欧州の AI エージェント開発者に採用されるかの初期エビデンス（GitHub・npm 等での SDK 採用）
- 今は優先度が低いこと:
  - 日本市場への直接的影響は今のところ限定的——欧州規制下の事例として参照するにとどめる

## ありそうな示唆
- 「規制 MiCA 準拠ステーブルコイン × x402 エージェント決済」の組み合わせが欧州のスタンダードになる可能性。EU AI Act 施行（2026 年 8 月）後に「AI エージェントの支払い追跡義務」が加わると、MiCA 準拠ステーブルコインは規制対応の観点で有利になりうる
- AllUnity（EUR・CHF・SEK）が多通貨ステーブルコインを揃えることで、欧州内クロスボーダー B2B エージェント決済の単一プロバイダーになれるポテンシャルがある

## 推測 / 監視ポイント
- BaFin 最終承認が 6 月に間に合わなければ SEKAU ローンチが遅延する
- x402 での SEKAU 使用は「ファシリテーターが USDC に変換→精算」か「SEKAU のままオンチェーン転送」か——プロトコルレベルの仕様を確認要
- スウェーデン中央銀行（Riksbank）の e-krona プロジェクトとの競合関係

## 未解決の論点
- SEKAU の精算チェーンは何か（Ethereum L1 / L2 / AllUnity 独自か）
- Agentic Payments インフラはすでに稼働中か、6 月ローンチと同時か
- MiCA EMT として発行する SEKAU の保有者制限（非 EU 居住者向け制限の有無）

## 参考リンク
- 一次情報: [CoinDesk（2026-05-20）](https://www.coindesk.com/business/2026/05/20/germany-s-allunity-plans-swedish-krona-stablecoin-pushes-into-ai-agentic-payments)
- 補足情報: [The Block（2026-05-20）](https://www.theblock.co/post/402027/allunity-plans-swedish-krona-stablecoin-launches-agentic-payments-infrastructure), [Payment Expert（2026-05-22）](https://paymentexpert.com/2026/05/22/allunity-beyond-euro-stablecoin-krona/)

## 重要度
- Medium

## 確からしさ
- High
