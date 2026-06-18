# Free-Riding in the AI Economy

## Overview

Free-Riding in the AI Economy は、x402-enabled payment systems における logic flaw を整理し、merchant 側の compute や API resource を実支払い前に引き出す `resource leakage` 問題を中心に分析した research prototype。

## User Goal

x402 paid API を公開したいが、実支払いが確定する前に resource だけ消費されるリスクを避けたい。

## Business Goal

machine-payments の monetization を成立させる前提として、merchant 側の revenue leakage と abuse cost を減らすこと。

## Category

x402, agent-payments, compliance

## Core Workflow

1. payer agent が x402-style access を要求する。
2. merchant は payment signal を受けて resource access を進める。
3. paper は Security Invariants、cross-resource substitution、concurrency race、allowance overdraft、resource leakage を整理する。
4. mitigation として request-bound signatures、pessimistic locking、tighter verification gate、fulfillment binding が必要になる。

## Pricing / Business Model

research artifact。直接の商用価格はなく、merchant hardening middleware や gateway product の設計 input としての価値が大きい。

## Differentiation

x402 adoption を増やす話ではなく、`merchant がどの瞬間に resource を解放してよいか` を中心課題としている点が practical。

## Operational Notes

- payment header の検証だけでは merchant 保護が不十分という示唆が強い。
- compute-heavy API や streaming response ほど影響が大きい。
- mitigation は latency や conversion rate を落とす可能性があるため、risk-based gate 設計が必要。

## Risks / Open Questions

- official SDK や live deployment の remediation 状況が未確認。
- x402 の各実装で再現条件がどこまで共通か追加確認が必要。
- refund / partial fulfillment を含むケースで leakage 判定をどうするか不明。

## Sources

- https://arxiv.org/abs/2605.30998
