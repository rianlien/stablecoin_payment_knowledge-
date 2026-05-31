---
title: "Block / Cash App、USDC 決済を 6000 万ユーザーに段階展開開始"
date: 2026-05-27
source: CoinDesk / The Block
source_url: https://www.coindesk.com/business/2026/05/27/block-kicks-off-cash-app-s-phased-stablecoin-roll-out-to-its-nearly-60-million-users
entity: Block / Cash App
category: stablecoin-payments / consumer-wallet / payment-rails
primary_category: stablecoin-payments
article_published_date: 2026-05-27
underlying_event_date: 2026-05-27
primary_source_date: 2026-05-27
tags:
  - stablecoin
  - USDC
  - consumer-payments
  - machine-payments
  - agent-commerce-infrastructure
summary: "Block が Cash App の約 6000 万 MAU に対して USDC 送受信機能を段階展開開始。初回フェーズは約 25%（1500 万ユーザー）に提供、Solana / Ethereum / Polygon / Arbitrum 対応。手数料無料、受け取り時は自動的に USD に変換。CEO Jack Dorsey はビットコン偏重姿勢から転換、需要に応じた対応と説明"
implications: "米国最大級の消費者向けフィンテックアプリが USDC を標準決済手段として取り込んだことで、AI エージェントが Cash App 経由で人間ユーザーへ送金・受け取りするシナリオの実現可能性が高まった"
importance: High
confidence: High
follow_up: "全 6000 万ユーザーへの展開完了時期、AI エージェントから Cash App への USDC 送金の対応有無（API 公開状況）、NY 州ユーザー向けの対応見通し"
---

## 概要
- Block（旧 Square）が Cash App の USDC 送受信機能を 2026 年 5 月 27 日より段階展開開始
- 初回フェーズ：全 MAU 約 6000 万の 25% 程度（約 1500 万ユーザー）から提供
- 対応ネットワーク：Solana、Ethereum、Polygon、Arbitrum

## 何が起きたか
- Cash App ユーザーが onchain ウォレットアドレスを使って USDC を送受信できるようになった
- Cash App への着金 USDC は自動的に USD 残高に変換される（ユーザーは暗号資産を保有せずに受け取れる）
- 全ての USDC 送受信取引について手数料を無料化
- 本人確認（ID 検証）済みユーザーに上限設定：日次送金 $2,000（週次 $5,000）、週次受取 $10,000
- ニューヨーク州ユーザーおよびスポンサードアカウントは対象外

## 確認された事実
- 出典：CoinDesk 独自取材（2026-05-27 付け報道「Block kicks off Cash App's phased stablecoin roll out」）
- The Block も同日独立報道で確認
- CEO Jack Dorsey は従来の「ビットコインのみ」路線から転換し、ユーザー需要への対応と説明
- 週内に全ユーザーへの展開を予定と一部報道

## なぜ重要か

### 決済事業者視点
- Cash App は米国の消費者向けフィンテックで最大規模のプレイヤーのひとつ（MAU 約 6000 万）。Venmo・Zelle との直接競合ポジションで USDC を標準機能化することは、stablecoin を「主流 P2P 決済」として位置づける上で重大な象徴的意義を持つ

### 加盟店視点
- 直接の加盟店向け機能ではないが、Cash App Pay（オフライン決済）との連携が将来的に整備されれば、USDC 残高から実店舗・EC 支払いへの動線が生まれる

### プロダクト視点
- USDC 受け取りを USD 自動変換することで「ユーザーに暗号資産リテラシーを求めない」設計。これは AI エージェント決済インフラが一般消費者に届く際の設計モデルとして参考になる
- Solana 対応が筆頭に来ている点は、Solana の x402 対応エコシステムとの接続可能性を示唆

### 規制 / リスク視点
- GENIUS Act 施行（2026-07-18）を見越した先行対応の可能性。PPSI（Permitted Payment Stablecoin Issuer）規制が確定する前の「実績づくり」という側面がある
- NY 州除外は BitLicense の制約によるものと見られる

## 我々への示唆
- いま検討すべきこと:
  - Cash App API を経由して AI エージェントが USDC を送受信できるかを確認——公開 API / MCP Server の有無を調査
  - Cash App の USDC 受け取り→USD 自動変換モデルを、自社プロダクトの「エージェント決済→ユーザー可視化」フローの参照例として評価
- 後で深掘りすべきこと:
  - Cash App Pay（IRL 決済）との USDC 連携の有無・ロードマップ
  - 将来的な Cash App Agent Wallet 機能の可能性
- 今は優先度が低いこと:
  - 取引上限・NY 除外の詳細条件（短期的に直接影響する事業展開がなければ）

## ありそうな示唆
- Cash App が USDC に対応したことで、「AI エージェントが稼いだ収益をユーザーの Cash App 口座に USDC 送金」というユースケースが技術的に成立するようになった

## 推測 / 監視ポイント
- Cash App が MCP Server を公開し、AI エージェントから直接 USDC 送金できるインターフェイスを提供するかどうか（現時点では未確認）
- Venmo / PayPal が類似機能を追随するタイムライン

## 未解決の論点
- Cash App の USDC 機能は x402 プロトコルとの互換性があるか（今回の発表には x402 への言及なし）
- エージェントからのプログラム的送金への対応（現在は人間ユーザー向けの UI ベース機能と見られる）

## 参考リンク
- 一次情報: [CoinDesk（2026-05-27）](https://www.coindesk.com/business/2026/05/27/block-kicks-off-cash-app-s-phased-stablecoin-roll-out-to-its-nearly-60-million-users)
- 補足情報: [The Block（2026-05-27）](https://www.theblock.co/post/402784/cash-app-lets-users-send-usdc-stablecoins-on-chains-like-solana-and-ethereum)

## 重要度
- High

## 確からしさ
- High
