# RAILS

## Overview

RAILS は、agentic commerce で必要になる payment、verification、fulfillment を clearing layer で束ねる verification-native architecture proposal。

## User Goal

agent 同士の有料取引を成立させたいが、支払い成功だけではなく履行確認と dispute boundary まで一緒に設計したい。

## Business Goal

machine commerce を本番運用できる clearing primitive を整え、paid API / paid agent network の trust cost を下げること。

## Category

agent-payments, x402, compliance

## Core Workflow

1. agent が有料サービスや resource を要求する。
2. clearing layer が payment intent、verification condition、release rule を扱う。
3. fulfillment が verification されてから value release される設計を目指す。
4. operator は dispute や failed execution を payment rail の外ではなく clearing primitive 内で扱える。

## Pricing / Business Model

research artifact。商用化ポイントは agent marketplace clearing、verified settlement infra、dispute / assurance middleware にある。

## Differentiation

単なる payment protocol ではなく、`verified clearing` を前提にしている。決済だけではなく fulfillment responsibility を product surface に乗せる点が重要。

## Operational Notes

- x402 の上に載る補完層なのか、別の settlement adapter を持つのかは未確定。
- verifier の trust model を誰が担うかで中央集権度が大きく変わる。
- high-frequency micropayments に使うなら latency budget の確認が必要。

## Risks / Open Questions

- public prototype や sample implementation の有無が未確認。
- human-in-the-loop dispute と fully automated verification をどう切り分けるか不明。
- commercial operator にとって clearing layer の追加複雑性が正当化されるか検証が必要。

## Sources

- https://arxiv.org/abs/2606.08790
