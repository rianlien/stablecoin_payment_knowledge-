---
title: "Tether 支援の Oobit、AI エージェント専用 Visa バーチャルカード「Agent Cards」を発表 — USDT 残高から直接支出・法定通貨変換不要"
date: 2026-04-30
source: "The Block / Tech Startups / Bitcoin.com"
source_url: https://www.theblock.co/post/399583/tether-oobit-ai-agents-visa-corporate-expense-card
entity: Oobit / Tether
category: 企業発表
tags:
  - agentic-commerce
  - stablecoin
  - wallet
  - payments
summary: "Tether が支援する暗号資産決済プラットフォーム Oobit が、AI エージェント専用の仮想 Visa カード『Agent Cards』を発表。企業の USDT 財務残高から直接支出し、法定通貨への変換なしに Visa 加盟店全体で使用可能。支出ポリシーをサーバーサイドで設定・エージェントが上書き不可。Q2 2026 より KYB 審査済み企業への展開を開始。"
implications: "エージェント決済における USDT＋Visa の組み合わせは、x402・MPP・ERC-8183 とは異なる『既存カードレール活用型』のアーキテクチャを実証する。AI エージェントに専用の決済 ID・支出制限・監査ログを付与するインフラが商用化されたことで、企業の AI 自律化において決済ガバナンスが技術的に解決可能な問題として位置付けられた。"
follow_up: "KYB 審査完了後の採用企業数・平均チケットサイズ、Oobit の他ステーブルコイン（USDC 等）への拡張有無、Visa ネットワーク側でのエージェント認識フラグ対応状況"
---

## 概要

2026 年 4 月 30 日、Tether が出資する暗号資産決済プラットフォーム Oobit が「Agent Cards」を発表した。AI エージェント 1 体ごとに専用の仮想 Visa カードを発行し、企業の USDT 財務残高から直接支出できる。法定通貨への変換は不要で、支出ポリシーはサーバーサイドで強制実行される。Q2 2026 から KYB（Know Your Business）審査済み企業への展開が始まる。

## 何が起きたか

**製品概要**
- AI エージェント 1 体ごとに専用の仮想 Visa カードを発行
- 企業の USDT 財務残高（ステーブルコイン トレジャリー）から直接ファンディング
- 法定通貨への変換なしに Visa 加盟店全体で利用可能
- 発行インフラ：Tether が裏付けに回る

**支出ガバナンス**
- 支出ポリシーは初期設定時に構成し、サーバーサイドで強制実行（エージェントによる上書き不可）
- 承認・拒否を問わずすべてのトランザクションがリアルタイムで人間が読める形式のログとして記録
- 承認キューの手作業を排除

**主なユースケース**
1. **決済処理連携**：Stripe 等のプラットフォームへの接続、サブスクリプション課金・ベンダー支払いの自動化
2. **自動経費報告**：全アクティブエージェント横断の構造化されたリアルタイム経費ログ

**展開スケジュール**
- Q2 2026 より KYB 審査済み企業への追加オンボーディングを開始

## なぜ重要か

### 決済事業者視点
- Oobit Agent Cards は「クリプトカード」の既存モデル（USDT → 法定通貨リアルタイム変換 → Visa 決済）とは異なり、USDT 残高のまま Visa で直接支出する仕組みを採用。PSP が介在するオフランプレイヤー（Marqeta・Lithic 等）の役割を部分的に代替する可能性がある
- エージェント識別フラグがカードレベルで実装されれば、Visa・Mastercard の不正検知（Radar 等）にエージェント起点トランザクションとして伝達できる設計に近づく

### 加盟店視点
- 加盟店側は通常の Visa 決済として受け取るため、特別な対応は不要
- AI エージェントによる自動購買の増加（マーケティング・クラウド調達・広告購買等）への対応として、加盟店が「エージェント顧客」を意識する契機になる

### プロダクト視点
- x402（HTTP ネイティブ）・MPP（Stripe）・ERC-8183（Ethereum）が「新規プロトコル」でエージェント決済を構築するのに対し、Oobit は「既存カードレール＋ステーブルコイン財務」というアプローチ。既存インフラを使う分だけ導入障壁が低い
- Mastercard の Verifiable Intent・Stripe Radar のエージェント識別と並んで、「エージェント支出のガバナンス」が決済インフラの重要機能として確立されつつある

### 規制 / リスク視点
- AI エージェントに KYB を通じた法人格に紐付いた支出権限を付与する設計は、AML・制裁コンプライアンスの観点からは「法人の代理人としての AI」という解釈を要する
- エージェントが発注した取引の責任主体（法人か、AI システムか）は規制上まだグレーゾーン
- GENIUS Act の PPSI 規制が USDT 発行体（Tether）に適用されるかが国際競争上の論点になる

## 我々への示唆

- いま検討すべきこと:
  - 自社プロダクトが法人顧客のエージェントに対して「支出権限を付与する」インフラを提供する余地があるか。Oobit の設計（KYB 法人 → エージェントカード）を参照フレームとして評価
  - 「既存カードレール活用型」（Oobit）vs「新規プロトコル型」（x402・MPP）の顧客ニーズを早期に把握するため、法人顧客との対話を行う
- 後で深掘りすべきこと:
  - Oobit の技術スタック：Visa BIN スポンサー、カード発行体、USDT 清算の具体的フロー
  - Oobit Agent Cards と Stripe MPP の機能競合範囲（Stripe も Link エージェントウォレットを提供）
- 今は優先度が低いこと:
  - Q2 2026 以降の採用企業数（公開前）

## 未解決の論点

- Oobit が対応するステーブルコインは現時点で USDT のみか、将来的に USDC・EURC 等に拡張するか
- Visa ネットワーク側でのエージェント発行トランザクションの識別・マーキングの有無
- Tether（USDT）は GENIUS Act の PPSI 規制対象外（外国発行体）だが、米国内での Oobit を通じた利用に対して FinCEN の MSB 規制がどのように適用されるか
- 競合するエージェントカード製品（Stripe・Mastercard Agent Pay 等）との市場シェア展開

## 参考リンク

- 一次情報: [The Block 報道](https://www.theblock.co/post/399583/tether-oobit-ai-agents-visa-corporate-expense-card)
- 補足情報: [Tech Startups 報道](https://techstartups.com/2026/04/30/oobit-introduces-agent-cards-giving-ai-systems-controlled-programmable-spending-power/)
- 補足情報: [Bitcoin.com 報道](https://news.bitcoin.com/tether-backed-financial-platform-oobit-gives-ai-agents-their-own-corporate-visa-cards/)
- 補足情報: [Stripe Sessions 2026 MPP（2026-04-30）](./2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments.md)
- 補足情報: [Coinbase × x402 Agentic.market（2026-04-21）](./2026-04-21_Coinbase-x402_agentic-market-launch.md)
- 補足情報: [ERC-8183 Agentic Commerce](../04_Protocols/ERC-8183_Agentic-Commerce.md)

## 重要度

- High

## 確からしさ

- High（The Block + 複数メディア報道）
