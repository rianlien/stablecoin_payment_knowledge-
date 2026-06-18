# APEX

## Overview

APEX は、HTTP 402 的な paid API access を crypto rail 前提ではなく UPI-like fiat flow で実装し、policy-aware spend control、tokenized verification、replay resistance をまとめた reference system。

## User Goal

agent が API を自律利用するときに、request ごとの課金、上限管理、replay 防止を実装したいが、stablecoin 前提に縛られたくない。

## Business Goal

payment rail を問わず、agent API monetization を `policy-driven approval + verifiable access` として成立させること。

## Category

agent-payments, compliance

## Core Workflow

1. API provider が paid endpoint に対して payment challenge を返す。
2. payer / agent 側が policy に沿って支払い可否を判定する。
3. settlement 完了後、short-lived verification token で access を consume する。
4. server 側は idempotent settlement と replay guard を使って重複消費を防ぐ。

## Pricing / Business Model

research artifact。商用化ポイントは paid API gateway、policy engine、merchant-side verification middleware、multi-rail monetization stack にある。

## Differentiation

stablecoin や x402 を否定するのではなく、`402-style paid access の本質は rail ではなく policy-enforced execution` だと示している点が重要。

## Operational Notes

- local payment rails に寄せた設計なので、stablecoin 導入時も approval policy と audit trail の要件比較に使いやすい。
- replay resistance と idempotent settlement を明示しており、merchant loss を protocol 外の運用でごまかしていない。
- 実運用では wallet、ledger、refund handling、team budget allocation を追加設計する必要がある。

## Risks / Open Questions

- public repo と runnable demo の有無は追加確認が必要。
- fiat rail 前提の設計を stablecoin rail に写すとき、どこまで簡略化できるか不明。
- cross-border settlement や compliance screening をどう差し込むかは source だけでは見えにくい。

## Sources

- https://arxiv.org/abs/2604.02023
