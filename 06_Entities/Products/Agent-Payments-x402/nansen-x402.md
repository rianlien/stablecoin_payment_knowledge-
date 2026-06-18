# Nansen x402 analytics access

## Overview

Nansen x402 analytics access は、blockchain analytics と wallet intelligence access を x402 の paid access model に載せる product signal。premium data product を request-native billing に落とせる点が実務上の主眼になる。

## User Goal

high-value analytics を、subscription 契約より軽く agent / internal tool から従量利用したい。

## Business Goal

premium data access を stablecoin rail で細かく monetization し、new usage path を増やす。

## Category

x402, agent-payments, compliance

## Core Workflow

buyer は analytics endpoint や intelligence resource にアクセスする際、x402 payment を添えて call する。provider は stablecoin の pay-per-use で data access を収益化する。

## Pricing / Business Model

公開 pricing は未確認。想定 value は `query per payment` または `resource unlock per payment` のような usage-based access。

## Differentiation

stablecoin payment を consumer checkout ではなく premium data monetization に使う点が特徴。compliance / trading / research で buyer value が明確なため、merchant acceptance より adoption route が現実的。

## Operational Notes

analytics product は access control、result caching、repeat access の扱いが商用化の分水嶺になる。x402 が fit するなら、usage granularity と permission boundary が product の中心になる。

## Risks / Open Questions

- live paid endpoint の有無が未確認
- KYB / allowlist と open paid access の関係が不明
- cached result や repeated request の billing policy が不明

## Sources

- https://www.x402.org/ecosystem
