# Strabo

## Overview

Strabo は、Universal Commerce Protocol の checkout interaction を declarative protocol として定義し、Peach agent で実装して既存 UCP agent と相互運用させる architecture prototype。

## User Goal

agentic checkout を作りたいが、wallet 接続や payment rail より先に quote、consent、fulfillment、failure handling の責務分界を明確にしたい。

## Business Goal

checkout orchestration を UI 実装依存から切り離し、merchant / buyer / agent 間の相互運用性と保守性を上げること。

## Category

checkout, agent-payments

## Core Workflow

1. UCP checkout interaction を declarative protocol として記述する。
2. Peach agent が protocol に従って quote、consent、order progression を処理する。
3. Google 実装の UCP agent と相互運用し、既存 stack を全面置換せずに導入できることを示す。
4. failure や obligation を protocol state として扱い、責務分界を code path より上で定義する。

## Pricing / Business Model

research artifact。商用化ポイントは merchant checkout orchestration layer、agent commerce SDK、protocol validation / simulation tool にある。

## Differentiation

checkout を payment button や wallet flow としてではなく、`declarative protocol` として切り出している点が核心。stablecoin rail の違いより前に、interaction design を formalize できる。

## Operational Notes

- wallet approval や settlement rail は別 layer として差し込む前提で読むのが自然。
- merchant fulfillment、refund、partial execution を protocol にどう載せるかが実務拡張点になる。
- 既存実装と相互運用できる前提は、導入ハードルを下げる現実的な signal。

## Risks / Open Questions

- public repo と runnable demo の有無は追加確認が必要。
- UCP checkout のうち payment-specific state がどこまで formalized されているかは abstract だけでは限定的。
- human approval UI と agent autonomy の境界をどう持たせるかは別設計が必要。

## Sources

- https://arxiv.org/abs/2606.05043
