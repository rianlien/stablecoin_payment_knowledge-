# Cryptorefills

## Overview

Cryptorefills は、暗号資産でギフトカードや eSIM などを購入できる既存 commerce platform に、AI agent 向け x402 checkout を追加した。agent は商品探索後に `HTTP 402` 経由で USDC on Base を支払い、そのまま購入完了できる。2026-05 には merchant operations reference repository も公開し、catalog discovery、quote handling、settlement reconciliation、delivery confirmation まで文書化している。

## User Goal

agent が人手承認なしで現実の商品購入を完了できること。

## Business Goal

merchant 側で agentic commerce の受け皿を作り、AI agent を新しい購買チャネルとして取り込むこと。

## Category

checkout, x402, agent-payments

## Core Workflow

1. Agent が商品や注文条件を取得する。
2. Merchant endpoint が `402 Payment Required` を返す。
3. Agent が USDC on Base で支払い証明を返す。
4. Merchant が決済確認後に fulfillment を行う。
5. Merchant は receipt、delivery confirmation、chain reconciliation を裏側で処理する。

## Pricing / Business Model

商品販売マージンが主と見られる。x402 自体は支払い rail であり、収益化の中心は commerce transaction。

## Differentiation

API monetization ではなく、実商品 checkout に x402 を接続している点が重要。さらに merchant operations 用の公開 playbook、TypeScript schemas、runnable examples まで出しており、agentic commerce の実務レイヤーまで見せている。

## Operational Notes

merchant 側では在庫、価格更新、delivery confirmation、refund、chain reconciliation が必須。公開 repository では live MCP / x402 endpoint に接続する runnable example もあり、導入時の論点が payment rail より merchant operations にあることが分かる。

## Risks / Open Questions

- 返金や fulfillment failure の設計が未確認
- fraud / abuse / agent identity 連携の扱いが未確認
- 対応 network が Base / USDC 中心でどこまで広がるか不明

## Sources

- https://www.cryptorefills.com/en/press-and-media/cryptorefills-launches-x402-payments-for-ai-agents
- https://github.com/Cryptorefills/agentic-commerce
