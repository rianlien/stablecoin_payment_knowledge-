---
title: "Google"
type: company
updated: 2026-06-15
category: payments
tags:
  - agentic-commerce
  - AP2
  - UCP
  - agent-identity
  - company
aliases:
  - Google Cloud
  - Gemini
  - AP2
  - Universal Cart
  - UCP
---

# Google

Google は AP2（Agent Payments Protocol）と UCP（Universal Commerce Protocol）を主導し、AI エージェントによる自律的な商取引のID認証・カタログ・決済承認の標準化を推進している。Gemini・Search・YouTube・Gmail を横断する Universal Cart を通じて、消費者向けエージェントコマースの入口を自社エコシステム内に構築している。

この vault では、Google を「エージェント商取引の消費者 UI・ID 標準・カタログ API を掌握し、AP2 と UCP を通じてその標準を業界インフラ化しようとするプラットフォームプレイヤー」として追う。

---

## 現状の要約

### 何をしているか

- **AP2（Agent Payments Protocol）の策定と FIDO Alliance への寄贈**：Mastercard と共同開発した AP2 v0.2 を 2026 年 4 月 28 日に FIDO Alliance へ移管。Human Not Present（人不在決済）機能を追加し、エージェントが事前承認に基づき自律決済を実行できる標準を整備。60 社超（Mastercard・Adyen・PayPal・Coinbase・Revolut・UnionPay 等）が参加。
- **UCP（Universal Commerce Protocol）の拡張**：Google I/O 2026（2026-05-19）で Universal Cart を発表し、Search・Gemini・YouTube・Gmail を横断するエージェント対応ショッピングカートを公開。Google Marketing Live（2026-05-28）では Identity Linking・Catalog API・マルチアイテムカートの 3 機能を追加し、Salesforce・Stripe・Shopify を実装パートナーに迎えた。
- **消費者向けエージェント UI の構築**：Gemini モデルが価格監視・在庫アラート・自律購入を担う Universal Cart を 2026 年夏に米国ロールアウト予定。Nike・Walmart・Target・Sephora・Wayfair 等の大手加盟店がローンチパートナーとして参加済み。
- **Google Cloud のエージェント決済インフラ提供**：Cloud KMS を暗号資産カストディ向けに拡張する計画を表明。マルチパーティカストディ（エージェントは鍵シャードの 1 つのみ保持）をエージェント設計の標準パターンとして推進。
- **AP2 × x402 の補完スタック設計**：Coinbase・Ethereum Foundation と連携して AP2 への x402 拡張を開発済み。AP2 が認証・認可レイヤー、x402 が USDC 決済レイヤーを担うスタック構成を実現。

### 見立て

Google の戦略は、消費者が AI で物を買う際の起点（Gemini・Search・YouTube・Gmail）を自社で押さえつつ、その背後で動くID認証・カタログ・決済承認の標準（AP2 + UCP）を業界共通インフラ化することにある。Apple・Amazon・Microsoft が追従する以前に「エージェントコマースの入口」を確保しようとする動きと読める。

Stripe が UCP 実装パートナーに加わり、Shopify が全加盟店を自動オプトインしたことで、AP2 + UCP スタックは単なる Google 内部機能を超え、数百万の加盟店が接続できる実用的なインフラに転じた。x402（Linux Foundation）と AP2（FIDO Alliance）は現時点では「補完的スタック」として統合されつつあるが、実装レベルでの役割分担はまだ流動的であり、引き続き監視が必要。

---

## 主要スタック

| レイヤー | Google の動き | 意味 |
|---|---|---|
| 消費者 UI | Universal Cart（Search・Gemini・YouTube・Gmail 横断） | エージェントコマースの消費者接点を自社内に統合 |
| ID・認可 | AP2 Intent Mandate / Identity Linking | エージェントが何を、誰の委任で買うかを標準化 |
| カタログ | UCP Catalog API | エージェントがリアルタイムで商品情報を取得する共通フォーマット |
| 決済プロトコル | AP2（FIDO Alliance）+ x402 拡張 | 認証・認可と USDC 決済レイヤーの補完スタック |
| クラウド基盤 | Google Cloud KMS（カストディ拡張予定） | エンタープライズ向けエージェント決済のカストディ層 |

---

## Inbox との紐付け

### AP2・プロトコル標準化

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-28 | [[2026-04-28_Google_ap2-fido-alliance]] | AP2 v0.2 を FIDO Alliance に寄贈・Human Not Present 機能追加・60 社参加 |
| 2026-05-10 | [[2026-05-10_PayPal-Google_consensus-miami-agentic-commerce]] | Google Cloud が Consensus Miami でクリプトレール不可避論を公言・Cloud KMS カストディ拡張を示唆 |

### UCP・加盟店対応・エコシステム拡大

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-19 | [[2026-05-19_Google_universal-cart-ap2-io2026]] | Google I/O 2026 で Universal Cart 発表・AP2 FIDO Alliance 移管確認・ローンチパートナー公開 |
| 2026-05-28 | [[2026-05-28_Google_ucp-update-identity-linking-catalog-marketing-live]] | Marketing Live で UCP に Identity Linking・Catalog API・マルチアイテムカートを追加・Stripe／Salesforce が実装パートナーに |
| 2026-05-29 | [[2026-05-29_Shopify_ucp-catalog-developer-agentic-commerce]] | Shopify が UCP Catalog を全開発者に開放・Google の UCP Catalog API と連動し需給インフラが揃う |

---

## 監視ポイント

- **AP2 v1.0 の確定タイムライン**：FIDO Alliance での標準化スケジュールと、GENIUS Act・MiCA との整合評価。AP2 の仕様（GitHub: google-agentic-commerce/AP2）が最新の UCP 機能に合わせてアップデートされているかを継続確認。
- **AP2 と x402 の技術的相互運用性の確定**：「補完スタック」と説明されているが、実装レベルでの役割分担（エンドポイント仕様・認証フロー）がどう整理されるか。
- **Universal Cart への Google Pay / ステーブルコイン支払い追加**：現状はカード主体と思われるが、AP2 v0.2 の Human Not Present + USDC 決済の商用展開スケジュール。
- **Gemini Spark の AP2 統合リリース時期**：AP2 を Google 製品に統合する最初の製品として注目。
- **競合プレイヤーの追従動向**：Apple・Amazon・Microsoft・Meta が同等のエージェントコマース UI とプロトコル対応を発表するタイミング。
- **Identity Linking の規制整合**：ユーザーアカウントへのエージェントアクセスを伴う OAuth スコープ管理が GDPR・改正 PSD2 とどう整合するか。

---

## 参考リンク

- [Google Cloud ブログ：AP2 発表](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)
- [Google ブログ：FIDO Alliance 寄贈発表](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/)
- [Google Blog：Universal Cart（I/O 2026、2026-05-19）](https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/)
- [Google Blog：Marketing Live 2026 UCP 発表（2026-05-28）](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/)
- [CoinDesk：Consensus Miami パネル（2026-05-10）](https://www.coindesk.com/business/2026/05/10/agentic-commerce-will-run-on-crypto-rails-paypal-and-google-reps-tell-consensus-miami)
