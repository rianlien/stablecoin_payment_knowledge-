---
title: "Visa"
type: company
updated: 2026-06-15
category: payments
tags:
  - stablecoin
  - agentic-commerce
  - agent-identity
  - payment-authorization
  - card-rail
---

# Visa

Visa は世界最大のカードネットワークであり、2025〜2026 年にかけて AI エージェント時代の決済インフラ整備に積極的に乗り出している。Trusted Agent Protocol（TAP）・Visa Intelligent Commerce（VIC）・Agentic Registry・ステーブルコイン清算拡張という複数の軸を同時展開し、agentic commerce における「カードレール側の主要プレイヤー」として際立ったポジションを確立している。

この vault では、Visa を「既存カードレールをエージェント決済・ステーブルコイン清算の両方に拡張するインフラプロバイダー」として追う。

---

## 現状の要約

### 何をしているか

- **Trusted Agent Protocol（TAP）のグローバル展開**：エージェントを Visa 認証済みとしてレジストリ登録し、加盟店・サービス全体で認証を維持するフレームワーク。Visa Agentic Ready プログラムを通じて米国・英国・欧州・LATAM・アジア太平洋・カナダに展開（カナダではBMO・CIBC・RBC・Scotiabank・TD の主要 5 行が参加）
- **Visa Intelligent Commerce（VIC）の商品化**：VIC Connect API を通じて Highnote・AWS・Mesh・Payabli 等のイシュアー・PSP パートナーがエージェント向け spending mandate（tokenized credential＋スペンドルール＋動的オーソリゼーション）を実装可能にした
- **OpenAI との戦略的連携**：ChatGPT 内で AI エージェントが Visa カードを使って購入完了まで実行できる連携を発表（2026-06-10 Visa Payments Forum）。Agent Score（加盟店のエージェント対応度スコア）・Agentic Registry（エージェント登録・検証機構）を新発表
- **ステーブルコイン清算の規模拡大**：対応チェーンを 9 に拡張、年率換算 70 億ドルの清算量（2026-04-29 時点）。acquirer 側にも週 7 日決済を拡大。銀行預金をプログラマブルなデジタルマネーに変換する技術層も構築中
- **Replit への戦略出資**：TAP を開発者プラットフォームに直接組み込み、TAP 対応エージェントの量産フライホイールを構築

### 見立て

Visa は agentic commerce で「カードレールの防衛」と「新たな認証標準の主導」を同時に進めている。TAP・VIC・Agentic Registry の三層構造は、エージェント発動取引の識別・認証・オーソリゼーションを Visa のインフラ上で完結させる設計であり、x402 や AP2（FIDO Alliance）が主導するオープン標準とは対照的に中央集権的な信頼レイヤーを構築しようとしている。

OpenAI との連携は業界を通じた最大のシグナルであり、「消費者が AI エージェントに日常的な購入を委任する」シナリオのデフォルト決済レールを Visa ネットワークに引き込む大きな一手と見られる。一方で、TAP のレジストリ管理が Visa に集権化されることによる単一障害点・プライバシーリスク、AP2 / AP4M との相互運用性未確定、返金・chargeback 時の責任分担設計など、未解決の論点も多い。

---

## Inbox との紐付け

### ステーブルコイン清算

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-29 | [[2026-04-29_Visa_stablecoin-settlement-9chains-7b]] | ステーブルコイン清算を 9 チェーンに拡大・年率 70 億ドル突破 |
| 2026-06-03 | [[2026-06-03_Stripe-Visa-Mastercard-Coinbase_stablecoin-consortium]] | Stripe・Mastercard・Coinbase と共同ステーブルコインプラットフォームを発表 |
| 2026-06-04 | [[2026-06-03_Stripe-Visa-Mastercard_joint-stablecoin-platform-report]] | Stripe・Mastercard・Coinbase 共同ステーブルコインプラットフォームレポート |

### Agentic Ready / TAP 展開

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-05 | [[2026-05-05_Visa_agentic-ready-canada-global]] | Agentic Ready をカナダ主要 5 行に展開、TAP のグローバル化が加速 |
| 2026-05-28 | [[2026-05-28_Visa-Replit_trusted-agent-protocol]] | Replit に戦略出資し TAP をデベロッパープラットフォームへ組み込み |

### Visa Intelligent Commerce（VIC）パートナー連携

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-ai-initiated-payments]] | Highnote が VIC Connect を実装、B2B エージェント決済のリファレンス事例 |
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-b2b-payments]] | Highnote × Visa の B2B agentic payments 詳細 |
| 2026-06-02 | [[2026-06-02_Crossmint_agentic-cards-visa-basis-theory]] | Crossmint が Visa ベースのエージェント向けカードを発行 |

### OpenAI 連携・Payments Forum 2026

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-06-10 | [[2026-06-10_Visa_payments-forum-openai-agentic-commerce]] | Visa Payments Forum にて OpenAI 連携・Agent Score・Agentic Registry 発表 |
| 2026-06-11 | [[2026-06-11_Visa-OpenAI_chatgpt-agent-payments]] | ChatGPT 内でエージェントが Visa カードで購入完了できる連携を公表 |

---

## 監視ポイント

- **TAP vs AP2（FIDO Alliance）の相互運用性**：VisaがTAPを独自維持するか、AP2 標準を採用するかが業界の認証フレームワーク統一の分岐点
- **Agentic Registry の登録要件・技術仕様の公開**：AP4M の Verifiable Intent や x402 との相互認識が可能かどうか
- **Agent Score の加盟店向け公開タイムライン**：スコアリング基準が公開された場合、x402 / AP2 対応の有無が評価に影響する可能性
- **OpenAI 連携の human-in-the-loop 緩和条件**：どの条件で完全自律決済を許可するかが agentic commerce の実用化速度を左右する
- **ステーブルコイン清算の対応通貨・チェーン拡大**：USDC 以外の PPSI 認定ステーブルコインへの拡張タイムライン
- **銀行向けデジタルマネー層のローンチパートナー発表**：JP Morgan・BofA 等の主要行が参加した場合、Circle/USDC の競合として市場インパクトが大きい
- **Mastercard AP4M との競合・共存の展開**：OpenAI が Mastercard 陣営にも参加するかどうか

---

## 参考リンク

- [Visa 公式ニュースルーム](https://usa.visa.com/about-visa/newsroom.html)
- [Visa Payments Forum 2026 プレスリリース（2026-06-10）](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22491.html)
- [Visa Agentic Ready カナダ展開（2026-05-05）](https://www.globenewswire.com/news-release/2026/05/05/3287953/0/en/Visa-Expands-Agentic-Ready-Program-to-Canada-to-Advance-AI-Driven-Commerce.html)
- [Visa ステーブルコイン清算拡張（2026-04-29）](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/default.aspx)
- [GitHub — Visa Trusted Agent Protocol（TAP）仕様](https://github.com/visa/trusted-agent-protocol)
