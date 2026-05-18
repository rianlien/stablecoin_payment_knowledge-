---
title: "x402 プロトコルが Arbitrum に正式対応——AI エージェントが Arbitrum 上のステーブルコイン（USDC 等）で API・サービスをマイクロ決済可能に。Coinbase x402 Foundation 管理の対応チェーンが 5 本に"
date: 2026-05-14
source: "Phemex News / Cryptowisser / Arbitrum Foundation Blog"
source_url: "https://phemex.com/news/article/x402-protocol-launches-on-arbitrum-for-aipowered-microtransactions-81450"
entity: "x402 Foundation / Arbitrum Foundation / Coinbase"
category: "protocol"
primary_category: "agentic-commerce"
article_published_date: 2026-05-14
underlying_event_date: 2026-05-14
primary_source_date: 2026-05-14
tags:
  - x402
  - Arbitrum
  - agent-payments
  - protocol
  - agentic-commerce
summary: "Coinbase が開発した x402 プロトコルが Arbitrum ネットワークに正式対応。AI エージェントが Arbitrum 上のステーブルコインで API・ソフトウェア・サービスをマイクロ決済できるようになった。Linux Foundation 傘下の x402 Foundation が管理し、Base・Polygon・Arbitrum・World・Solana の 5 チェーンで Coinbase ホスト型ファシリテーターが利用可能。"
implications: "x402 の対応チェーン拡大により、Arbitrum エコシステムの DeFi・API プロバイダーが自律エージェントの決済対象として加わる。チェーン選択の多様化はエージェント開発者のユースケース適合範囲を広げる。"
importance: Medium
confidence: Medium
follow_up: "Arbitrum 上の x402 利用トランザクション数・ボリュームの推移、Arbitrum 固有のステーブルコイン（USDC.e・USDT 等）の対応状況、x402 Foundation の次の対応チェーン"
---

## 概要

2026 年 5 月 14 日（木）、Arbitrum Foundation が Coinbase の x402 プロトコルの Arbitrum 対応を X（旧 Twitter）で発表した。AI エージェントが Arbitrum 上のステーブルコインを用いて API・コンテンツ・ソフトウェアをマイクロ決済できる。x402 を管理する Linux Foundation 傘下の x402 Foundation では、Base・Polygon・Arbitrum・World・Solana の 5 チェーンで Coinbase ホスト型ファシリテーターが提供される。

## 何が起きたか

- **x402 の Arbitrum 対応**：Coinbase Developer Platform（CDP）のファシリテーターサービスが Arbitrum に対応し、ERC-20 決済（USDC 等）を x402 プロトコルで処理可能に
- **対応チェーン一覧（確認済み）**：Base・Polygon・Arbitrum・World・Solana（計 5 チェーン）
- **無料枠**：月 1,000 トランザクションまでプロトコル手数料ゼロ
- x402 プロトコル全体の実績：165M+ トランザクション処理（69,000 以上のアクティブボット）、Base 上 119M+ トランザクション・Solana 上 35M+ トランザクション、年率約 $600M ボリューム（2026 年 3 月時点）
- x402 は 2026 年 4 月 28 日時点で月間 75M+ トランザクション・$24M+ ボリューム・2 秒決済という数値も報告されている（出典の測定タイミングに差異あり、推定含む）
- 管理体制：x402 Foundation（Linux Foundation 傘下）、サポート企業 20 社超（Cloudflare・Stripe・AWS・Google・Visa・Circle・Solana Foundation 等）

## 確認された事実

- Arbitrum Foundation が Arbitrum の x402 対応を X で発表（2026-05-14）
- 対応チェーン：Base・Polygon・Arbitrum・World・Solana（Coinbase CDP ドキュメントで確認）
- プロトコル手数料ゼロ・月 1,000 トランザクションの無料枠（CDP ドキュメントより）
- x402 は Coinbase + Cloudflare 共同開発の HTTP 決済標準（HTTP 402 ステータスコードを活用）

## なぜ重要か

### 決済事業者視点

- x402 の対応チェーン拡大は、「エージェントがどのチェーン上で動くか」に依存せず x402 標準で決済できるユニバーサル性を高める。Arbitrum エコシステムの Uniswap・GMX・Aave 等の DeFi インフラと組み合わせれば、DeFi 操作の自動課金が可能になる
- Arbitrum は EVM 互換 L2 として最大 TVL を持つチェーンの一つ。企業・機関向け Arbitrum One/Nova の採用が x402 決済の B2B ユースケースを広げる

### 加盟店視点

- Arbitrum 上で API・コンテンツ・SaaS を提供する事業者がターゲット。x402 エンドポイントを実装するだけでエージェントからのマイクロペイメントを受け取れる

### プロダクト視点

- Base + Solana + Arbitrum の 3 チェーン対応により、USDC の主要流通チェーン上での x402 決済がほぼカバーされた。今後の拡張は Ethereum mainnet・OP Mainnet（Optimism）・zkSync 等が候補

### 規制 / リスク視点

- Arbitrum は米国投資家に広く普及している EVM L2。規制当局がスマートコントラクト決済への監督を強化する場合、Arbitrum 上の x402 トランザクションも対象になりうる

## 我々への示唆

- いま検討すべきこと:
  - Arbitrum 上の x402 実装を試し、Base 上の実装（Cryptorefills 等）との遅延・手数料差を比較する
- 後で深掘りすべきこと:
  - Arbitrum 固有のステーブルコイン（USDC.e・bridged USDT）が Coinbase ファシリテーターで対応されているか確認
  - x402 Foundation の技術ガバナンス（アップグレード・標準変更のプロセス）
- 今は優先度が低いこと:
  - World チェーン（Worldcoin）の x402 対応詳細（消費者向けユースケースが主）

## ありそうな示唆

- x402 が Base・Solana・Arbitrum を標準対応したことで、エージェント開発者が「どのチェーン上に決済インフラを組むか」を設計する際の選択肢が実質的に標準化された。今後は「x402 vs AP2 vs Circle Nanopayments」というプロトコル間の競争に議論が移る可能性がある

## 推測 / 監視ポイント

- x402 の累積トランザクション数・ボリューム成長率（月次データが利用可能か）
- Arbitrum 固有の x402 開発者採用数（サンプル実装・OSS リポジトリの Fork 数等）
- AP2（AgentPayments Protocol）・Circle Nanopayments との棲み分け事例

## 未解決の論点

- Arbitrum 上の x402 で利用できる具体的なステーブルコインの種類（native USDC / bridged USDC.e の区別）
- x402 プロトコル数値（75M/165M トランザクション）の測定方法の差異（同一事象の異なる集計タイミングか、別々のデータか）——推定含む

## 参考リンク

- 一次情報: [Phemex News（2026-05-14）](https://phemex.com/news/article/x402-protocol-launches-on-arbitrum-for-aipowered-microtransactions-81450)
- 補足情報: [Cryptowisser](https://www.cryptowisser.com/news/x402-by-coinbase-is-now-live-on-arbitrum) / [Arbitrum Foundation Blog](https://blog.arbitrum.foundation/x402-payments-on-arbitrum/) / [Coinbase CDP ドキュメント](https://docs.cdp.coinbase.com/x402/welcome)

## 重要度

- Medium

## 確からしさ

- Medium（Phemex / Cryptowisser 報道確認、Arbitrum Foundation ブログ記事あり。ただし記事日付の一次確認は間接的）
