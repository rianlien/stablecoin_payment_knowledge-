# Compliance-Aware Agentic Payments on Stablecoin Rails

## Overview

Compliance-Aware Agentic Payments on Stablecoin Rails は、x402-style payment authorization に policy wrapper と policy manager を組み合わせ、payment execution の時点で compliance 判定と attestation を入れる architecture prototype。

## User Goal

agent が stablecoin payment を実行する前に、制裁・地域・利用方針などの policy 判定を runtime で通したい。

## Business Goal

stablecoin payments を regulated setting に広げるため、compliance を後段 review ではなく execution gate に移し、manual exception cost を減らすこと。

## Category

compliance, agent-payments, x402

## Core Workflow

1. agent または client が x402-style authorization を作る。
2. policy wrapper が payment intent を policy manager に渡す。
3. modular compliance checks を通過した場合のみ execution を進める。
4. 判定結果や attestation を transaction と結びつけて残す。

## Pricing / Business Model

research artifact。商用化するなら compliance middleware、regulated payment gateway、policy attestation service の形が考えやすい。

## Differentiation

compliance を onboarding や batch review ではなく、`payment execution gate` そのものに置く点が重要。stablecoin payment の friction を後工程で吸収せず、runtime に寄せている。

## Operational Notes

- false block が conversion rate や agent completion rate を落とす可能性がある。
- policy manager の latency budget が short-lived API payments に耐えられるか確認が必要。
- attestation verifier が中央集権的だと、protocol 中立性より hosted governance に寄る。

## Risks / Open Questions

- runnable demo や public code が未確認。
- compliance rule の更新運用を誰が持つか不明。
- off-chain case review と fully automated block の境界がまだ曖昧。

## Sources

- https://arxiv.org/abs/2605.00071
