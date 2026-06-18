# x402-secure

## Overview

x402-secure は、AI-driven x402 payments 向けの real-time risk control layer。x402 flow の前段に risk checks と signal collection を差し込み、fraud や dispute を減らす設計で紹介されている。

## User Goal

autonomous agent に支払い権限を持たせても、危険な支払いを実行前に止めたい。

## Business Goal

stablecoin / x402 payment runtime の前段に risk gate を差し込み、merchant protection を独立 product にする。

## Category

compliance, x402, agent-payments

## Core Workflow

merchant または platform は x402 payment flow の前に x402-secure を置く。payment request は risk checks と signal collection を通過し、問題がある取引は block または manual handling に回す。

## Pricing / Business Model

未確認。value は settlement rail ではなく risk reduction と dispute avoidance にある。

## Differentiation

KYT/OFAC のような generic screening だけでなく、agent behavior と request context を payment runtime に差し込む点が特徴。compliance を onboarding 外へ押し広げている。

## Operational Notes

agent payment の実務では `後で監査する` だけでは弱い。x402-secure の signal は、merchant protection の中心が execution-time gating へ移っていることを示す。

## Risks / Open Questions

- risk engine が hosted scoring か rules-based か不明
- false positive 時の override flow が不明
- signal retention と audit trail の運用責任が不明

## Sources

- https://www.x402.org/ecosystem
