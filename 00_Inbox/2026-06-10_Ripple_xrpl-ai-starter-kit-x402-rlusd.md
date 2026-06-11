---
title: "Ripple、XRPL AI Starter Kit を公開——x402 プロトコルが初めて非 EVM チェーン（XRPL）に対応し RLUSD でエージェント決済が可能に"
date: 2026-06-10
source: "Ripple / The Block / PYMNTS / CoinMarketCap"
source_url: "https://www.theblock.co/post/404243/ripple-launches-toolkit-for-agentic-payments-on-xrpl"
entity: "Ripple / RippleX"
category: x402 / machine-payments
primary_category: machine-payments
article_published_date: 2026-06-10
underlying_event_date: 2026-06-10
primary_source_date: 2026-06-10
tags:
  - x402
  - machine-payments
  - agentic-commerce
  - stablecoin-payments
  - RLUSD
summary: "Ripple が 2026-06-10、XRP Ledger（XRPL）を x402 プロトコルの対応チェーンとして追加（パートナー t54 Labs が実装貢献）し、開発者向けの「XRPL AI Starter Kit」を公開。AI エージェントが XRP または RLUSD（Ripple の USD 担保ステーブルコイン）を使って API・コンピューティング・デジタルサービスの代金を x402 プロトコル経由で支払えるようになる。XRPL の 3〜5 秒確定ファイナリティ（ペンディングなし）とオンチェーン DEX（RLUSD ⇔ 他通貨交換）が特徴。Mastercard AP4M の launch partner（RippleX）として同日参加。"
implications: "x402 プロトコルが初めて非 EVM チェーンに対応した。XRPL は金融機関・銀行への採用実績が豊富であり（Ripple の XRP On-Demand Liquidity / ODL）、Ripple の既存パートナー金融機関が XRPL 経由でエージェント決済インフラを構築するルートが生まれた。RLUSD が x402 の第 3 の主要ステーブルコイン（USDC・PYUSD に続く）として機能する可能性がある。"
importance: Medium
confidence: High
follow_up: "XRPL x402 実装の本番採用状況（件数・金額・開発者数）、RLUSD の x402 取引シェア、t54 Labs の技術仕様の公開（XRPL への x402 実装の技術的詳細）、AP4M での XRPL/RLUSD 利用の実際のユースケース"
---

## 概要

Ripple が 2026 年 6 月 10 日、x402 プロトコルの対応チェーンとして XRP Ledger（XRPL）を追加し、開発者向けツールキット「XRPL AI Starter Kit」を公開した。Mastercard AP4M 発表と同日に行われ、RippleX は AP4M の 35 社超の launch partner の一社として参加。XRPL 上で RLUSD または XRP を使って AI エージェントが API・コンピューティング・デジタルサービスの代金を支払える最初の完全なツールチェーンが整った。

## 何が起きたか

- **XRPL の x402 対応**：
  - Ripple のパートナー t54 Labs が XRPL を x402 プロトコルの対応チェーンとして実装・貢献
  - これまで Base・Solana・Arbitrum 等の EVM 互換チェーンが主要対応チェーンだったが、初めて非 EVM チェーン（XRPL）が加わった
  - XRPL の特徴として訴求：3〜5 秒のファイナリティ（確定 or 失効の二択で「ペンディング」状態なし）、エージェントがポーリングループ・リトライロジックを実装せずに次ステップに進める設計

- **XRPL AI Starter Kit の内容**：
  - XRPL 上でエージェント決済アプリを構築するための開発者向けツール・統合機能のセット
  - 対応トークン：XRP（ネイティブ）・RLUSD（Ripple の USD 担保ステーブルコイン）
  - RLUSD は XRPL ネイティブ発行で、XRPL の DEX を通じて他通貨と交換可能
  - ターゲットユースケース：API 課金・コンピューティングリソース・デジタルサービスの自律決済

- **Mastercard AP4M との接続**：
  - 同日に Mastercard が AP4M をローンチし、RippleX が launch partner として参加
  - AP4M は RLUSD/XRPL での決済をサポートすることを確認

- **Ripple Insights による発表**：
  - Ripple 公式ブログ「Building the Future of Agentic Payments: Introducing the XRP Ledger AI Starter Kit」で詳細を公開

## 確認された事実

- 発表日：2026-06-10
- x402 XRPL 対応の実装者：t54 Labs（AP4M launch partner でもある）
- 対応トークン：XRP・RLUSD
- ファイナリティ時間：3〜5 秒（確定的、ペンディング状態なし）
- XRPL DEX：RLUSD を他通貨に交換可能
- AP4M への参加：RippleX が 35 社超のパートナーの一社として参加
- 出典：Ripple 公式 Insights ブログ・The Block・PYMNTS・CoinMarketCap が同日報道

## なぜ重要か

### 決済事業者視点

