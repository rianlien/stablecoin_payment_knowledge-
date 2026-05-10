---
title: "Exodus、AI エージェント専用ステーブルコイン「XO Cash」と AgentKit SDK を発表——Visa 仮想デビットカード付き、エージェントが鍵を持たずに決済"
date: 2026-05-08
source: GlobeNewswire / CryptoBriefing / AMBCrypto
source_url: https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/Exodus-Launches-XO-Cash-as-the-First-Stablecoin-Built-for-AI-Agents.html
entity: Exodus
category: 企業発表
tags:
  - agentic-commerce
  - payments
  - wallet
  - agent-payments
article_published_date: 2026-05-08
underlying_event_date: 2026-05-08
primary_source_date: 2026-05-08
summary: "暗号資産ウォレット大手 Exodus（NYSE: EXOD）が 2026 年 5 月 8 日、AI エージェント専用に設計されたステーブルコイン「XO Cash」と開発者向け SDK「AgentKit」を発表。Solana 上で動作し、1 回の API コールでエージェントに専用ウォレットを発行できる。エージェントは Visa 加盟店全店で使える仮想デビットカードを持ち、ユーザーが設定した日次上限・1 件上限・利用可能加盟店の範囲内で自律決済できる。エージェントは秘密鍵を保持しない非カストディアル設計。MoonPay・Monavate と共同開発。XO Cash 間の送金は無料で、USDC/USDT への自動変換が決済時に発生する。"
implications: "AI エージェント向けの『アカウント＋カード』が一体で提供される初の製品。エージェントが Visa ネットワーク全体で決済できる点で、x402（API 課金）・MoonAgents Card（Mastercard）に続く第三の決済経路が登場した。"
follow_up: "XO Cash の対応地域・規制ステータス（英国・EU・米国）、AgentKit の MCP 統合ロードマップ、Monavate のカード発行ライセンス適用範囲、エージェント向け Visa デビットカードの AML・KYC 責任の所在"
---

## 概要

暗号資産ウォレット Exodus Movement（NYSE American: EXOD）が 2026 年 5 月 8 日、AI エージェント専用に設計されたステーブルコイン「XO Cash」と開発者向け SDK「AgentKit」を正式発表した。Solana ブロックチェーン上で動作し、MoonPay および Monavate（Mastercard プリンシパルメンバー）との共同開発によって、エージェントが秘密鍵を管理せずに Visa 加盟店全店で決済できる仕組みを実現した。

## 何が起きたか

**XO Cash の概要**

- Solana 上に構築された AI エージェント専用のステーブルコイン
- エージェント間送金・サービス利用料の支払いを想定した設計
- USDC / USDT への自動変換機能（決済時にエージェントが USDC や USDT を要求するサービスへの支払いを単一トランザクションで処理）
- XO Cash 間の取引は手数料ゼロ

**AgentKit SDK**

- 1 回の API コールでエージェント専用ウォレットを発行
- ユーザーが設定できるパラメーター：
  - 日次支出上限
  - 1 件あたり上限
  - 利用可能加盟店のリスト
  - レート制限
- 設定はいつでもリアルタイムで変更可能
- エージェントは秘密鍵を保持しない設計——Exodus Pay の残高から直接支出し、鍵管理を回避

**Visa 仮想デビットカード**

- 各 XO Cash エージェントウォレットには 1 回の API コールで仮想 Visa デビットカードを発行可能
- Monavate のカードインフラを利用（Exodus Pay と MoonAgents Card と同一インフラ）
- Visa 加盟店（オンライン・実店舗含む）全店で利用可能
- ウォレットに設定されたスペンディングルールがカード決済にも自動適用

**MoonPay との連携**

- Exodus Pay・MoonPay・Monavate の既存インフラを拡張する形で開発
- MoonAgents Card（MoonPay × Mastercard、発表 2026-05-01）と並行して、Visa レールの AI エージェント向け製品が整備された

**市場見通し（自社引用）**

- AI エージェントが 2030 年までに消費者商取引の 3 兆〜5 兆ドルを仲介すると予測されるとし、XO Cash をその基盤通貨と位置付け

## なぜ重要か

### 決済事業者視点

- AI エージェント向けウォレット＋仮想カードの「セット発行 API」が初登場したことで、PSP・PayFac がエージェント向け決済機能を既存インフラに素早く組み込める環境が整った
- Visa ネットワーク全体をカバーする点で、MoonAgents Card（Mastercard）と合わせて「AI エージェントが既存カードネットワークの大半にアクセスできる状態」が実現しつつある

