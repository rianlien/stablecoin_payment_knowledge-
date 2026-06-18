# Five Attacks on x402 Agentic Payment Protocol

## Overview

Five Attacks on x402 Agentic Payment Protocol は、x402 merchant / payer flow に対する複数の attack path を整理し、本番利用に必要な anti-replay、verification、abuse control を明文化する security analysis。

## User Goal

x402 endpoint を公開したいが、demo レベルでは見えない exploit や merchant-side loss を事前に潰したい。

## Business Goal

x402 を安全に商用化するための threat model と hardening checklist を整え、導入障壁を下げること。

## Category

x402, agent-payments, compliance

## Core Workflow

1. x402 による paid access flow を前提にする。
2. paper は merchant / payer / protocol boundary で成立する 5 種類の attack を整理する。
3. reproducible testbed と live endpoint audit を通じて、authorization、binding、replay protection、web-layer handling の failure を示す。
4. operator はその結果を middleware や hosted gateway の設計に反映する。

## Pricing / Business Model

research artifact。価値は商用 x402 gateway、merchant hardening service、agent wallet governance product に転用しやすい点にある。

## Differentiation

spec の紹介ではなく、production threat model を attack taxonomy として明示している。`x402 can work` ではなく `x402 fails here` を先に示すタイプ。

## Operational Notes

- self-host 実装と hosted path で必要な対策が分かれる可能性が高い。
- receipt / audit artifact の保存面まで含めて設計した方が実務的。
- merchant が何をもって fulfillment 開始としてよいかを protocol 外で補う必要がある。

## Risks / Open Questions

- 5 attack のうち reference implementations で既に緩和済みのものがどれか未確認。
- reproducible testbed の code 公開範囲を追加確認したい。
- dispute handling や customer support まで落とし込める実装指針が出るか不明。

## Sources

- https://arxiv.org/abs/2605.11781
