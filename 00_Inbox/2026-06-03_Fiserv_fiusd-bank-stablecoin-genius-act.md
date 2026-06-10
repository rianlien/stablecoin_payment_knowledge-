---
title: "Fiserv、GENIUS Act 準拠の銀行向けステーブルコイン FIUSD を 7 月ローンチへ"
date: 2026-06-03
source: "Payment Week / Payments Dive"
source_url: "https://paymentweek.com/2026-6-3-fiserv-stablecoin-arrives-next-month/"
entity: Fiserv
category: PSP-readiness / stablecoin-payments / regulation
primary_category: PSP-readiness
article_published_date: 2026-06-03
underlying_event_date: 2026-06-03
primary_source_date: 2026-06-03
tags:
  - stablecoin
  - PSP-readiness
  - GENIUS-Act
  - bank-infrastructure
  - FIUSD
summary: "Fiserv CEO が Bernstein の Strategic Decisions カンファレンスで、銀行・信用組合向けステーブルコイン FIUSD（Financial Institution U.S. Dollar）を 7 月にローンチすると表明。GENIUS Act 準拠設計で、銀行が顧客預金を自行エコシステム内に保持しつつトークン化ドル残高を提供できる。Bank of North Dakota がパイロットパートナー。"
implications: "Fiserv が約 1 万の銀行・信用組合に FIUSD を展開すれば、ステーブルコインの分散型発行モデル（各行独自発行）が普及し、Circle USDC のような集中型モデルと競合・補完する構造が生まれる。エージェント決済レールへの統合には追加対応が必要だが、規模感は見逃せない。"
importance: Medium
confidence: High
follow_up: "7 月ローンチの実現・Bank of North Dakota パイロット結果・GENIUS Act 準拠取得状況・x402/AP2/Circle CPN との相互運用性計画・Clover 加盟店決済との統合"
---

## 概要

- Fiserv（世界最大級の決済テクノロジー企業、約 1 万の銀行・信用組合を顧客）が銀行・信用組合向けステーブルコイン FIUSD を 7 月にローンチ予定
- FIUSD = "Financial Institution U.S. Dollar"——各銀行・信用組合が独自に発行できる GENIUS Act 準拠のドル建てステーブルコイン
- 1 DDA（預金口座）にフィアット残高とステーブルコインウォレットを並存させる設計

## 何が起きたか

- CEO Mike Lyons が 2026-06-03 の Bernstein Strategic Decisions カンファレンスで 7 月ローンチを公表
- Bank of North Dakota が最初のパイロットパートナーとして参加予定
- 設計：顧客の預金を自行エコシステム内に維持しながら、トークン化されたドル残高・転送機能を提供する

## 確認された事実

- 発表者：Fiserv CEO Mike Lyons（Bernstein Strategic Decisions カンファレンス、2026-06-03）
- ローンチ目標：2026 年 7 月
- 対象顧客：Fiserv が契約する銀行・信用組合（約 1 万機関）
- 規制準拠：GENIUS Act に対応する設計
- パイロット：Bank of North Dakota
- 設計コンセプト：1 DDA の中にフィアット残高とステーブルコインウォレットを並存させ、預金が銀行外に流出しない構造

## なぜ重要か

### 決済事業者視点

- Fiserv は世界最大級のコアバンキング・決済インフラ提供者。1 万機関への展開は、ステーブルコイン決済の潜在的な着地ネットワークを一気に拡大する
- 「各銀行独自発行」モデルは、Circle USDC（単一発行体）・Tether USDT との根本的な差別化：銀行が既存の顧客信頼基盤とともにステーブルコインを提供できる

### 加盟店視点

- Fiserv の加盟店向け決済ソリューション（Clover など）と統合された場合、加盟店が FIUSD でのステーブルコイン決済を受け入れる経路が生まれる
- ただし現時点では加盟店向け決済統合は未確認

### プロダクト視点

- x402・AP2 等のエージェント決済プロトコルが FIUSD をサポートするには追加の技術統合が必要——現時点では USDC との直接競合ではなく補完的ポジション
- GENIUS Act 準拠設計であれば、将来的に PPSI 認定を受けた場合エージェント決済にも利用可能

### 規制 / リスク視点

- 各行が独自に FIUSD を発行する場合、GENIUS Act の「1:1 準備金」「AML/CFT プログラム」要件を各行が個別に満たす必要がある
- 分散型発行モデルは、FDIC 保険（各行の顧客預金に適用）との整合性が取りやすい——FDIC NPRM の「ステーブルコイン保有者には pass-through 保険なし」問題を銀行保有者の観点から回避しやすい設計

## 我々への示唆

- いま検討すべきこと:
  - FIUSD の x402/AP2 統合計画が発表された場合の、自社エージェント決済設計への影響評価
  - Fiserv 経由のステーブルコイン着地ネットワークが整った際の加盟店向けアプローチ機会
- 後で深掘りすべきこと:
  - Clover（Fiserv 加盟店 POS）への FIUSD 統合タイムライン
  - 他社コアバンキングプロバイダー（FIS・Jack Henry）の同様の動き
- 今は優先度が低いこと:
  - Bank of North Dakota パイロットの詳細規模（小規模パイロットの段階では直接影響なし）

## ありそうな示唆

- FIUSD が普及すれば、ステーブルコイン決済の送金先が「USDC（Circle 発行）」から「各銀行発行の互換ステーブルコイン」に多様化する。エージェント決済インフラが「どのステーブルコインでも受け入れる」設計になっているかが重要
- Fiserv が x402 や AP2 への統合を発表した場合、一気にエージェント決済の主要インフラになりうる規模感を持つ

## 推測 / 監視ポイント

- 7 月ローンチの実現と Bank of North Dakota パイロットの規模・成果
- Fiserv の加盟店決済（Clover、約 200 万台の POS 端末）との統合計画
- x402・AP2・Circle CPN との相互運用性の有無
- 他のコアバンキングプロバイダー（FIS、Jack Henry）の同等製品発表

## 未解決の論点

- FIUSD は各銀行ブランドのステーブルコインなのか、「Fiserv FIUSD」という統一トークンなのか
- 銀行間の FIUSD は相互に交換可能か（ERC-20 標準など）、または行ごとに分断されるか
- エージェントが複数の FIUSD 発行銀行に送金する際の経路設計

## 参考リンク

- 一次情報: [Payment Week（2026-06-03）](https://paymentweek.com/2026-6-3-fiserv-stablecoin-arrives-next-month/)
- 補足情報: [Payments Dive（2026-06-03）](https://www.paymentsdive.com/news/fiserv-stablecoin-arrives-next-month/821877/)

## 重要度

- Medium

## 確からしさ

- High
