---
title: "NEAR AI、USDC × Confidential Intents でエージェント向けプライベート・ステーブルコイン決済を提供開始"
date: 2026-05-14
source: PRNewswire
source_url: https://www.prnewswire.com/news-releases/near-ai-brings-private-usdc-stablecoin-payments-to-the-agentic-economy-302772311.html
entity: NEAR AI
category: 企業発表
primary_category: agent-payments
article_published_date: 2026-05-14
underlying_event_date: 2026-05-14
primary_source_date: 2026-05-14
tags:
  - agentic-commerce
  - agent-identity
  - stablecoin
  - privacy
  - machine-payments
summary: "NEAR AI が USDC と Confidential Intents を統合し、NEAR AI Agent Market 上の AI エージェントが取引金額・相手先を公開せずに USDC で決済できる仕組みを提供開始。エージェント決済における「プライバシーが主流化のボトルネック」（Paxos 指摘）への直接的な回答となる実装。"
implications: "エンタープライズ・機関向けエージェント決済において、公開ブロックチェーン上での取引可視性問題を技術で解消する最初の本番実装の一つ。Paxos が Consensus Miami（5 月 8 日）で指摘した「プライバシーインフラ未整備が最大の障壁」という課題に対して、NEAR が ZK ではなく Confidential Intents（TEE + NEAR プライベートシャード）アーキテクチャで先行した。"
importance: High
confidence: High
follow_up: "Confidential Intents の技術仕様（TEE の詳細・NEAR プライベートシャードの構成）、対応できるトランザクション規模・手数料、Circle / USDC 以外のステーブルコインへの拡張計画、規制上の KYC/AML 対応（プライバシーと法的開示義務の両立設計）"
---

## 概要

- NEAR AI が USDC と Confidential Intents を統合し、NEAR AI Agent Market 上の AI エージェントがプライベートなステーブルコイン決済を実行できる環境を提供開始した（2026 年 5 月 14 日）。
- AI エージェントは USDC を決済通貨として使用しながら、取引金額・取引相手を公開ブロックチェーン上で露出させずに決済できる。
- Consensus Miami（5 月 8 日）で Paxos が「公開ブロックチェーン上の取引データ露出が企業・機関の本格利用を阻む」と警告した課題に対し、NEAR が実装レベルで先行した形。

## 何が起きたか

- NEAR AI が公式プレスリリースで、Confidential Intents（NEAR プライベートシャードを活用した機密クロスチェーン実行レイヤー）に USDC サポートを追加したと発表。
- NEAR AI Agent Market 上のユーザーとエージェントは、USDC で支払い・受け取りを行いながら、取引金額・カウンターパーティを公開しない形での決済が可能になった。
- 決済フロー全体（タスク投稿から精算まで）は分散型インフラ上で完結し、センシティブな商業的情報の露出リスクを低減する。

## 確認された事実

- 発表日：2026 年 5 月 14 日（PRNewswire）
- 決済通貨：USDC（Circle 発行の完全準備型ステーブルコイン）
- 技術基盤：Confidential Intents ＝ NEAR プライベートシャードを活用した機密クロスチェーン実行レイヤー
- 対象プラットフォーム：NEAR AI Agent Market
- Confidential Intents 自体は 2026 年 3 月に NEAR がローンチ（当時 NEAR トークンが 17% 急騰・$2.7B の取引量を記録）
- 今回は Confidential Intents への USDC サポート追加と、AI エージェントの決済利用に特化したポジショニングが新しい

## なぜ重要か

### 決済事業者視点

- B2B・機関向けエージェント決済において、「取引が競合・監査機関・一般に可視」という公開ブロックチェーンの構造的問題を解消する具体的な実装が登場した。
- エンタープライズがエージェント決済に踏み切れない最大の理由の一つ（取引データの競合他社への露出）が、テクノロジーレベルで対処可能になる。

### 加盟店視点

- NEAR AI Agent Market 経由でサービスを提供する企業・開発者は、収益構造・顧客関係をプライバシー保護しながらエージェントからの支払いを受け取れる。

### プロダクト視点

- Confidential Intents アーキテクチャ（TEE + NEAR プライベートシャード）は、ZK-proof ベースのアプローチと競合する別路線。ZK より実装が簡易で応答速度が高い可能性があるが、信頼境界（TEE のトラストモデル）が異なる。
- エージェント向け決済基盤の差別化要素として「プライバシー保証レベル」という新しい軸が加わった。

