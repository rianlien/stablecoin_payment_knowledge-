# QuickNode x402 Payments

## Overview

QuickNode は `Build with AI` docs の中で x402 Payments を公開し、USDC micropayment が必要な API / digital resource へのアクセス制御を hosted infra 前提で実装できるようにしている。

## User Goal

developer が x402 merchant / facilitator の土台を一から組まずに、pay-per-request API や tool monetization を試したい。

## Business Goal

QuickNode の developer platform を AI-native payment / monetization layer まで拡張すること。

## Category

x402, agent-payments

## Core Workflow

developer は x402-enabled endpoint を用意し、payment-required response と payment verification を QuickNode docs に沿って実装する。client 側は x402 対応の支払いを実行し、USDC payment 完了後に resource にアクセスする。

## Pricing / Business Model

developer infrastructure 型。x402 支払いと QuickNode platform usage の両方が導入面に関わる。

## Differentiation

x402 を概念説明ではなく hosted path 付き docs として提示しているため、agentic payment を infra buyer がすぐ検証しやすい。

## Operational Notes

production 利用前には settlement timing、supported chains、charge / retry semantics、rate limit との統合、receipt logging を確認したい。

## Risks / Open Questions

- verification と settlement finality の responsibility がどこにあるか未確認
- supported assets / chains の広さが限定的かもしれない
- merchant-side fulfillment や partial failure handling の実装は別途必要

## Sources

- https://www.quicknode.com/docs/build-with-ai/x402-payments
