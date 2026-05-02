---
title: "Google、エージェント決済プロトコル AP2 を FIDO Alliance に寄贈——v0.2 で「人不在決済」機能追加、60 社超参加"
date: 2026-04-28
source: "Google Cloud Blog / FIDO Alliance / The Paypers"
source_url: "https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol"
entity: "Google / FIDO Alliance"
category: "プロトコル標準化"
tags:
  - agentic-commerce
  - protocol
  - payments
  - regulation
summary: "Google が Agent Payments Protocol（AP2）v0.2 を 2026 年 4 月 28 日に FIDO Alliance へ寄贈。Mastercard が共同開発した「Verifiable Intent」標準と合わせてオープン標準化。60 社超（Mastercard・Adyen・PayPal・Coinbase・Revolut・UnionPay 等）が参加。v0.2 で追加された「Human Not Present」機能により、事前承認に基づくエージェント自律決済が可能になった。"
implications: "x402（Linux Foundation）・Stripe MPP・Circle Nanopayments に続き、AP2 が FIDO Alliance の中立的なガバナンスに移行することで、アジェンティック決済の国際標準争いが「オープンコンソーシアム vs. 特定プラットフォーム主導」の構図に入った。"
follow_up: "FIDO Alliance ワーキンググループの運営体制・公開タイムライン、AP2 v1.0 仕様の確定、x402 との統合・競合関係の整理"
---

## 概要

Google は 2026 年 4 月 28 日に Agent Payments Protocol（AP2）を FIDO Alliance へ寄贈し、アジェンティック決済の業界標準化を中立的なコンソーシアム主導へ移管した。AP2 は元々 2026 年 4 月 3 日に発表されたエージェント間決済プロトコルで、v0.2 ではエージェントが人間の事前承認に基づいて自律的に決済を実行する「Human Not Present（人不在決済）」機能が追加された。Mastercard と共同開発した「Verifiable Intent」標準も合わせて FIDO Alliance へ寄贈し、エージェントが実行した決済の改ざん不可能なログを残す仕組みも標準化される。

## 何が起きたか

- **FIDO Alliance 寄贈日**：2026 年 4 月 28 日
- **AP2 v0.2 主要追加機能**：
  - **Human Not Present（人不在決済）**：ユーザーが事前に承認した指示に基づき、エージェントが自律的に（例：限定チケットが発売と同時に購入する等）決済を完了できる機能
  - A2A（Agent-to-Agent）プロトコルの拡張として設計され、MCP（Model Context Protocol）とも連携可能
- **Verifiable Intent 標準**：Mastercard と共同開発。エージェントが実行した決済に対してユーザー承認の改ざん不可能なログを作成し、説明責任を担保する
- **参加組織（60 社超）**：Mastercard、American Express、Adyen、PayPal、Coinbase、Etsy、Forter、Intuit、JCB、Mysten Labs、Revolut、Salesforce、ServiceNow、UnionPay International、Worldpay 等
- **x402 との関係**：Google はすでに Coinbase・Ethereum Foundation 等と連携して AP2 への x402 拡張（A2A x402 extension）を開発済み——AP2 と x402 は競合ではなく、AP2 が認証・認可レイヤーを担い x402 が USDC 決済レイヤーを担うスタック構成
- **FIDO Alliance の役割**：AP2 の開発・メンテナンスをプラットフォーム中立なコンソーシアムに移管し、特定企業依存を排除

## なぜ重要か

### 決済事業者視点

- 60 社超の国際的な決済機関（カードネットワーク・PSP・フィンテック）が参加したことで、AP2 は x402・Stripe MPP よりも「業界標準」としての重みを持つ可能性がある
- FIDO Alliance の実績（パスキー等の認証標準）を考えると、AP2/Verifiable Intent は比較的短期で国際標準として採用されうる

### 加盟店視点

- Human Not Present 決済が標準化されると、AI エージェントが人間と同等の購買行為を自律的に実行できるようになる。加盟店は「エージェント向けの承認・ルール設計」を商品・決済フロー設計に組み込む必要が生じる

### プロダクト視点

- AP2（FIDO Alliance）・x402（Linux Foundation）・Stripe MPP・Circle Nanopayments の 4 インフラが並走する中、AP2 と x402 は「補完的スタック」として統合されつつあり、Stripe MPP は閉じたエコシステム、Circle Nanopayments は USDC 発行体主導という差別化軸が見えてきた
- 自社エージェント決済プロダクトを設計する際、AP2＋x402 のオープンスタックを選択すれば特定ベンダーロックインを避けられる

### 規制 / リスク視点

- Verifiable Intent（改ざん不可能な承認ログ）は、将来的な規制当局のエージェント取引監査要件に対応するインフラとして機能しうる
- FIDO Alliance への移管により、AP2 の仕様策定に規制当局が関与しやすくなり、各国規制との整合が加速する可能性

## 我々への示唆

- いま検討すべきこと:
  - AP2（FIDO Alliance）と x402（Linux Foundation）の統合スタックを自社エージェント決済のベースアーキテクチャとして評価する。Stripe MPP の閉鎖性・Circle Nanopayments の USDC 限定性と対比
  - Verifiable Intent の仕様を確認し、エージェント取引の監査証跡設計に組み込めるか評価
- 後で深掘りすべきこと:
  - FIDO Alliance のワーキンググループへの参加可否と、日本リージョンでの代表企業の動向
  - AP2 v1.0 の確定タイムラインと GENIUS Act・MiCA との整合評価
- 今は優先度が低いこと:
  - AP2 の非決済機能（エージェント認証など）の詳細仕様

## 未解決の論点

- AP2（FIDO Alliance）・x402（Linux Foundation）は補完的と説明されているが、実装レベルでどう役割分担されるか？
- Human Not Present 決済は GENIUS Act・MiCA における AML・消費者保護規制の「取引確認義務」とどう整合するか？
- Verifiable Intent の「改ざん不可能なログ」はオンチェーン記録か、オフチェーン署名か？

## 参考リンク

- 一次情報:
  - [Google Cloud ブログ：AP2 発表](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)
  - [Google ブログ：FIDO Alliance 寄贈発表](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/)
- 補足情報:
  - [The Paypers：FIDO Alliance 寄贈報道](https://thepaypers.com/payments/news/google-donates-agent-payments-protocol-to-fido-alliance)
  - [PYMNTS：Google・Mastercard と FIDO Alliance](https://www.pymnts.com/artificial-intelligence-2/2026/google-and-mastercard-contribute-agentic-commerce-standards-to-fido-alliance/)
  - [Coinbase：Google × x402 統合](https://www.coinbase.com/developer-platform/discover/launches/google_x402)
  - [既存ノート：x402 Foundation Linux Foundation 移管（2026-04-02）](2026-04-02_x402-Foundation_linux-foundation-launch.md)
  - [既存ノート：Stripe MPP（2026-04-30）](2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments.md)

## 重要度

- High

## 確からしさ

- High（Google 公式ブログ・FIDO Alliance 公式発表・複数メディア一致。4 月 28 日の寄贈日は明確に確認済み）