- XRPL は Ripple の ODL（On-Demand Liquidity）を通じて多くの送金・金融機関に使われているチェーン。これらの機関がエージェント決済のために XRPL を選ぶ場合、x402 プロトコルが利用できる
- RLUSD はエンタープライズグレードの USD 担保ステーブルコインとして設計されており、USDC に次ぐ x402 エコシステムの主要ステーブルコインになる候補

### 加盟店視点

- XRPL を基盤とする金融機関・フィンテックと取引する加盟店にとって、RLUSD/XRPL 経由のエージェント決済が選択肢に加わる
- 現時点では XRPL x402 の加盟店採用実績は未確認——Base/Solana と比較したエコシステムの成熟度差が採用速度に影響する

### プロダクト視点

- x402 の「XRPL + RLUSD 対応」により、エージェント決済プロダクトが利用するチェーン・ステーブルコインの選択肢が増加。Base の USDC を使った設計が「最短路」だが、XRPL/RLUSD が機関向けにより適する場合がある
- XRPL の「ペンディングなし確定ファイナリティ」はエージェントのループ設計を簡素化する——「支払い完了を待つ間に次のアクションを止める」デッドロックが起きにくい

### 規制 / リスク視点

- RLUSD は Ripple によってエンタープライズ向けに設計されており、GENIUS Act 準拠の PPSI 申請状況が重要な監視ポイント。Ripple の既存規制問題（SEC との和解 2024 年）の後処理が RLUSD の米国内採用に影響する可能性
- XRPL の「非 EVM」性質は、EVM チェーン向けに設計されたスマートコントラクトベースのエスクロー（Kustodia 等）と直接統合できない可能性がある

## 我々への示唆

- いま検討すべきこと:
  - 自社プロダクトが XRPL 対応の金融機関パートナーと連携している場合、RLUSD/XRPL 経由のエージェント決済の採用可能性を評価する
  - t54 Labs の XRPL x402 実装仕様が公開されたら、自社の x402 統合に XRPL チェーンサポートを追加するコストを評価する
- 後で深掘りすべきこと:
  - RLUSD の GENIUS Act PPSI 申請状況（Ripple は公式声明を出していない）——PPSI 認定を受けていない場合、GENIUS Act 施行後の米国内使用に制限がかかる可能性
  - XRPL x402 の本番採用データ——t54 Labs が実装から本番取引件数が出るまでどれくらいかかるか
- 今は優先度が低いこと:
  - XRP（ネイティブトークン）での x402 決済——エージェント商取引の主流はステーブルコイン（RLUSD）であり、XRP 価格変動リスクのある XRP 建て取引は限定的なユースケース

## ありそうな示唆

- t54 Labs が AP4M と x402 XRPL 対応の両方に関与していることから、AP4M の「Mastercard 決済保証 + XRPL/RLUSD 決済」というユースケースが最初の実用事例になる可能性がある
- Ripple の銀行向けネットワーク（ODL パートナー）が AP4M 経由でエージェント間 B2B 決済を RLUSD で行うユースケースが、まず金融機関向け市場で立ち上がる可能性

## 推測 / 監視ポイント

- Ripple の SEC 和解後の RLUSD 米国内展開の法的クリア状況——GENIUS Act PPSI 申請の有無
- XRPL x402 が x402 Foundation のメインチェーンとして Base に次ぐ採用を獲得するまでの時間軸
- Mastercard AP4M での XRPL/RLUSD 利用の最初の実用ケースの発表

## 未解決の論点

- RLUSD の GENIUS Act PPSI 申請状況・米国内での法的位置づけ
- t54 Labs の XRPL x402 実装のスマートコントラクト/プロトコル設計の詳細
- XRPL のアカウント要件（最低残高 XRP 10 枚 = リザーブ）がエージェント決済の経済性に与える影響

## 参考リンク

- 一次情報: [The Block（2026-06-10）](https://www.theblock.co/post/404243/ripple-launches-toolkit-for-agentic-payments-on-xrpl)
- 補足情報: [PYMNTS（2026-06-10）](https://www.pymnts.com/blockchain/2026/ripple-targets-agentic-payments-market-with-xrpl-starter-kit/)
- 補足情報: [CoinMarketCap（2026-06-10）](https://coinmarketcap.com/academy/en/article/ripple-launches-ai-agent-payments-with-xrp-and-rlusd)
- 補足情報: [The Defiant（2026-06-10）](https://thedefiant.io/converge/tradfi-and-fintech/ripple-xrpl-ai-starter-kit-mastercard-agent-pay-machines)
- 一次情報（Ripple 公式）: [Ripple Insights](https://ripple.com/insights/xrpl-ai-starter-kit/)

## 重要度

- Medium

## 確からしさ

- High（Ripple 公式 Insights・The Block・複数専門メディアによる確認）
