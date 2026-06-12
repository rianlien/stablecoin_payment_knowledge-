---
title: "JPMorgan・Citi・BofA・Wells Fargo、The Clearing House 経由でトークン化預金ネットワークを 2027 年上半期に構築予定——ステーブルコイン対抗策"
date: 2026-06-05
source: "Wall Street Journal / CoinDesk / Unchained"
source_url: "https://www.coindesk.com/markets/2026/06/05/jpmorgan-bank-of-america-and-citi-are-going-on-the-blockchain-offensive-with-a-shared-tokenized-network"
entity: "JPMorgan Chase / Citigroup / Bank of America / Wells Fargo / The Clearing House"
category: tokenized-deposits / bank-competition / payment-rails
primary_category: payment-rails
article_published_date: 2026-06-05
underlying_event_date: 2026-06-05
primary_source_date: 2026-06-05
tags:
  - tokenized-deposits
  - bank-competition
  - stablecoin-regulation
  - payment-rails
  - GENIUS-Act
summary: "米国大手銀行（JPMorgan・Citi・BofA・Wells Fargo 等）が、銀行共同所有の The Clearing House を通じてトークン化預金ネットワークを 2027 年上半期に構築すると WSJ が報道。預金をブロックチェーン上でトークン化しながら資金を銀行システム内に維持する設計で、24/7 即時決済を実現する。GENIUS Act・CLARITY Act による stablecoin 普及加速を危機感の直接の背景とする、TradFi による組織的な対抗策。"
implications: "銀行連合のトークン化預金ネットワークが実現すれば、USDC 等のステーブルコインと同等の即時・プログラマブル決済機能が銀行システム内で提供される。エージェント決済の決済レール選択に「銀行トークン vs ステーブルコイン」という新しい軸が加わる。ただし 2027 年上半期目標は Fiserv FIUSD（7 月ローンチ）より遅く、短期的には USDC の優位は変わらない。"
importance: High
confidence: Medium（WSJ 報道・銀行数行が参加意向を示すが、まだ公式計画発表段階ではない）
follow_up: "The Clearing House の公式発表、パイロット銀行名・参加規模の開示、GENIUS Act 準拠設計の詳細、x402/AP2 との統合計画、2027 Q1 パイロット開始確認"
---

## 概要

- JPMorgan・Citi・Bank of America・Wells Fargo 等の米国大手銀行が、銀行共同所有の The Clearing House を通じてトークン化預金ネットワークを 2027 年上半期に構築する計画を WSJ が報道（2026-06-05）
- 設計：従来の銀行預金をブロックチェーン上でトークン化し、銀行システム内に資金を維持しながら 24/7 即時決済・プログラマブルな資金移動を実現する
- 動機：GENIUS Act・CLARITY Act によるステーブルコイン普及への危機感——預金の暗号資産ウォレットへの流出（デポジット・フライト）を防ぐ組織的対応

## 何が起きたか

- WSJ が 2026-06-05 に、JPMorgan・Citi・BofA・Wells Fargo らがトークン化預金ネットワーク構築計画を検討していると報道
- ネットワークの運営主体は The Clearing House（大手銀行が共同所有するリアルタイム決済会社）
- 目標タイムライン：2027 年上半期
- ターゲット市場：大企業（マルチナショナル）のプログラマブル財務管理・リアルタイム流動性管理・クロスボーダー決済

## 確認された事実

- 参加予定銀行：JPMorgan Chase・Citigroup・Bank of America・Wells Fargo（CoinDesk・Unchained が確認）
- 運営：The Clearing House（参加銀行が共同所有）
- 目標時期：2027 年上半期
- 設計：従来の銀行預金をブロックチェーントークンに変換し、銀行システム内に資金を維持
- 特性：24/7 即時転送（既存のバッチ決済サイクルを排除）
- 動機：GENIUS Act・CLARITY Act による stablecoin への預金流出リスクへの対応

## なぜ重要か

### 決済事業者視点

- 米国決済業界の「既存決済大手（Visa・Mastercard・Stripe）がステーブルコインに対応」という動きと並行して、銀行業界が「ステーブルコインと競合する独自インフラ」を構築する動きが同時進行。決済レールが「Visa/MC ステーブルコイン精算 vs 銀行トークン化預金」に分岐する可能性
- The Clearing House は既存の RTP（Real-Time Payments）ネットワークも運営しており、既存の即時決済インフラとの統合設計が想定される

