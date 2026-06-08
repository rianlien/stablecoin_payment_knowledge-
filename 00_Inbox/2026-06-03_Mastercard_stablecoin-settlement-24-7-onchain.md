---
title: "Mastercard、ステーブルコイン決済を 24/7 本番展開——USDC・PYUSD・RLUSD を 8 チェーンで受け付け"
date: 2026-06-05
source: Mastercard プレスリリース / The Block / CoinDesk
source_url: https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
entity:
  - Mastercard
  - Circle（USDC）
  - Paxos（PYUSD・USDG・USDP）
  - Ripple（RLUSD）
  - SoFi（SoFiUSD）
  - Cross River
  - Lead Bank
  - Nuvei
  - ARQ（DolarApp）
  - CBW Bank
category: stablecoin-payments
primary_category: stablecoin-payments
article_published_date: 2026-06-03
underlying_event_date: 2026-06-03
primary_source_date: 2026-06-03
tags:
  - stablecoin
  - stablecoin-payments
  - payment-rails
  - Mastercard
  - merchant-PSP-readiness
summary: "Mastercard が 2026-06-03、USDC・PYUSD・RLUSD を含む規制済みステーブルコインを使った 24/7 オンチェーン決済を本番展開。Arbitrum・Base・Canton・Ethereum・Polygon・Solana・Tempo・XRPL の 8 チェーンに対応。先行採用パートナーは Cross River・Lead Bank・Nuvei・ARQ・CBW Bank。米国・ラテンアメリカから開始し、順次グローバル展開へ。"
implications: "カードネットワークレベルで週末・祝日含む 24/7 ステーブルコイン決済が標準化されると、エージェント決済の決済タイミング制約（通常営業日・バッチ処理）が解消される。Mastercard 加盟店での AI エージェント購買の実現可能性が高まる。"
importance: High
confidence: High
follow_up: "Mastercard エージェント決済（Agent Pay / Verifiable Intent）との統合——既存の Agentic Tokens が新ステーブルコイン決済レールで利用可能になるか確認。Visa の対抗動向（Visa TAP + ステーブルコイン決済の組み合わせ更新有無）。"
---

## 概要

Mastercard が 2026 年 6 月 3 日に公式プレスリリースで、カードネットワーク上でのステーブルコインを使った 24/7 オンチェーン決済の展開を発表。USDC（Circle）・PYUSD・USDG・USDP（Paxos）・RLUSD（Ripple）・SoFiUSD（SoFi）の 6 種ステーブルコインが対象。Arbitrum・Base・Canton・Ethereum・Polygon・Solana・Tempo・XRPL の 8 チェーンでの決済を受け付ける。

## 何が起きたか

- Mastercard が正式に「カードネットワーク上のステーブルコイン決済」を本番化
- 対応ステーブルコイン：USDC（Circle）、PYUSD・USDG・USDP（Paxos）、RLUSD（Ripple）、SoFiUSD（SoFi）
- 対応ブロックチェーン：Arbitrum、Base（x402 の主要チェーン）、Canton、Ethereum、Polygon、Solana、Tempo（Stripe/MPP のチェーン）、XRPL
- 先行採用パートナー：Cross River、Lead Bank、Nuvei、ARQ（旧 DolarApp、ラテンアメリカ向けフィンテック）、CBW Bank
- 地域：米国・ラテンアメリカから開始。その後グローバル展開予定（時期・地域未開示）
- 従来の Mastercard 決済（バッチ処理・平日のみ）を「置き換えるのではなく補完する」設計

## 確認された事実

- Mastercard 公式プレスリリース（2026-06-03）で確認
- 追加機能として「Intraday（日中）決済」と「週末・祝日決済」も同時発表
- Mastercard は 2026 年初頭に BVNK を買収し、ステーブルコイン決済インフラへの布石を打っていた
- 2024 年以降 Mastercard は Aptos・Polygon・Solana 等でのステーブルコイン決済テストを実施しており今回はその本番化

## なぜ重要か

### 決済事業者視点

- カードネットワーク本体がステーブルコイン決済を 8 チェーン同時対応で本番化したことは、PSP が「Mastercard 加盟店でのステーブルコイン受け取り」を顧客に提供できる基盤が整ったことを意味する
- Nuvei のような PSP が先行採用パートナーに含まれており、Mastercard 経由のステーブルコイン決済を PSP が顧客（加盟店）に提供するモデルが実証される
- Base と Solana が対応チェーンに含まれており、x402（Base 主体）や MPP（Stripe/Tempo チェーン）と組み合わせた設計が可能になる

