---
title: "Circle、ガスフリー USDC ナノペイメントをメインネット本番稼働——AI エージェント・API 従量課金向けに 11 チェーン対応"
date: 2026-05-01
source: "Circle 公式 / QuickNode ブログ / CryptoTimes"
source_url: "https://www.circle.com/nanopayments"
entity: "Circle"
category: "プロダクトローンチ"
tags:
  - stablecoin
  - agentic-commerce
  - payments
  - protocol
summary: "Circle が Circle Gateway を基盤とするナノペイメント（Nanopayments）をメインネットで本番稼働。USDC を $0.000001 単位で送付可能なガスフリーマイクロペイメントインフラで、AI エージェント・API 従量課金・マシン決済を主要ターゲットとする。Ethereum・Base・Arbitrum・Polygon 等 11 チェーンに対応し、QuickNode・Alchemy・Goldsky がデイワンパートナーとして参加。"
implications: "x402（Linux Foundation / Coinbase）・Stripe MPP に次ぐ三つ目のアジェンティック・マイクロペイメントインフラが Circle から登場。USDC の発行体が直接マイクロ決済レイヤーを提供することで、決済最終性・コンプライアンス・流動性の垂直統合が可能になる。"
follow_up: "日次実取引量の公開、x402 との相互運用性・競合関係の整理、Stripe MPP との差別化、KYT/AML 義務の帰属整理"
---

## 概要

Circle が Circle Gateway インフラ上で Nanopayments をメインネット本番稼働させた（2026 年 5 月 1 日前後）。ガスフリーで $0.000001 以上の USDC マイクロ送金をミリ秒単位で処理し、数千件をバッチして単一コミットメントとしてオンチェーン決済する仕組みを提供する。当初 2026 年 3 月にテストネットで公開済みで、今回メインネット本番稼働に移行した。

## 何が起きたか

- **ローンチ形態**：メインネット本番稼働（テストネット：2026 年 3 月 4 日、メインネット：2026 年 4 月末〜5 月 1 日）
- **最小決済額**：$0.000001（1 マイクロドル）—— 従来のオンチェーン手数料では経済的に不可能な単位
- **対応チェーン（11 チェーン）**：Ethereum、Arbitrum、Base、Optimism、Polygon PoS、Avalanche、Sei、Sonic、Unichain、HyperEVM、World Chain
- **技術仕組み**：Circle Gateway が数千件の Nanopayment をバッチ集約し、単一のオンチェーンコミットメントとして決済。エンドユーザーはガス代ゼロ
- **ターゲットユースケース**：AI エージェントの API 従量課金、データアクセス料、コンピューティングリソース課金、時間単位のサービス利用など「ペイ・パー・ユース」モデル
- **デイワンパートナー**：QuickNode（ブロックチェーン API プロバイダー）、Alchemy（同）、Goldsky（ブロックチェーンインデックス）
- **決済スピード**：ミリ秒単位での検証・確認

## なぜ重要か

### 決済事業者視点

- Circle が自社発行 USDC のマイクロペイメントレイヤーを直接提供することで、PSP・ブリッジ・アグリゲーターを介さずに AI エージェント決済が完結するルートが整備された
- $0.000001 という単位は従来の Visa/Mastercard レールでは経済的・技術的に不可能。アジェンティック決済特有の「超小額・超高頻度」ユースケースに特化した設計
- バッチ決済によるガスフレス設計は、オンチェーンコストの予測可能性を高め、法人顧客向けの CFO 承認を得やすくなる

### 加盟店視点

- QuickNode・Alchemy などのインフラプロバイダーが従量課金型の API 収益化を USDC で実現できるようになった
- 従来のサブスクリプション型 API 課金から「コール単位課金」へ移行する際のインフラコストが大幅低下

### プロダクト視点

- x402（Coinbase/Linux Foundation）や Stripe MPP と並んで、Circle Nanopayments は三つ目のアジェンティック決済インフラとして登場
- USDC 発行体 Circle が直接レイヤーを提供するため、他 2 つと比べて「決済最終性と USDC 流動性の垂直統合」が最も強い
- 11 チェーン対応は x402（主に Base 中心）よりも広いチェーンカバレッジを持つ

### 規制 / リスク視点

- Circle Gateway がバッチ集約するため、個別エージェントのトランザクションがオンチェーン上で直接可視化されない可能性があり、KYT（Know Your Transaction）の適用単位が不明確
- AI エージェントが自律的に USDC を支出する場合、エージェント所有者・プラットフォーム・Circle のうちどの主体が AML 義務を負うかは既存規制では未解決

## 我々への示唆

- いま検討すべきこと:
  - Circle Nanopayments・x402・Stripe MPP の 3 インフラを比較し、自社プロダクトのエージェント決済設計でどれをベースとするかの方針整理
  - QuickNode/Alchemy の統合事例を参照し、自社 API や SaaS プロダクトへのペイ・パー・ユース課金モデル適用可能性を評価
- 後で深掘りすべきこと:
  - バッチ決済における KYT 義務の帰属（Circle が一括報告主体になるか否か）
  - x402 との相互運用性（Nanopayments API が x402 の HTTP 402 レスポンス仕様に対応するか）
  - メインネット稼働後の実取引量の公開タイミング
- 今は優先度が低いこと:
  - 個別チェーン（Sei・Sonic・HyperEVM 等）への対応詳細

## 未解決の論点

- Circle Nanopayments・x402・Stripe MPP の 3 インフラは競合するか補完するか？各インフラ間の相互運用性はあるか？
- バッチ集約決済における KYT・AML 義務はどの主体に帰属するか（Circle、ノードオペレーター、エージェント所有者）？
- $0.000001 単位の取引に対して、GENIUS Act の AML 要件（例：取引報告閾値）はどのように適用されるか？

## 参考リンク

- 一次情報:
  - [Circle Nanopayments 公式ページ](https://www.circle.com/nanopayments)
  - [Circle ブログ：テストネット発表（2026-03-04）](https://www.circle.com/blog/circle-nanopayments-launches-on-testnet-as-the-core-primitive-for-agentic-economic-activity)
- 補足情報:
  - [QuickNode ブログ：メインネット稼働パートナー発表](https://blog.quicknode.com/nanopayments-powered-by-circle-gateway-live-on-mainnet-with-quicknode/)
  - [CryptoTimes 報道（2026-04-29）](https://www.cryptotimes.io/2026/04/29/circle-introduces-nanopayments-system-for-ultra-small-usdc-transfers/)
  - [既存ノート：Coinbase Agentic.market × x402（2026-04-21）](2026-04-21_Coinbase-x402_agentic-market-launch.md)
  - [既存ノート：Stripe MPP（2026-04-30）](2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments.md)

## 重要度

- High

## 確からしさ

- High（Circle 公式ページ・QuickNode ブログ・複数メディア一致。メインネット稼働の正確な日付は「4 月末〜5 月 1 日」で確認、CryptoTimes 記事は 4 月 29 日付）