### 加盟店視点

- 実現すれば、銀行口座から直接発行されるトークンでの支払いが可能になる。「USDC（Circle 発行）を使わずに、銀行口座のステーブルコイン等価物」で支払う経路ができる
- エージェント決済を行う企業（大企業・API 事業者）が、銀行口座から直接エージェントに資金を供給できるインフラになりうる

### プロダクト視点

- x402・AP2・CPN 等の現行エージェント決済プロトコルは USDC 前提。銀行トークン化預金が普及した場合、「どのトークンで決済するか」のマルチ通貨対応が必要になる
- 2027 年上半期の目標は現行のステーブルコイン展開（USDC・RLUSD 等の 2026 年本番稼働）より遅く、短中期の設計への直接影響は限定的

### 規制 / リスク視点

- 銀行が発行するトークン化預金は FDIC 保険の対象となる可能性が高く、ステーブルコインの「FDIC 保険なし」問題を回避できる
- GENIUS Act の PPSI（Permitted Payment Stablecoin Issuer）要件との関係：銀行が発行する場合、PPSI 認定プロセスを経由せずに連邦・州の既存銀行規制で対応できる可能性がある

## 我々への示唆

- いま検討すべきこと:
  - 銀行トークン化預金と USDC の共存シナリオ（2027 年以降）を前提に、マルチ通貨・マルチレール対応の設計コストを概算する
  - The Clearing House の公式発表・パイロット銀行名の開示をトリガーとして、既存の x402/CPN 設計への影響を評価する体制を整える
- 後で深掘りすべきこと:
  - 銀行トークン化預金と USDC の技術的・規制的な互換性（相互交換可能か、それとも完全別系統か）
  - Fiserv FIUSD（7 月ローンチ目標）と The Clearing House ネットワークの設計上の類似点・差異
- 今は優先度が低いこと:
  - 2027 年上半期という目標時期は 1〜1.5 年先であり、現時点での設計変更は不要

## ありそうな示唆

- 銀行業界が「ステーブルコインへの預金流出」を本格的に危機として認識し、集団的な対応策を取り始めたことの証左。GENIUS Act・CLARITY Act の立法がステーブルコイン普及を加速するリスクへの防衛的な動きとして解釈できる
- Fiserv FIUSD（各銀行独自発行モデル）と The Clearing House ネットワーク（銀行連合の共有インフラ）が両方進む場合、「銀行系トークン化ドル」は複数の発行形態に分散する可能性がある

## 推測 / 監視ポイント

- The Clearing House の公式発表タイミング——WSJ 報道から 6 ヶ月以内に公式発表が出るか
- 参加銀行数の拡大（現在 JPMorgan・Citi・BofA・Wells Fargo の 4 行、他の大手銀行が追随するか）
- GENIUS Act 最終規則（7/18 デッドライン）との整合性——銀行トークン化預金が PPSI の定義に含まれるかどうか
- x402・AP2 や Mastercard AP4M が銀行トークン化預金への対応を発表するか

## 未解決の論点

- 銀行トークン化預金は ERC-20 等のオープン標準か、The Clearing House 独自の閉じた設計か
- ステーブルコイン（USDC 等）と銀行トークン化預金の相互交換性——クロスレール決済が可能か
- AI エージェントが銀行トークン化預金を直接使って自律決済できる設計になるか（x402 のような API 連携）

## 参考リンク

- 一次情報: [CoinDesk（2026-06-05）](https://www.coindesk.com/markets/2026/06/05/jpmorgan-bank-of-america-and-citi-are-going-on-the-blockchain-offensive-with-a-shared-tokenized-network)
- 補足情報: [Unchained（2026-06-05）](https://unchainedcrypto.com/jpmorgan-citi-bofa-and-wells-fargo-plan-2027-tokenized-deposit-network-as-banks-move-to-counter-stablecoins/)
- 補足情報: [Genfinity（2026-06-05）](https://genfinity.io/2026/06/05/jpmorgan-citi-bofa-tokenized-deposit-network-2027/)

## 重要度

- High

## 確からしさ

- Medium（WSJ 報道・銀行各行が参加意向、公式計画発表ではない段階）