### 加盟店視点

- 週末・祝日を含む 24/7 決済は、クロスボーダー B2B 決済の遅延リスクを大幅に低減
- AI エージェントが時間外に自律的に発注→決済する際に「営業日外は決済不可」という制約が解消される
- ラテンアメリカ（ARQ/DolarApp 経由）が最初の展開地域——ドル建て決済需要の高い新興市場での先行普及が見込まれる

### プロダクト視点

- Mastercard の Verifiable Intent（エージェント決済認証）+ 今回のステーブルコイン決済レール = AI エージェントが Mastercard ネットワーク上でステーブルコインによる 24/7 決済を実行できる技術的組み合わせが完成
- Tempo（Stripe の MPP 専用チェーン）が Mastercard 対応チェーンに含まれていることは、MPP と Mastercard の統合を示唆する可能性がある（要確認）
- Base が対応チェーンに含まれているため、x402 のトランザクションが Mastercard 決済ネットワークに着地するパスが理論上存在する

### 規制 / リスク視点

- USDC・PYUSD・RLUSD・SoFiUSD はいずれも GENIUS Act の PPSI 要件を満たす、または満たす見込みの発行体から発行されている（発表時点での整理）
- 8 チェーンへの同時対応は「チェーン選択の分散」としてシステミックリスクを低減しているが、クロスチェーンのリコンシリエーション複雑性は増す

## 我々への示唆

- いま検討すべきこと:
  - 自社がエージェント決済を設計する際に「Mastercard ステーブルコイン決済 × Agent Pay（Verifiable Intent）」のスタックが利用できるかを確認——Mastercard 発行カード + ステーブルコイン着地の両立が技術的に実現しているかを Cross River 等に確認
  - Base が Mastercard 対応チェーンに含まれている点を注目——x402 取引が最終的に Mastercard 決済ネットワークに着地するフローが実装されれば、x402 のアドレスブルマーケットが飛躍的に拡大する
- 後で深掘りすべきこと:
  - Tempo（Stripe のチェーン）が Mastercard 対応チェーンに含まれる意味——MPP と Mastercard 決済ネットワークの統合が正式に進むかどうかを Stripe/Tempo 側の発表で確認
  - Mastercard Agent Pay（Verifiable Intent）とステーブルコイン決済レールの統合タイムライン
- 今は優先度が低いこと:
  - 具体的な加盟店への提案は、Mastercard のステーブルコイン決済 API 仕様が公開されてから

## ありそうな示唆

- Mastercard のステーブルコイン決済本番化は、短期的には Visa のステーブルコイン決済（9 チェーン・4 月発表）との「カードネットワーク競争」を加速させ、加盟店・PSP がどちらのレールを選ぶかの決定を迫る
- 両社が同時にステーブルコイン決済本番化を進めることで「カードレールでのステーブルコイン決済」が 2026 年下半期に業界標準として定着する可能性が高まった

## 推測 / 監視ポイント

- Mastercard の次の発表：アジア太平洋・欧州への展開タイムライン
- Mastercard Agentic Tokens（Verifiable Intent）との統合発表
- Visa との競争動向（Visa も類似機能を 2026 年中に拡張するか）
- Nuvei・Cross River が Mastercard ステーブルコイン決済を使った最初の商業取引の発表

## 未解決の論点

- Tempo チェーンが Mastercard 対応に含まれる意図（Stripe との協調か偶然か）
- Canton ブロックチェーンの採用背景（Daml/Canton は機関向けプライベートチェーン——どの金融機関が Canton 経由で利用するか）
- ステーブルコイン決済とフィアット決済の精算の整合方式（ネッティング vs. グロス）

## 参考リンク

- 一次情報: [Mastercard プレスリリース（2026-06-03）](https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html)
- 補足情報: [The Block（2026-06-03）](https://www.theblock.co/post/403474/mastercard-expands-stablecoin-settlement-options-with-usdc-pyusd-and-rlusd), [CoinDesk（2026-06-03）](https://www.coindesk.com/markets/2026/06/03/mastercard-expands-on-chain-settlement-in-bet-on-stablecoins-and-always-on-finance)

## 重要度

- High

## 確からしさ

- High（Mastercard 公式プレスリリースで確認済み）
