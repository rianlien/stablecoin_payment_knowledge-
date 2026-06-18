# BofAI x402

## Overview

BofAI x402 は、merchant、buyer、facilitator の x402 flow を Python / TypeScript で実装した GitHub repo。TRON、BSC、Base での stablecoin 支払い例と AI agent wallet skill を含む。

## User Goal

builder が x402 の責務分界と実装感をコードベースで理解し、ローカル環境で試したい。

## Business Goal

open-source reusable repo として x402 adoption を促進し、agent payment demo や merchant prototype の出発点を提供する。

## Category

x402, agent-payments

## Core Workflow

developer は repo を clone し、merchant service、facilitator、client を起動する。buyer または agent が payment-required endpoint にアクセスし、対応チェーン上の stablecoin 支払い後に protected resource を利用する。

## Pricing / Business Model

open-source project。commercial model は source 上で未確認。

## Differentiation

multi-chain demo と AI wallet skill まで含めており、x402 を単なる spec ではなく merchant system として理解しやすい。

## Operational Notes

repo は prototype / demo 色が強い。production へ進めるには wallet security、secret management、monitoring、idempotency、refund handling を自前で足す必要がある。

## Risks / Open Questions

- merchant ops 向け edge case がどこまで実装済みか不明
- multi-chain support が保守できる前提か未確認
- compliance / accounting layer は別建て前提

## Sources

- https://github.com/bofai/x402