### 加盟店視点

- 既存の Visa 端末・オンラインゲートウェイを一切変更せずに、AI エージェントからの注文・支払いを受け入れられる状態になる
- ただし加盟店はエージェント発動取引かどうかを識別するメタデータを持たないため、チャージバック・紛争管理において新たなリスクが発生する

### プロダクト視点

- AI エージェントの支払い手段は①x402（HTTP 402 / USDC / API 課金）②MoonAgents Card（Mastercard 加盟店）③XO Cash ＋ Visa の三層構造に整備された
- AgentKit の「1 API コールでエージェントに財布とカードを渡す」抽象化は、アプリ開発者がエージェント決済を数時間で実装できるレベルのシンプルさを実現しており、エコシステム拡大の加速要因となりうる

### 規制 / リスク視点

- エージェントが秘密鍵を持たず Exodus Pay 残高から決済する構造は、ユーザーがカストディアンであり続けることを意味する——規制上の KYC 義務の主体はユーザー（Exodus Pay 利用者）側に残る
- ただし AI エージェントが Visa 加盟店全体で決済できるとなると、エージェントの購入行動が AML 的に審査されるべきかどうかという論点が発生する（現状は Exodus Pay の口座 KYC に依存）

## 我々への示唆

- いま検討すべきこと:
  - AgentKit SDK の技術仕様・対応チェーン・MCP 統合可能性を確認し、自社エージェント決済製品への統合可否を評価する
  - XO Cash ＋ Visa（AgentKit）・MoonAgents Card（Mastercard）を組み合わせた「エージェント向けカード決済」の優先度評価——x402 では対応できない実店舗・既存加盟店向けユースケースを補完できる
- 後で深掘りすべきこと:
  - エージェントが Visa 加盟店で生成したチャージバック・紛争の帰属責任（Exodus / MoonPay / Monavate / 加盟店）の分担ルール
  - XO Cash の規制ステータス（英国 FCA・EU MiCA・米国 FinCEN の下での位置づけ）
- 今は優先度が低いこと:
  - XO Cash トークン自体の価格動向・取引所上場（エージェント決済インフラとしての機能評価が先）

## 未解決の論点

- AgentKit で発行した Visa デビットカードの AML ・不正検知ルールは誰が設定・運用するか（Exodus / Monavate / Visa）
- XO Cash が USDC/USDT に自動変換される際の為替リスク・スリッページは誰が負担するか
- エージェント向け Visa デビットカードが 3DS 認証や強力な顧客認証（SCA）をどう処理するか
- 米国展開に向けた規制上のパスは何か（FinCEN への送金業者登録等）

## 参考リンク

- 一次情報:
  - [GlobeNewswire — Exodus Launches XO Cash as the First Stablecoin Built for AI Agents（2026-05-08）](https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/Exodus-Launches-XO-Cash-as-the-First-Stablecoin-Built-for-AI-Agents.html)
  - [Stocktitan — Exodus EXOD 公式発表](https://www.stocktitan.net/news/EXOD/exodus-launches-xo-cash-as-the-first-stablecoin-built-for-ai-j1iykhrq77zs.html)
- 補足情報:
  - [CryptoBriefing — Exodus launches XO Cash stablecoin for AI agents on Solana](https://cryptobriefing.com/exodus-xo-cash-stablecoin-ai-agents-solana/)
  - [AMBCrypto — Exodus launches XO Cash as AI agents become crypto's next payments battleground](https://ambcrypto.com/exodus-launches-xo-cash-as-ai-agents-become-cryptos-next-payments-battleground/)
  - [GNCrypto — Exodus launches XO Cash SDK on Solana for AI Visa payments](https://www.gncrypto.news/news/exodus-xo-cash-sdk-solana-ai-visa-payments/)
- 関連ノート:
  - [MoonPay MoonAgents Card（Mastercard）2026-05-01](./2026-05-01_MoonPay_moonagents-card-mastercard-ai-agents.md)
  - [Solana Foundation × Google Cloud Pay.sh（x402）2026-05-05](./2026-05-05_Solana-GoogleCloud_pay-sh-x402-agent-payments.md)

## 重要度

- High

## 確からしさ

- High（GlobeNewswire 公式プレスリリース・NYSE 開示・複数メディア一致）
