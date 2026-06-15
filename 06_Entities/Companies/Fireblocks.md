---
title: "Fireblocks"
type: company
updated: 2026-05-21
category: payments
tags:
  - stablecoin
  - agentic-commerce
  - custody
  - x402
  - company
---

# Fireblocks

Fireblocks は、機関向けデジタル資産カストディ・ウォレットインフラを起点に、AI エージェント決済の送金側と受け取り側の両インフラを提供する方向へ拡張している。

この vault では、Fireblocks を「エージェント決済のレール（送受両側）を機関グレードのセキュリティとコンプライアンスで提供する企業」として追う。

---

## 現状の要約

### 何をしているか

- **Agentic Payments Suite のローンチ**: AI エージェントが起点となる決済フローの全ライフサイクルをカバーするインフラを提供。送金側（エージェントが払う）と受け取り側（マーチャントが受ける）の両方を自社で押さえる。
- **x402 Foundation への参加**: Linux Foundation が運営する x402 プロトコルのガバナンス組織に加盟。Google、Microsoft、AWS、Mastercard、Visa、Circle、Polygon Labs、Solana Foundation 等が参加するエコシステムに合流。
- **x402 へのセキュリティ拡張の寄与**: プロトコル層に「リクエスト整合性 + 支出ガバナンス」のセキュリティ拡張を提供。自社インフラが標準の形成側に入る構造をつくっている。
- **B2B2C モデルの維持**: エンドユーザーやマーチャントへの直販ではなく、PSP・フィンテックが自社サービスに組み込むインフラとして提供。

### 見立て

Fireblocks の動きは「暗号資産カストディ会社」から「エージェント決済インフラのレールを両側から握る会社」へのポジション転換。Stripe が法定通貨フローへのステーブルコイン吸収を目指すのに対して、Fireblocks は機関グレードのセキュリティと規制対応を武器に、エージェント決済の新しいレールそのものを設計・提供しようとしている。

---

## 主要レイヤー

| レイヤー | Fireblocks の動き | 意味 |
|---|---|---|
| 受け取り側 | Agentic Payments Gateway（PSP 向け） | マーチャントがブロックチェーン知識なしで AI エージェントからの決済を受け取れる |
| 送金側 | Agentic Wallets（フィンテック向け） | エンドユーザーが AI エージェントに支出権限を安全に委任できる |
| プロトコル | x402 Foundation 参加・セキュリティ拡張の寄与 | 業界標準の設計に入ることで自社インフラが標準に準拠するだけでなく標準を形成する側になる |
| コンプライアンス | オフランプ・変換・照合・セトルメントデータ生成 | 規制対応金融機関でも使えるグレードのコンプライアンス処理を内包 |

---

## プロダクト詳細

### Agentic Payments Gateway

**対象顧客:** PSP（決済サービスプロバイダー）→ その先のマーチャント

AI エージェントから送られてくるステーブルコイン決済を受け取るための acceptance レイヤー。PSP がカード加盟店獲得・銀行振込と同じ感覚でマーチャントに提供できる。

**できること:**
- AI エージェントからのステーブルコイン決済の受け取り
- ブロックチェーンの知識不要（マーチャント側の実装負担なし）
- 受信資金を Fireblocks ウォレットまたは連携口座に自動ルーティング
- オフランプ（stablecoin → 法定通貨）・通貨変換・照合処理に対応
- 監査・規制向けの構造化セトルメントデータを自動生成
- any stablecoin / any blockchain に対応
- コンプライアンス・セキュリティをエージェント速度（自動・高速）で処理

**確認済みパートナー:** Tazapay（70以上の市場）

---

### Agentic Wallets

**対象顧客:** フィンテック企業 → その先のエンドユーザー

エンドユーザーが AI エージェントに「代わりに払ってきて」と安全に委任できるプログラマブルウォレットインフラ。フィンテックが自社サービスに組み込んで提供する。

**できること:**
- エンドユーザーが AI エージェントに支出権限を委任（支出上限・スコープを定義）
- エージェントが自律的に署名・送金・決済を実行
- x402 または MPP に対応したマーチャントならどこにでも払える
- 全トランザクションの完全な監査証跡を記録
- リクエスト整合性チェックと支出ガバナンスをプロトコル層に内包

**ユースケース例:**
- 旅行 AI アシスタントがホテルや航空券を自動予約・決済
- 在庫補充の自動化（エージェントが閾値を検知して発注・支払い）
- API の従量課金をエージェントがリアルタイム決済

---

## エコシステム上の位置づけ

```
エンドユーザー
  ↓ 委任
AI エージェント  ← Agentic Wallets（フィンテックが提供）
  ↓ x402 / MPP で支払い
マーチャント    ← Agentic Payments Gateway（PSP が提供）
  ↓
Fireblocks インフラ（決済処理・コンプライアンス・セトルメント）
```

---

## 未解決・監視ポイント

- Agentic Payments Gateway / Agentic Wallets が GA か、ベータか、ロードマップかは未確認
- x402 のセキュリティ拡張の具体的な OSS 公開状況
- MPP（Stripe の Machine Payments Protocol）との競合・共存関係
- Coinbase、Circle など他の機関向けインフラ企業との差別化

---

## 更新ログ

- **2026-05-21**: Agentic Payments Suite（Agentic Payments Gateway + Agentic Wallets）ローンチ、x402 Foundation 参加を発表。確認済みパートナー: Tazapay、Agora（AUSD）、Wyoming Stable Token Commission。

---

## Inbox との紐付け

### ローンチ・発表

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-20 | [[2026-05-20_Fireblocks_x402-foundation-agentic-payments-suite]] | Agentic Payments Suite（Gateway + Wallets）ローンチと x402 Foundation 参加の正式発表 |
| 2026-05-20 | [[2026-05-20_Sui-Fireblocks_gasless-stablecoin-transfers]] | Sui との連携でガスレスのステーブルコイン送金を実現 |
| 2026-06-02 | [[2026-06-02_Fireblocks_flow-stablecoin-acceptance-psp-fintech]] | Flow プロダクト：PSP・フィンテック向けステーブルコイン受け取りソリューション |

### 関連エコシステム動向

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-28 | [[2026-05-28_OTL_open-transaction-layer-agentic-coordination]] | OTL（Fireblocks・Checkout.com・Robinhood 参加）によるエージェント決済の調整レイヤー構想 |

---

## 参考リンク

- [プレスリリース (PR Newswire)](https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html)
- [CoinTelegraph 記事](https://cointelegraph.com/news/fireblocks-launches-agent-payment-support-for-ai-agents)
