---
title: "x402 Foundation"
type: company
updated: 2026-06-23
category: infrastructure
tags:
  - x402
  - agentic-commerce
  - agent-payments
  - protocol
  - micropayments
---

# x402 Foundation

x402 Foundation は、HTTP ベースのエージェント向けマイクロペイメントプロトコル「x402」を管理する Linux Foundation 傘下の中立組織。Coinbase と Cloudflare が共同で立ち上げ、2026 年 4 月 2 日設立。Stripe・AWS・Google・Visa・Circle・Mastercard・Solana Foundation 等 20 社超がサポートする。x402 プロトコルの仕様策定・オープンソース実装・エコシステム拡張を担い、AI エージェントが USDC でサービスを自律的に購入できる機械間決済（M2M payments）インフラの標準化を推進する。

---

## 現状の要約

### 何をしているか

- **x402 プロトコルの管理**：HTTP 402 ステータスコードを活用した AI エージェント向けオープン決済プロトコルの仕様策定・維持。TypeScript・Python・Go・Java の SDK を提供
- **マルチチェーン展開**：Base（メイン）・Ethereum・Polygon・Arbitrum・World・Solana の 6 チェーンで Coinbase ホスト型ファシリテーターを提供（2026 年 5 月時点）。Arbitrum 対応は 2026-05-14 に追加
- **バッチ決済の追加**：2026-05-13、オンチェーンエスクロー + オフチェーンバウチャー方式のバッチ決済（Batched Settlement）を追加。1 コール $0.0001 未満の AI マイクロペイメントが経済的に成立
- **Agentic.market 連携**：Coinbase が x402 上に構築した AI エージェント向けサービスマーケットプレイス「Agentic.market」を通じてエコシステム実用化を推進。Bloomberg・AWS・OpenAI 等が参加（2026 年 4 月時点）
- **ネットワーク規模**（2026 年 5 月 13 日時点）：累積 169M 件以上の支払い、59 万人以上の買い手、10 万件以上の売り手サービス
- **Fireblocks 参加**：2026-05-20、Fireblocks が x402 Foundation に参加し Agentic Payments Suite を発表

### 見立て

x402 Foundation は AI エージェント向けオープン決済プロトコルの標準化主体として、エコシステムを急速に拡大している。Linux Foundation の中立ガバナンス構造が Stripe・Visa・Mastercard 等の競合をも参加させる求心力になっている。ただし「承認ギャップ（approval gap）」——ウォレット確認の 5〜15 秒遅延が小額決済経済を阻害——という構造的課題が定量化されており、AP2 スペンディングマンデート（FIDO Alliance）との統合が解決経路として注目される。月次出来高は 2025 年 11 月ピーク（$5.15M）から 77% 減少（2026 年 5 月時点 $1.19M）しており、取引件数が回復している点と合わせて推移を継続監視する必要がある。

---

## Inbox との紐付け

| 日付 | ノート | 位置づけ一行 |
|---|---|---|
| 2026-04-21 | [[2026-04-21_Coinbase-x402_agentic-market-launch]] | Coinbase が x402 上に Agentic.market をローンチ。69,000 エージェント稼働・累計 1.65 億件処理 |
| 2026-05-13 | [[2026-05-13_x402_batch-settlement-sub-cent-ai-payments]] | x402 バッチ決済追加——$0.0001 以下 AI マイクロペイメントが経済的に成立 |
| 2026-05-14 | [[2026-05-14_x402_arbitrum-launch-agent-payments]] | x402 が Arbitrum に正式対応。対応チェーンが 5 本（→ 6 本）に |
| 2026-05-20 | [[2026-05-20_Fireblocks_agentic-payments-suite-x402-foundation]] | Fireblocks が x402 Foundation に参加し Agentic Payments Suite を発表 |
| 2026-05-23 | [[2026-05-20_Fireblocks_agentic-payments-suite-x402]] | Fireblocks Agentic Payments Suite 詳細——PSP 向け Gateway・フィンテック向け Wallets の 2 製品、x402/MPP 両対応 |
| 2026-05-27 | [[2026-05-27_x402_approval-gap-volume-data]] | 承認ギャップ問題の定量化——月次出来高 77% 減・取引件数は回復 |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100M-agentic-payments-base]] | Chainalysis が x402 の 1 億件突破を報告。Base 上のエージェント決済主力に |
| 2026-06-15 | [[2026-06-15_x402_canton-network-exact-scheme]] | x402 に Canton Network（機関向けブロックチェーン）の exact scheme 対応が追加——Goldman Sachs 等参加機関で x402 machine payments が利用可能に |
| 2026-06-17 | [[2026-06-17_x402_onpaymentrequired-trust-gate]] | x402 クライアントに onPaymentRequired trust-gate フック追加——支払い前のペイアドレス検証・支出上限・外部信頼スコアリングを標準化 |
| 2026-06-19 | [[2026-06-19_x402_siwx-go-support]] | x402 SIWX が Go 言語に対応——TypeScript・Python・Go のクロス SDK エージェント認証が完成 |

---

## 監視ポイント

- 月次出来高の回復軌跡（$1.19M → ピーク $5.15M 方向への再成長があるか）
- AP2（FIDO Alliance）との統合による承認ギャップ解消の進捗
- Stripe・Visa・Mastercard が Foundation 参加にとどまらず、自社製品との x402 統合を本格化するか
- GENIUS Act 最終規則確定後、USDC on Base の PPSI 認定状況と x402 の「法的準拠インフラ」としての位置づけ
