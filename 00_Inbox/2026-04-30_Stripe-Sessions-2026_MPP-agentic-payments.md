---
title: "Stripe Sessions 2026：Machine Payments Protocol（MPP）と AI エージェント決済インフラ"
date: 2026-04-30
source: Stripe 公式ブログ
source_url: https://stripe.com/blog/everything-we-announced-at-sessions-2026
entity: Stripe
category: 企業発表
tags:
  - agentic-commerce
  - payments
  - protocol
  - stablecoin
  - wallet
summary: "Stripe が Machine Payments Protocol（MPP）を発表。AI エージェントがマイクロ・定期・オンデマンド決済をプログラムで実行できる標準プロトコルで、Link エージェントウォレット・Shared Payment Tokens・Privy CLI ウォレットプロビジョニングと組み合わせ、エージェント向け決済インフラのフルスタックを提供。"
implications: "x402（Linux Foundation）や ERC-8183（Ethereum）と並行して、Stripe が独自のエージェント決済標準 MPP を提唱。既存の Stripe エコシステム（Bridge・Link・Treasury・Issuing）を全て統合したインフラ優位で市場を押さえにいく構図。"
follow_up: "MPP の仕様公開有無・オープン化動向、x402 との相互運用性、Radar エージェント識別機能の GA タイミング"
---

## 概要

Stripe Sessions 2026（2026-04-30）で発表された Machine Payments Protocol（MPP）は、AI エージェントが人間の介在なしに決済を完了するための Stripe 独自の標準。Link エージェントウォレット・Shared Payment Tokens・Privy CLI・Stripe Console と組み合わさり、エージェントが「発見 → 承認 → 支払い → 管理」を完結できる統合インフラを形成する。

## 何が起きたか

**Machine Payments Protocol（MPP）**
- AI エージェントがマイクロ決済・定期決済・オンデマンド決済をプログラムで実行するためのプロトコルを発表
- Stripe が独自標準として提唱（仕様のオープン化・外部公開の有無は現時点で未確認）

**Link エージェントウォレット**
- エージェントが加盟店の承認と可視性を保ちながら決済を実行できるウォレット機能
- ステーブルコイン・法定通貨カード・Klarna・Affirm（BNPL）を横断して支払い可能

**Shared Payment Tokens**
- ステーブルコイン・法定カード・Klarna・Affirm を単一トークンに統合し、エージェントが複数決済手段を統一的に扱えるようにする仕組み

**Privy CLI によるエージェントウォレットプロビジョニング**
- Privy との連携で、エージェント向けウォレットをコマンドラインから即時発行
- エージェントの支出状況を管理するダッシュボードを提供
- 加盟店側がエージェントのスコープルール・承認フローを設定可能な「エージェントガードレール」も提供

**Stripe Console（エージェンティック実行環境）**
- 自然言語でビジネス上の問題や Stripe 操作タスクをエージェントが完結できる実行環境
- 「アイデンティティ割り当て・スコープルール・機密アクションの承認フロー」によるエージェント制御

**Radar エージェント識別機能（プレビュー）**
- 正規の AI エージェントと不正アクターを識別する機能
- ボット悪用防止と「エージェント経由の正規取引」を区別する機能を同時プレビュー

## なぜ重要か

### 決済事業者視点
- Stripe が MPP という独自プロトコルを提唱したことで、エージェント決済の標準争いが加速する。x402（Linux Foundation）・ERC-8183（Ethereum）・MPP（Stripe）の 3 系統が並走するフェーズへ
- Stripe は x402 Foundation の創設メンバーでもあるため、MPP と x402 が競合するのか補完するのかが不明確。Stripe 内部でのポジション整理が焦点

### 加盟店視点
- エージェントが Klarna・Affirm（BNPL）まで利用できる Shared Payment Tokens は、エージェントが「人間と同等の購買力」を持つことを意味する。与信・規制対応は誰の責任かが問われる
- 加盟店がエージェントの支出上限・承認ルールを設定できる点は、エンタープライズ向け導入ハードルを下げる

### プロダクト視点
- MPP + Link エージェントウォレット + Bridge（ステーブルコイン） + Issuing（バーチャルカード） + Treasury（残高管理）の組み合わせで、Stripe はエージェントの「財布」として機能するフルスタックを持った
- ERC-8183（Trustless Agents）・ERC-8004 との接続性は現時点で不明。Stripe がオンチェーン資産とオフチェーン Stripe 残高のブリッジをどう設計するかが問われる

### 規制 / リスク視点
- エージェントが BNPL（Klarna・Affirm）を利用する場合、消費者信用法・与信審査要件との整合が問われる（エージェント利用者が「消費者」に当たるか否か）
- Radar のエージェント識別機能はボット/エージェント区別の実装例として業界注目を集めるが、識別精度・誤検知リスクは GA 後のデータ蓄積が必要

## 我々への示唆

- いま検討すべきこと:
  - MPP の仕様が公開された場合、x402・ERC-8183 との相互運用性評価を優先。Stripe エコシステムに閉じたプロトコルであれば、オープン標準優先の方針を再確認
  - Link エージェントウォレットの「加盟店承認フロー」設計は、自社のエージェント向け決済プロダクト設計に直接参照できる
- 後で深掘りすべきこと:
  - MPP と x402 の技術的差異（HTTP 402 ベースか、Stripe API ベースか）および Stripe が両方を維持する意図
  - Radar エージェント識別機能の識別シグナル（IPアドレス、User-Agent、行動パターン等）の公開情報
- 今は優先度が低いこと:
  - Stripe Console は Stripe 内部運用ツールのため、外部プロダクト開発への直接的な影響は小さい

## 未解決の論点

- MPP 仕様はオープンか、Stripe 固有か。x402 との関係（競合・補完・統合）が未明
- Shared Payment Tokens における BNPL（Klarna・Affirm）のエージェント利用の与信審査フロー
- Privy CLI ウォレットの KYC/AML 責任分担（Stripe・Privy・事業者それぞれの役割）
- エージェントガードレールの「機密アクション承認フロー」の具体的な実装（人間介在必須か、自動化可能か）

## 参考リンク

- 一次情報: [Stripe Sessions 2026 発表まとめ](https://stripe.com/blog/everything-we-announced-at-sessions-2026)
- 補足情報: [x402 Foundation Linux Foundation 移管（2026-04-02）](./2026-04-02_x402-Foundation_linux-foundation-launch.md)
- 補足情報: [Coinbase Agentic.market × x402（2026-04-21）](./2026-04-21_Coinbase-x402_agentic-market-launch.md)
- 補足情報: [ERC-8183 Agentic Commerce プロトコルノート](../04_Protocols/ERC-8183_agentic-commerce.md)
- 補足情報: [ERC-8004 Trustless Agents プロトコルノート](../04_Protocols/ERC-8004_trustless-agents.md)

## 重要度

- High

## 確からしさ

- High（Stripe 公式ブログによる一次情報。MPP 仕様詳細は未公開のため「Stripe が発表した」事実は High、仕様内容の解釈部分は Medium）
