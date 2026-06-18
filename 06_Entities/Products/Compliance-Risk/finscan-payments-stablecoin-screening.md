# FinScan Payments stablecoin screening

## Overview

FinScan Payments stablecoin screening は、stablecoin transactions と digital wallet addresses を既存 payment screening framework に取り込む enterprise compliance solution。

## User Goal

stablecoin rail を扱い始めても、別の compliance vendor や別運用を増やさずに screening を回したい。

## Business Goal

FinScan が payment screening を `traditional rails + stablecoins` の単一運用面に拡張すること。

## Category

compliance

## Core Workflow

金融機関や fintech は既存の FinScan Payments integration を通じて、traditional rails と同じ API から stablecoin payment と wallet address screening を行う。sanctions、PEP、dual-use goods などのチェックを同時に回す。

## Pricing / Business Model

enterprise SaaS / compliance platform。価格は source 上で未確認。

## Differentiation

stablecoin 専用 point solution を別建てせず、既存 payment screening の延長として導入できる点が実務的。新しい rail を `同じ control framework` に入れたい buyer に刺さる。

## Operational Notes

OFAC、NBCTF、UK、UN など複数リスト対応が明示されている。実装前には wallet attribution、latency、false positive handling、case review workflow を確認したい。

## Risks / Open Questions

- on-chain attribution の精度が運用品質を左右する
- transaction monitoring と travel rule 連携の範囲が未確認
- real-time rails で screening latency が UX を損なう可能性

## Sources

- https://www.finscan.com/post/finscan-launches-digital-wallet-stablecoin-payments-screening-for-global-aml-sanctions-compliance
- https://www.finscan.com/payment-screening
