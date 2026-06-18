# A2A x402 Extension

## Overview

A2A x402 Extension は、Agent-to-Agent protocol 上で on-chain payment をやり取りするための x402 拡張 spec / library / examples リポジトリ。

## User Goal

paid agent service を、独自課金 handshake を毎回作らずに他 agent から利用可能にしたい。

## Business Goal

A2A x402 が agent-to-agent commerce の標準支払いフローになり、A2A agent を商用サービス化しやすくすること。

## Category

x402, agent-payments

## Core Workflow

merchant agent は `payment-required` を返し、client agent は署名済み支払い情報を `payment-submitted` として返す。merchant agent は検証・settlement 後に `payment-completed` でサービス結果を返す。

## Pricing / Business Model

open-source spec / library。収益化モデルは repo 上ではなく、これを使う paid agent service 側に属する。

## Differentiation

HTTP x402 的な支払いを A2A message flow に落とし込み、spec、core library、examples を multi-language 前提でまとめている。

## Operational Notes

実導入では fulfillment timeout、partial delivery、escrow、refund、identity binding、service reputation を別レイヤーで補う必要がありそう。

## Risks / Open Questions

- v0.1.0 ベースで production contract がまだ薄い
- dispute / refund / fulfillment failure の扱いが今後の争点
- x402 以外の payment scheme とどう共存するか未確定

## Sources

- https://github.com/google-agentic-commerce/a2a-x402
