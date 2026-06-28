---
title: "Ripple"
type: company
updated: 2026-06-28
category: blockchain-payments
tags:
  - x402
  - machine-payments
  - agentic-commerce
  - RLUSD
  - stablecoin
  - company
aliases:
  - RippleX
  - RLUSD
  - XRP Ledger
  - XRPL
---

# Ripple

Ripple は XRP Ledger（XRPL）ブロックチェーンと ODL（On-Demand Liquidity）を通じた国際送金・決済インフラを提供するフィンテック企業。USD 担保ステーブルコイン「RLUSD」を発行し、2026-06-10 に x402 プロトコルの XRPL 対応と「XRPL AI Starter Kit」を公開して AI エージェント決済分野に参入した。

この vault では、Ripple を「XRPL × RLUSD を基盤とする機関向けエージェント決済インフラの構築者」として追う。x402 プロトコルが初めて非 EVM チェーンに対応した重要なエコシステム拡張として位置づける。

---

## 現状の要約

### 何をしているか

- **x402 の XRPL 対応**：2026-06-10 にパートナー t54 Labs が x402 プロトコルを XRPL に実装し発表。これまで Base・Solana・Arbitrum 等 EVM 互換チェーンが主要対応チェーンだったが、初めて非 EVM チェーンが加わった。XRPL の 3〜5 秒確定ファイナリティ（ペンディング状態なし）がエージェントのリトライロジック不要という設計上の優位として訴求
- **XRPL AI Starter Kit**：XRPL 上でエージェント決済アプリを構築するための開発者向けツールキット。XRP（ネイティブ）と RLUSD の両方で支払いが可能。AI エージェントが API・コンピューティング・デジタルサービスを x402 経由で自律決済できる
- **RLUSD**：Ripple が発行する USD 担保ステーブルコイン。XRPL ネイティブ発行で、XRPL の DEX を通じて他通貨と交換可能。エンタープライズグレードを訴求しているが、GENIUS Act PPSI 申請状況は未確認（2026-06-10 時点）
- **RLUSD 日本ローンチ（JFSA 承認）**：2026-06-24 に SBI グループとの連携で JFSA から「第4種電子決済手段」の認可を取得——外国発行ステーブルコインとして日本国内初の規制承認事例。SBI VC Trade（VCTRADE）を通じて機関・リテール双方に提供。初期流動性プールは Ethereum 上に構築（XRPL は初期対象外）。時価総額は約 17 億ドル。Circle × 野村の USDC FX 決済プラットフォームと同時期に参入し、日本市場での二頭体制が形成
- **Mastercard AP4M 参加**：2026-06-10 に Mastercard が AP4M（Agentic Payments for Machines）をローンチし、RippleX が 35 社超の launch partner の一社として参加。AP4M は RLUSD/XRPL での決済をサポート
- **既存インフラ**：ODL（XRP を流動性ブリッジとして使う国際送金ソリューション）を通じて多くの銀行・送金事業者と提携実績あり。Ripple は 2024 年に SEC との長期訴訟を和解

### 見立て

Ripple の強みは、既存の銀行・金融機関への ODL 経由のリレーションシップ。XRPL を x402 に対応させたことで、これらの機関が機関向け AI エージェント決済インフラとして XRPL/RLUSD を選ぶルートが整った。ただし x402 エコシステムの主要チェーンは依然 Base（Coinbase）であり、XRPL の採用には時間がかかると見られる。RLUSD の GENIUS Act PPSI 申請状況が米国内普及の鍵で、未申請の場合は GENIUS Act 施行後の利用に制限がかかる可能性がある。2026-06-24 の JFSA 承認（第4種電子決済手段）は、日本市場における機関向け RLUSD 活用の法的根拠を確立した。初期は Ethereum ベースのため XRPL との連携は今後の課題だが、SBI グループとの 2016 年来のリレーションシップが日本での早期普及を後押しする。Circle（USDC × 野村）と日本市場での競合が本格化しており、2027 年を見据えた国内クロスボーダー決済インフラの主導権争いとなる見通し。

---

## Inbox との紐付け

| 日付 | ノート | 位置づけ一行 |
|---|---|---|
| 2026-04-23 | [[2026-04-23_CryptoCoalition_clarity-act-senate-letter]] | Ripple が CLARITY Act マークアップを求める業界連名書簡に参加 |
| 2026-05-08 | [[2026-05-08_Consensus-Miami_stablecoin-permission-slip]] | Ripple SVP が「機関採用に必要な 3 要素」を Consensus Miami で整理——規制・信頼・ユーティリティ |
| 2026-06-10 | [[2026-06-10_Ripple_xrpl-ai-starter-kit-x402-rlusd]] | XRPL AI Starter Kit と x402 XRPL 対応——初の非 EVM チェーン対応で Mastercard AP4M にも参加 |
| 2026-06-24 | [[2026-06-24_Ripple-SBI_rlusd-japan-jfsa-launch]] | RLUSD の日本ローンチ——JFSA「第4種電子決済手段」規制承認、外国発行ステーブルコインとして国内初 |
