---
title: "Agent Wallets（AIエージェント専用ウォレット）"
type: topic
updated: 2026-06-15
tags:
  - agent-payments
  - agentic-commerce
  - wallet
  - machine-payments
  - stablecoin
---

# Agent Wallets（AIエージェント専用ウォレット）

AI エージェントが自律的に資金を管理・送金・決済するために設計された専用ウォレットカテゴリ。従来のユーザー向けウォレットと異なり、エージェントが秘密鍵を持たず、ユーザーが定義した支出ルールの範囲内でのみ決済を実行できる「権限委任モデル」が設計の中核にある。2026年春以降、OwlTing・Coinbase Base・MetaMask・Alipay・Exodus・WSPN など複数のプレイヤーが立て続けにプロダクトをローンチし、独立したプロダクトカテゴリとして確立しつつある。

---

## 全体像

### 登場の背景

エージェント決済の普及に伴い、「エージェントがどこに資金を持ち、どう支払うか」というインフラ層の問題が顕在化した。従来のウォレット（MetaMask 等）はユーザーが操作することを前提としており、自律エージェントによる高頻度・小額・無人決済には適合しない。Agent Wallet はこのギャップを埋めるために設計された専用カテゴリである。

### 設計の共通原則

複数プレイヤーの設計を横断すると、以下の原則が収束しつつある：

1. **エージェントは秘密鍵を持たない**：鍵は TEE（Trusted Execution Environment）、MPC、スマートコントラクト、またはプラットフォーム管理のセキュアエンクレーブで保管される
2. **支出ルールはユーザーが設定**：日次上限・取引上限・許可加盟店リスト・レートリミットをインフラ層で強制
3. **自律性のグラデーション**：MetaMask の Guard Mode / Beast Mode に代表されるように、「常時承認」から「完全自動」の間でユーザーが自律度を選択できる設計が主流になりつつある
4. **ノンカストディまたは軽量カストディ**：中間者（エージェント発行者・ハブ）が資金を保管しない設計が規制対応と信頼確保の観点から好まれる

### アーキテクチャの多様性

| アーキテクチャ | 代表例 | 特徴 |
|---|---|---|
| TEE + スマートウォレット | Coinbase Base MCP | エージェントが鍵にアクセスせず、ユーザー承認フロー付き |
| セルフカストディ + MCP スキル | OwlTing OwlPay | 秘密鍵はユーザーデバイスにローカル保管、組み込みエージェントスキル付き |
| 秘密鍵不要の支出権限モデル | Exodus XO Cash + AgentKit | エージェントは「支出権限」のみ保有、Exodus Pay 残高から支出 |
| 消費者 UI 付き管理ウォレット | Alipay AI Wallet | 消費者がエージェントの支払いを管理・制御するコントロールパネル設計 |
| Guard / Beast Mode 二段階 | MetaMask Agent Wallet | DeFi 自律実行対応、保護プログラム（最大 $10,000）付き |
| マルチチェーン決済スキル | WSPN W Agent | 注文オーケストレーションと決済実行を分離した軽量ハブ設計 |

### 地理的多様性

欧米（OwlTing・Coinbase・MetaMask・Exodus）だけでなく、中国（Alipay AI Wallet）、アジア太平洋（WSPN W Agent）でも並行して独自設計が進んでいる。設計思想・規制対応の方向性に差異があり、グローバル統一標準にはなっていない。

---

## 主要ノート

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-05-04 | [[2026-05-04_OwlTing_owlpay-agent-wallet]] | 米国 40 州 MTL × Visa Direct 対応のセルフカストディ型エージェントウォレット正式ローンチ |
| 2026-05-08 | [[2026-05-08_Exodus_xo-cash-ai-agent-stablecoin]] | AI エージェント専用ステーブルコイン XO Cash と AgentKit SDK、Mastercard 加盟店対応 |
| 2026-05-15 | [[2026-05-15_WSPN_w-agent-stablecoin-ai-agent-payments]] | マルチチェーン対応エージェント決済スキル W Agent、APAC 向け設計 |
| 2026-05-26 | [[2026-05-26_Coinbase-Base_mcp-ai-agent-wallet]] | Base MCP：ChatGPT・Claude から TEE 管理のスマートウォレット経由でオンチェーン操作が可能に |
| 2026-05-26 | [[2026-05-26_Alipay_ai-wallet-token-pay-agentic-payments]] | Alipay AI Wallet（消費者向け管理 UI）と Token Pay（AI モデル企業向け API 課金）を同時発表 |
| 2026-06-08 | [[2026-06-08_MetaMask_ai-agent-wallet-launch]] | MetaMask Agent Wallet：Guard Mode / Beast Mode + 最大 $10,000 補償プログラム付きのリミテッドアーリーアクセス |

---

## 現状の論点

- **セキュリティモデルの標準化未完**：TEE vs. MPC vs. スマートコントラクト vs. セルフカストディという複数のアーキテクチャが並立しており、どれが業界標準になるかは未定。規制当局の「資金保管主体」の定義次第で有利不利が変わりうる
- **規制上の位置づけが不明確**：エージェントが自律実行する送金・決済が各国の MTL（送金業免許）・PPSI（支払いステーブルコインの発行規制）においてどの主体の行為として扱われるかが確定していない。OwlTing の 40 州 MTL は先行例だが、各州の解釈は未確認
- **自律性と人間制御のトレードオフ**：MetaMask Beast Mode や Alipay AI Wallet の設計が示すように、「エージェントに任せる範囲」と「ユーザーが最終承認を保持する範囲」のバランスをどこに置くかは製品ごとに異なる。EU AI Act・GENIUS Act の人間監視義務との整合が今後の焦点
- **プロトコル連携の欠如**：現状、多くの Agent Wallet は x402・AP2・MPP 等の決済プロトコルとの直接統合を宣言していない。Coinbase Base MCP が x402 と接続するかどうかが一つの試金石
- **中国・APAC の独自路線**：Alipay AI Wallet と WSPN W Agent は欧米プロトコルと異なる設計で進んでおり、グローバル相互運用性が課題になる可能性がある

---

## 監視ポイント

- MetaMask Agent Wallet の一般提供（数ヶ月以内）と、x402・AP2・CPN との統合発表の有無
- Coinbase Base MCP と x402 の直接統合（エージェントが DeFi 操作と同時に x402 決済を行えるか）
- GENIUS Act 最終規則化（〜2026-07-18）における「エージェント自律決済」の PPSI 定義への含否
- OwlTing・MetaMask・Exodus の AgentKit/SDK に対して、どの AI フレームワーク（LangChain・AutoGPT・Claude・OpenAI Agents 等）が正式統合を発表するか
- TEE ベースの鍵管理が規制当局に「セルフカストディ」と認定されるかどうか
- MoonPay + Monavate スタックが Exodus 以外のエージェントウォレットにも採用されるか（Mastercard 接続の標準化）
- Alipay AI Wallet のオープン API 公開の有無（サードパーティエージェントからの接続可否）

---

## 関連ページ

- [[agent-payment-authorization]]
- [[x402-ecosystem]]
- [[psp-merchant-readiness]]
- [[MOC_agent-payments-stack]]
