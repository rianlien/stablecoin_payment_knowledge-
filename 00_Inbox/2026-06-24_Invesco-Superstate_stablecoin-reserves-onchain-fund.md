---
title: "Invesco、GENIUS Act 準拠のステーブルコイン準備金向けオンチェーンファンドを SEC に申請（2026-06-24）"
date: 2026-06-28
source: "CoinDesk / The Defiant / en.cryptonomist.ch / techtimes.com"
source_url: "https://www.coindesk.com/business/2026/06/25/asset-management-giant-invesco-files-for-tokenized-fund-targeting-stablecoin-reserve-market"
entity: "Invesco / Superstate"
category: "stablecoin-payments / institutional-adoption / regulation"
primary_category: "stablecoin-payments"
article_published_date: 2026-06-25
underlying_event_date: 2026-06-24
primary_source_date: 2026-06-24
tags:
  - stablecoin
  - regulation
  - payments
  - institutional
  - GENIUS-Act
summary: "運用資産 $2.45T の大手資産運用会社 Invesco が、GENIUS Act 準拠ステーブルコイン発行体向け準備金管理オンチェーンファンドを SEC に申請（2026-06-24）。ファンド名 "Invesco Stablecoin Reserves Onchain Fund"、分類は Rule 2a-7 政府系マネーマーケットファンド、NAV 一定 $1.00。株式トークン化と株主台帳管理は Superstate が担当。効力発生は申請から約 60 日後（2026 年 8 月末）見込み。"
implications: "主要 TradFi 機関が GENIUS Act 準拠の stablecoin 準備金インフラを直接提供し始めた最初の事例。stablecoin 発行体は USDC・RLUSD 等の準備金運用を既存の証券口座から延長する形でオンチェーンで管理できるようになる。BlackRock BUIDL・Franklin Templeton BENJI 等が競合する $4T 準備金市場に Invesco が参入。"
importance: High
confidence: High
follow_up: "① SEC 審査の実際の効力発生日（申請 60 日後 = 2026-08 末）② Invesco が採用する具体的なブロックチェーン（未公表）③ Circle・Tether・Ripple 等の主要 stablecoin 発行体が実際にこのファンドを採用するか④ BlackRock BUIDL・Franklin BENJI との競合：stablecoin 準備金市場のシェア動向"
---

## 概要

運用資産 2.45 兆ドルの大手資産運用会社 Invesco が 2026 年 6 月 24 日、SEC に対して「Invesco Stablecoin Reserves Onchain Fund」の登録申請（Form N-1A 後発効改正）を提出した。既存ファンドシリーズ "Short-Term Investments Trust" の新系列として組み入れる形式。GENIUS Act が規定する高品質流動資産（HQLA）要件を充足する stablecoin 発行体（PPSI）向けの準備金運用手段として明示的に設計されており、主要 TradFi 機関が GENIUS Act 準拠の専用インフラを提供する初の事例となる。

## 何が起きたか

- **申請日**: 2026-06-24（Form N-1A 後発効改正、SEC への正式提出）
- **ファンド名**: Invesco Stablecoin Reserves Onchain Fund
- **分類**: Rule 2a-7 政府系マネーマーケットファンド、NAV $1.00 固定
- **投資対象**: 現金等価物・短期米国国債・現先取引（レポ取引）
- **オンチェーン化**: 株式をパブリックブロックチェーン上のトークンとして記録（チェーン未指定）
- **Superstate の役割**: 株式トークン化 + オンチェーン株主台帳の運営（Sub-Transfer Agent）
- **Superstate との既存関係**: 2026 年 3 月に Invesco が Superstate の USTB（トークン化米国債ファンド）の管理を引き継ぎ、Superstate のデジタル譲渡代理人技術を採用した経緯あり
- **期待効力発生日**: 申請から約 60 日後（2026 年 8 月末頃）
- **ターゲット市場**: stablecoin 準備金管理市場（推定 $4T 規模）

## 確認された事実

- Invesco の申請は GENIUS Act の「stablecoin 発行体は高品質流動資産で発行残高を 1:1 バックする」要件を充足するための準備金手段として明示的に位置づけられている
- Rule 2a-7（SEC 登録マネーマーケットファンド規制）への準拠により、GENIUS Act が想定する "high-quality liquid assets" の定義をクリアする設計
- CoinDesk・en.cryptonomist.ch（2026-06-25〜26）・techtimes（2026-06-27）の複数メディアが独立して報道

## なぜ重要か

### 決済事業者視点

