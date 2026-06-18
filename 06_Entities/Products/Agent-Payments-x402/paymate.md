# PayMate

## Overview

PayMate は x402 payment-required response に対して、agent が事前に割り当てられた USDC budget と trusted provider list の範囲内で自動支払いできる middleware demo。

## User Goal

operator が agent に paid API を使わせたいが、勝手な spend や unknown provider への支払いは避けたい。

## Business Goal

agent payment に governance layer を足し、paid tool usage をより現実的な product pattern として見せること。

## Category

agent-payments, compliance, x402

## Core Workflow

operator は agent 用 wallet に USDC budget を prefund し、許可 provider を whitelist する。agent が x402 endpoint に遭遇すると、PayMate が provider と金額を検査し、条件内なら自動で支払って処理を続行する。

## Pricing / Business Model

showcase demo。商用モデルは未確認。

## Differentiation

approval pop-up ではなく、prefunding と trusted provider list によって agent payment を制御している点が practical。

## Operational Notes

production 化には provider reputation、wallet segregation、usage reporting、budget top-up、exception review flow が必要。micro-budget governance の観点では参考になる。

## Risks / Open Questions

- dispute と refund の operator flow が未確認
- multi-tenant isolation をどう担保するか不明
- trusted list 更新時の policy rollout が要検討

## Sources

- https://ethglobal.com/showcase/paymate-f3z7m