### 規制 / リスク視点

- プライバシーを提供しながら KYC/AML の規制要件を満たす「選択的開示」の設計が今後の法的論点になる。NEAR のアーキテクチャがどこまで規制上の開示要件を満たすかは未確認。
- GENIUS Act・CLARITY Act の規制枠組みが固まりつつある中で、「プライバシー × コンプライアンス」の両立を設計しておく必要がある。

## 我々への示唆

- いま検討すべきこと:
  - NEAR Confidential Intents の技術仕様（選択的開示・AML 対応の設計）を確認し、Polygon Hinkal（2026-05-04）や ZK-proof 系プロトコルとの比較軸を整理する。
  - エンタープライズ向けエージェント決済プロダクトの RFP・要件定義に「プライバシー保証レベル」を評価軸として追加することを検討する。
- 後で深掘りすべきこと:
  - Confidential Intents の KYC/AML 選択的開示設計と GENIUS Act・CLARITY Act の規制要件との適合性。
  - NEAR AI Agent Market の実取引量・採用事業者の規模感（プレスリリース単体では不明）。
  - ERC-5564 Stealth Addresses・Polygon Hinkal との技術的・戦略的比較。
- 今は優先度が低いこと:
  - NEAR プロトコルやエコシステム全体への投資判断。決済インフラ観点での技術把握が優先。

## ありそうな示唆

- Paxos が Consensus Miami で指摘した「プライバシーが主流化のボトルネック」という課題に対し、NEAR は Ethereum L2（ZK）ではなく独自プライベートシャードアーキテクチャで最初の実装を提示した。このことは、プライバシー対応エージェント決済が「誰が標準を握るか」の競争局面に入ったことを示唆する。
- 決済プライバシーの「事実上の標準」が ZK-proof（Polygon Hinkal・ERC-5564 等）か TEE ベース（NEAR Confidential Intents）かは 2026〜2027 年に決まる可能性が高い。

## 推測 / 監視ポイント

- 規制当局が「プライバシー決済」をマネーロンダリングリスクとして取り扱うかどうか（FinCEN・FATFの姿勢）
- Ethereum 系プライバシープロトコル（EIP-7503 ZK Wormholes・ERC-5564 Stealth Addresses）との機能・速度・コスト比較
- Circle（USDC 発行体）が NEAR Confidential Intents との統合をどこまで公式サポートするか
- 他のエージェント決済プラットフォーム（Exodus XO Cash・MoonPay AgentKit 等）がプライバシー機能を追加するか

## 未解決の論点

- Confidential Intents の TEE（Trusted Execution Environment）のトラストモデル：誰がシャードを運営するか、コード検証の仕組み
- USDC 以外のステーブルコイン（USDT・USDS・EURC 等）への対応ロードマップ
- NEAR AI Agent Market の現在の取引規模・対応ユースケース（プレスリリース単体では不明）
- 規制上の KYC/AML 開示との両立設計の詳細

## 参考リンク

- 一次情報: [PRNewswire — NEAR AI Brings Private USDC Stablecoin Payments to the Agentic Economy（2026-05-14）](https://www.prnewswire.com/news-releases/near-ai-brings-private-usdc-stablecoin-payments-to-the-agentic-economy-302772311.html)
- 補足情報: [CoinDesk — NEAR token jumps 17% after Confidential Intents launch（2026-03-02）](https://www.coindesk.com/markets/2026/03/02/near-token-jumps-17-after-confidential-intents-launch-outpaces-privacy-tokens-sector)
- 補足情報: [KuCoin — NEAR Launches Confidential Intents for Cross-Chain Privacy](https://www.kucoin.com/news/articles/near-enhances-cross-chain-privacy-with-confidential-intents-launch)
- 関連ノート: [[2026-05-08_Consensus-Miami_stablecoin-permission-slip]] （Paxos によるプライバシーボトルネック指摘）
- 関連ノート: [[2026-05-04_Polygon-Hinkal_private-stablecoin-payments]]

## 重要度

- High

## 確からしさ

- High（PRNewswire 公式プレスリリースに基づく。TEE の技術詳細は一次情報未確認のため、アーキテクチャ部分は Medium）
