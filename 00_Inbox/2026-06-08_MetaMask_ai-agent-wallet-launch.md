---
title: "MetaMask、AI エージェント向け自己管理型ウォレットを発表——Guard Mode / Beast Mode と $10,000 補償プログラムを搭載"
date: 2026-06-08
source: CoinDesk
source_url: https://www.coindesk.com/tech/2026/06/08/metamask-launches-ai-agent-wallet-with-built-in-security-for-crypto-trades
entity: MetaMask / ConsenSys
category: agent-wallet / agentic-commerce
primary_category: agentic-commerce
article_published_date: 2026-06-08
underlying_event_date: 2026-06-08
primary_source_date: 2026-06-08
tags:
  - agentic-commerce
  - agent-wallet
  - agent-security
  - defi
  - machine-payments
summary: "MetaMask（ConsenSys）が AI エージェント専用の自己管理型ウォレット「MetaMask Agent Wallet」をリミテッドアーリーアクセスで発表。スワップ・無期限先物・予測市場・流動性提供を自律実行できるエージェントを対象に、トランザクションシミュレーション・MEV 保護・Guard Mode / Beast Mode のセキュリティ層と最大 $10,000 の Transaction Protection プログラムを搭載。"
implications: "AI エージェントが実際の資本を管理して金融判断を下すユースケースが本番ステージに入りつつあることの証左。エージェント向けウォレットのセキュリティ設計（支出上限・プロトコル許可リスト・2FA）が業界標準化の先行事例になる可能性がある。"
importance: High
confidence: High
follow_up: "リミテッドアーリーアクセスから一般提供への拡大時期、Transaction Protection プログラムの実際の補償件数・金額の公開、Beast Mode 採用率と損失発生率の比較データ"
---

## 概要

MetaMask（ConsenSys）が、AI エージェントが DeFi 上で自律的に資本を運用するための自己管理型ウォレット「MetaMask Agent Wallet」を発表。2026年6月8日にリミテッドアーリーアクセスを開始し、数ヶ月以内に一般提供予定。

## 何が起きたか

- MetaMask が AI エージェント専用の自己管理型ウォレットをリミテッドアーリーアクセスで公開
- 対象ユースケース：Ethereum 互換チェーン上でのスワップ・無期限先物・予測市場・流動性提供の自律実行
- ConsenSys CEO Joe Lubin（Ethereum 共同創設者）がコメント：「エージェントは実際の資本を管理し、実際の金融判断を下す。その下のインフラがそれに値するものでなければならない」

## 確認された事実

**セキュリティ機能：**
- トランザクション自動シミュレーション・脅威スキャン・MEV 保護
- フラグが立ったトランザクションに 2FA 要求
- **Guard Mode**（デフォルト）：支出上限・プロトコル許可リスト・承認要件を設定
- **Beast Mode**（オプトイン）：プロンプト頻度を下げつつ悪意あるトランザクションチェックは維持
- **Transaction Protection プログラム**：損失に対して最大 $10,000 まで補償

**製品状態：**
- 2026年6月8日 リミテッドアーリーアクセス開始
- 数ヶ月以内に一般提供予定

## なぜ重要か

### 決済事業者視点
- エージェントが自律的に DeFi 取引を実行する場合、従来の PSP・カードレール・決済フローは完全にバイパスされる。MetaMask Agent Wallet はそのバイパス層の標準インターフェースになる可能性がある

### 加盟店視点
- 直接的な関係は薄いが、DeFi 上で資本を自律運用するエージェントが一般化すると、「エージェントがユーザーの資産を使って購買する」ユースケースのウォレット層がこの設計を参照モデルとして採用する可能性がある

### プロダクト視点
- Guard Mode / Beast Mode という「自律性のグラデーション」設計は、エージェント決済プロダクトが「ユーザー最終承認を保持しながら自動化度を段階的に引き上げる」UX パターンの参照実装になる
- 支出上限・プロトコル許可リスト・2FA フラグという 3 層設計は、他の x402 / CPN / MPP 対応ウォレットがセキュリティ仕様を策定する際の先行事例になる

### 規制 / リスク視点
- GENIUS Act 最終規則化（〜7/18）が進む中、「エージェントが自律実行する DeFi 取引」が PPSI の対象になるかどうかは未確定
- Transaction Protection プログラム（$10,000 補償）は消費者保護の実装例として規制当局が参照する可能性がある
- Beast Mode（ユーザー承認頻度低減）が GENIUS Act・EU AI Act の「高リスク AI における人間監視義務」とどう整合するかは今後の論点

## 我々への示唆

- いま検討すべきこと:
  - Guard Mode / Beast Mode の 2 モード設計と、Travala Travel MCP の ERC-7715 セッションキー設計（同日採用）を比較し、自社エージェント決済プロダクトの承認フロー設計に活用できるか評価する
  - 支出上限・プロトコル許可リスト設計が自社プロダクトのリスク管理フレームワークに組み込み可能か検討する

- 後で深掘りすべきこと:
  - Beast Mode 採用率・損失発生率の公開データ（エージェントの自律性向上とセキュリティのトレードオフを定量評価できる最初の業界データになりうる）
  - MetaMask Agent Wallet が x402 / AP2 / CPN などのエージェント決済プロトコルを直接サポートするかどうか

- 今は優先度が低いこと:
  - リミテッドアーリーアクセス期の具体的なユーザー数・取引件数（一般提供後に評価）

## ありそうな示唆

- MetaMask は業界最大規模の自己管理型ウォレットであり、この設計が一般提供された場合、エージェント向けウォレットの事実上の標準になる可能性がある
- Guard Mode / Beast Mode という段階的自律性設計は、Worldline×ING×Mastercard（消費者最終承認）・Travala ERC-7715（セッションキー）と同じ「自律性段階管理」の方向性に収束しており、業界横断でコンセンサスが形成されつつある

## 推測 / 監視ポイント

- MetaMask Agent Wallet が一般提供後に x402・AP2・CPN との統合を発表するかどうか
- Transaction Protection プログラムの補償実績データが公開されるタイミング
- GENIUS Act 最終規則で「エージェントが自律実行する DeFi 取引」が PPSI 定義の対象になるかどうか（7/18 デッドライン）

## 未解決の論点

- Beast Mode でのエージェント自律実行が GENIUS Act・EU AI Act の人間監視要件と整合するかどうか
- $10,000 補償プログラムの財源・保険設計の詳細（ConsenSys が自前で引き受けるのか、外部保険を利用するのか）
- MetaMask Agent Wallet がエージェント「ID」をどう管理するか（KYA 対応の有無）

## 参考リンク

- 一次情報: [MetaMask AI Agent Wallet Launch（CoinDesk, 2026-06-08）](https://www.coindesk.com/tech/2026/06/08/metamask-launches-ai-agent-wallet-with-built-in-security-for-crypto-trades)
- 補足情報:

## 重要度

- High

## 確からしさ

- High