- stablecoin 発行体が GENIUS Act 準拠の準備金運用手段を TradFi インフラから調達できるようになる。従来は T-Bills の直接保有・既存 MMF 利用が主流だったが、オンチェーン記録付き専用ファンドが登場することで、準備金の透明性（オンチェーン可視化）と流動性管理の両立が容易になる
- Invesco の参入により BlackRock BUIDL・Franklin Templeton BENJI に続く第 3 の主要 TradFi プレイヤーが stablecoin 準備金市場に参入。競争激化で手数料低下と流動性向上が期待できる

### 加盟店視点

- 直接的な影響は限定的。ただし stablecoin 発行体の準備金管理が TradFi インフラに深く組み込まれることは、USDC・RLUSD 等の「規制準拠済み」ステーブルコインの信頼性・継続性を高める

### プロダクト視点

- x402 / AP4M 等のエージェント決済が USDC・RLUSD を送金手段として使う設計の場合、発行体の財務基盤が TradFi 機関によって支えられる構造が強化されることはリスク低下を意味する
- GENIUS Act 最終規則（7/18 デッドライン）が確定した後、PPSI に認定された stablecoin 発行体がどのファンドを採用するかが競争軸になる

### 規制 / リスク視点

- GENIUS Act が要求する準備金要件を充足する具体的な金融商品が TradFi 機関から提供され始めた——これは GENIUS Act の法的実効性が機関投資家レベルで「実装可能」と判断されたことを示す重要なシグナル
- SEC への正式申請のため、SEC の Rule 2a-7 審査（通常 60 日）を通過する必要がある。効力発生前の段階では、stablecoin 発行体はこのファンドを準備金として使用できない

## 我々への示唆

- いま検討すべきこと:
  - GENIUS Act 最終規則確定後（7/18 以降）、USDC・RLUSD 等の準備金構成開示を確認し、Invesco・BlackRock・Franklin 等のどのオンチェーン MMF を採用しているかを把握する
  - x402 / AP4M 対応決済で使用する stablecoin の準備金透明性要件を評価基準に加える
- 後で深掘りすべきこと:
  - Invesco が採用するブロックチェーン（Ethereum か Solana か Base か）と Superstate の既存 USTB との技術的互換性
  - GENIUS Act 最終規則における「HQLA」の具体的定義と Rule 2a-7 MMF の適合判定
  - BlackRock BUIDL vs Franklin BENJI vs Invesco SROF の三極競争における料率・流動性・チェーン対応の比較
- 今は優先度が低いこと:
  - 申請段階のため効力発生（8 月末）まで実用上の変化なし。7/18 GENIUS Act 最終規則が確定するまでは準備金市場の動向は流動的

## ありそうな示唆

- 「準備金管理の TradFi 統合」が stablecoin 発行体の競争優位性になる：Circle が Invesco ファンドを採用すれば USDC 準備金のオンチェーン透明性が向上し、機関投資家向けの信頼性がさらに高まる
- Superstate は stablecoin 準備金管理の「インフラ層」ポジションを確立しつつある。Invesco に続く大手 TradFi が Superstate を採用する可能性がある

## 推測 / 監視ポイント

- Invesco が採用するパブリックブロックチェーンの選択（Ethereum/Solana 優位か）
- Circle・Ripple・Paxos 等の PPSI が正式に Invesco SROF を採用する発表の有無
- SEC が 60 日以内に効力を認可するか（修正要求で遅延の可能性）

## 未解決の論点

- GENIUS Act 最終規則が 7/18 より前に公告されない場合、Invesco SROF の "GENIUS Act 準拠" ステータスがどう法的に定義されるか
- stablecoin 発行体が Invesco SROF 以外の準備金手段（T-Bills 直接保有等）を選んだ場合のオンチェーン監査の仕組み

## 参考リンク

- 一次情報: [CoinDesk（2026-06-25）](https://www.coindesk.com/business/2026/06/25/asset-management-giant-invesco-files-for-tokenized-fund-targeting-stablecoin-reserve-market)
- 補足情報: [en.cryptonomist.ch（2026-06-26）](https://en.cryptonomist.ch/2026/06/26/invesco-tokenized-stablecoin-fund/) / [The Defiant（2026-06-25）](https://thedefiant.io/converge/tradfi-and-fintech/invesco-files-for-tokenized-stablecoin-reserve-money-market-fund-built-on-superstate-rails) / [techtimes（2026-06-27）](https://www.techtimes.com/articles/319182/20260627/invesco-files-tokenized-stablecoin-reserve-fund-chain-shares-4t-market-race.htm)

## 重要度

- High

## 確からしさ

- High（複数メディアが一致、SEC 申請という一次行為あり）
