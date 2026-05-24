---
title: "Sui、ステーブルコインのガスレス送金をメインネットで本番稼働（Fireblocks 連携）（2026-05-20）"
date: 2026-05-20
source: PR Newswire / Sui Blog
source_url: https://www.prnewswire.com/news-releases/sui-launches-gasless-stablecoin-transfers-with-support-from-fireblocks-302778111.html
entity: Sui / Mysten Labs
category: payment-infrastructure / stablecoin-infrastructure
primary_category: payment-infrastructure
article_published_date: 2026-05-20
underlying_event_date: 2026-05-20
primary_source_date: 2026-05-20
tags:
  - stablecoin-infrastructure
  - merchant-readiness
  - payment-infrastructure
  - Fireblocks
summary: "Sui がメインネットでステーブルコインのガスレス送金（SUI トークン不要）を本番稼働。USDC を含む 7 種のステーブルコインに対応。Fireblocks がローンチ前から統合済み。プロトコルレベルの恒久的な設計変更であり補助金・一時施策ではない。"
implications: "ステーブルコイン決済の最大のUX障壁の一つ（ガストークン別途保有要件）が Sui 上で解消。エージェント決済・加盟店決済の実装がシンプルになる。Fireblocks との同時統合は、機関向け採用の即時可能性を示す。"
importance: Medium
confidence: High
follow_up: "他チェーン（Base・Solana・Arbitrum 等）での同種のガスレス機能の対応状況、エージェント決済フローでの Sui × Fireblocks の実際の実装例"
---

## 概要

2026 年 5 月 20 日、Sui ブロックチェーンがメインネット上でステーブルコインのガスレス送金機能を本番稼働させた。この機能は、ユーザーや企業が SUI トークンを別途保有・管理することなく、ステーブルコインのみで送金・支払いを完了できるプロトコルレベルの恒久的な設計変更。Fireblocks がローンチ前から統合を完了しており、機関向け利用が即日から可能な状態でスタートした。

## 何が起きたか

- Sui がメインネットでガスレスステーブルコイン送金を本番稼働（2026-05-20）
- **対応ステーブルコイン（7 種）**：USDsui・suiUSDe・AUSD・FDUSD・USDB・USDC・USDY
- **仕組み**：ステーブルコイン送金手数料は $0.00 on Sui。SUI ネイティブトークンのガス残高が不要
- **設計の性質**：補助金・スポンサープログラム・一時的キャンペーンではなく、プロトコルレベルの単/バッチ P2P 送金に対する恒久的な構造変更
- Fireblocks（$14 兆以上のデジタルアセットを保護）がローンチ前に統合を完了し、機関向け採用の初期参照事例となっている

## 確認された事実

- ローンチ日：2026-05-20（PR Newswire・Sui ブログ・Daily Hodl 等複数媒体が報道）
- 対応ステーブルコインに USDC が含まれる
- Fireblocks がローンチ前（pre-launch）に統合を完了したと明示
- プロトコルレベルの恒久的設計変更であると Sui が明言

## なぜ重要か

### 決済事業者視点

- ガストークン別途保有というオンボーディング摩擦が Sui 上で解消。ステーブルコイン決済を実装する PSP が「ガス管理」という付随コストを排除できる
- Fireblocks の事前統合により、Fireblocks を利用する機関・PSP は即日から Sui 上のステーブルコイン決済を利用可能

### 加盟店視点

- 加盟店が Sui 上でステーブルコイン受け取りを設定する際、ガストークン用の SUI 残高管理が不要になる
- 送金手数料 $0.00 は、マイクロペイメントやエージェント向けの少額高頻度決済に適した条件

### プロダクト視点

- エージェント決済インフラで Sui チェーンを選択する際のコスト・複雑性が低下。エージェントがステーブルコインのみを保有・管理すれば決済を実行できる
- x402 の Sui 対応（既報：Base・Polygon・Arbitrum・World・Solana に次ぐ拡大）と合わせると、Sui は「ガスレス × x402 対応」という差別化ポジションを持つ

### 規制 / リスク視点

- ガスレス設計は技術的改善だが、AML スクリーニング・Travel Rule の適用対象となるトランザクション範囲に変更はない
- Fireblocks の KYT・Travel Rule 統合により、機関向け利用でのコンプライアンスは既存フロー内で対応可能

## 我々への示唆

- いま検討すべきこと:
  - 自社の Sui 上のステーブルコイン実装計画がある場合、ガスレス移行後の手数料モデル・ユーザーオンボーディング設計を見直す
- 後で深掘りすべきこと:
  - エージェント決済フローにおける Sui × Fireblocks の実装リファレンス（特に Agentic Payments Suite との統合）
  - Base・Solana 等他チェーンでの同種ガスレス機能対応動向
- 今は優先度が低いこと:
  - Sui 固有の DeFi エコシステム動向（決済インフラ以外の文脈）

## ありそうな示唆

- ガスレス機能が Sui の「決済チェーン」ポジショニングを強化し、x402 対応チェーンの中での競合優位を高める可能性

## 推測 / 監視ポイント

- Sui のガスレス機能採用後の USDC 取引量の変化（決済ユースケースの比率増加）
- 他の x402 対応チェーン（Base・Arbitrum・Solana）がガスレスまたは同等のシンプル化機能を追加するか

## 未解決の論点

- ガスレス機能のトランザクションコスト負担はどこに帰属するか（バリデーターへの補填メカニズム）
- エージェント決済フローでのバッチ送金（並行実行）時の挙動

## 参考リンク

- 一次情報: [PR Newswire（2026-05-20）](https://www.prnewswire.com/news-releases/sui-launches-gasless-stablecoin-transfers-with-support-from-fireblocks-302778111.html)
- 補足情報: [Sui ブログ](https://blog.sui.io/sui-launches-gasless-stablecoin-transfers-with-support-from-fireblocks/) / [Decrypt（2026-05-20）](https://decrypt.co/368568/sui-launches-gasless-stablecoin-transfers-with-support-from-fireblocks)

## 重要度

- Medium

## 確からしさ

- High
