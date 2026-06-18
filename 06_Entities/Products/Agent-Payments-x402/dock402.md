# dock402

## Overview

dock402 は `Building the App Store for x402` を掲げる multi-chain x402 SDK / infra project。GitHub 上では Base、Solana、Polygon、BSC、Sei、Peaq 対応や audit logging を打ち出し、client / server 両面の integration surface をまとめている。

## User Goal

multi-chain の x402 payment flow を、wallet adapter や facilitator endpoint を含めて短時間で試す。

## Business Goal

x402 の導入 friction を SDK 化で下げ、dApp / agent / usage-based billing 向け payment layer として採用を広げる。

## Category

- x402
- agent-payments

## Core Workflow

1. Developer は `dock402-x402-sdk` を導入する。
2. Client 側で wallet と network、max amount を設定する。
3. Server 側で payment requirements、verification、settlement を処理する。
4. paid resource access を multi-chain で有効化する。

## Pricing / Business Model

GitHub README では未確認。SDK / docs / hosted facilitator を含む developer infra モデルに見える。

## Differentiation

- multi-chain x402 を前面に出している。
- client / server example があり、`SDK + facilitator endpoint + wallet compatibility` まで 1 つの面に載せている。
- audit trails と compliance logging を README 上で訴求している。

## Operational Notes

- README ベースでは production-ready を掲げるが、実運用事例は未確認。
- supported wallet と framework coverage は広いが、self-hostability と settlement guarantees の確認が必要。
- reusable ではあるが、現時点では demo 寄り評価が妥当。

## Risks / Open Questions

- README 先行で、実トランザクション evidence が薄い可能性がある。
- facilitator 依存度が高い場合、permissionless さが弱まる。
- compliance logging が監査 artifact になるのか、単なる app telemetry なのか不明。

## Sources

- https://github.com/dock402
