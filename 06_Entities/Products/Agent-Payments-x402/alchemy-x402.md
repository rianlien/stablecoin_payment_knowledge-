# Alchemy x402 monetized APIs

## Overview

Alchemy x402 monetized APIs は、blockchain developer platform の RPC / web3 API access を x402 で従量課金できるようにする product signal。x402 ecosystem では、AI agents や applications が stablecoins で RPC calls や web3 APIs に支払える方向として紹介されている。

## User Goal

paid API を account provisioning や monthly contract より細かく、request-native に売りたい / 使いたい。

## Business Goal

developer infra の usage billing を agent-native stablecoin rail に載せ、new buyer segment を取る。

## Category

x402, agent-payments

## Core Workflow

provider は paid endpoint を x402 対応にする。buyer 側の app / agent は request 時に支払いを添えて RPC や API を実行する。stablecoin settlement で pay-per-call access を成立させる。

## Pricing / Business Model

source 上では pricing 未確認。ただし value proposition は subscription より従量 access にあり、stablecoin rail は collection primitive として機能している。

## Differentiation

checkout ではなく infra billing を前面にした点が重要。stablecoin payment の最も自然な導入先が paid API であることを示す。

## Operational Notes

agent economy では human-friendly signup より machine-friendly authorization が重要になる。Alchemy のような infra seller が x402 を使うなら、payment UX の中心は buyer wallet ではなく `rate limit / idempotency / quota` になる。

## Risks / Open Questions

- live endpoint availability が未確認
- enterprise billing と per-request billing の共存設計が不明
- underpayment / failed execution 時の handling が不明

## Sources

- https://www.x402.org/ecosystem
