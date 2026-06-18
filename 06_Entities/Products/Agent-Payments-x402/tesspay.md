# TessPay

## Overview

TessPay は、agentic commerce 向けに `Verify-then-Pay` を中心に据え、mandate、escrow、Proof of Task Execution、rail-agnostic settlement、audit trail を束ねる trusted transaction infrastructure proposal。

## User Goal

agent に支払い付きタスクを任せたいが、先払いで終わらせず、履行確認と証跡を条件に資金解放したい。

## Business Goal

machine commerce の trust gap を埋め、settlement 成功だけでは足りない高額・高リスクフローを product 化できるようにすること。

## Category

agent-payments, compliance, checkout

## Core Workflow

1. user intent を mandate として定義し、agent discovery と authorization scope を固定する。
2. execution 前に資金を escrow し、agent は task を実行する。
3. task 結果に対して Proof of Task Execution を集め、verification predicate を満たした場合のみ資金を解放する。
4. transaction lifecycle 全体を tamper-evident audit trail として残す。

## Pricing / Business Model

research artifact。商用化ポイントは escrow orchestration layer、proof-based payout infra、trusted marketplace clearing、verification middleware にある。

## Differentiation

payment rail 自体ではなく、`verification before release` を transaction の中心に置いている。stablecoin rails を使う場合も、value transfer より release condition の方を product 差分にしている点が重要。

## Operational Notes

- rail-agnostic adapter 前提なので、stablecoin / fiat / closed-loop balance を横断して比較できる。
- verifier の trust model と latency budget が実運用では大きな争点になる。
- escrow 解放条件と dispute handling は checkout / fulfillment / compliance の共通設計問題として読める。

## Risks / Open Questions

- public code や smart contract 実装の有無は未確認。
- PoTE verifier を central operator が持つのか、market 参加者に分散させるのか不明。
- low-ticket micropayments でも overhead が許容されるかは未検証。

## Sources

- https://arxiv.org/abs/2602.00213
