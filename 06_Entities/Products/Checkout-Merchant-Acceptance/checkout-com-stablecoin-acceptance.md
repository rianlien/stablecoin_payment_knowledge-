# Checkout.com stablecoin acceptance

## Overview

Checkout.com は 2026-06-02 に Coinbase Payments と組んだ stablecoin acceptance を発表した。enterprise merchant が既存 Checkout.com surface 上で stablecoin を payment method として追加できる形で、merchant に新しい crypto ops stack を要求しない。

## User Goal

既存 PSP / acquirer 導線を崩さずに、consumer の stablecoin 支払い需要を取り込む。

## Business Goal

enterprise payments portfolio に stablecoin を追加し、global demand capture と payment method breadth を強化する。

## Category

- checkout
- compliance

## Core Workflow

1. Merchant は既存 Checkout.com integration を前提に stablecoin acceptance を有効化する。
2. Consumer は stablecoin で支払う。
3. Coinbase Payments が裏側の payments infrastructure を担う。
4. Merchant は既存 trusted infrastructure の延長で stablecoin payment を受ける。

## Pricing / Business Model

公式発表では未確認。Checkout.com の enterprise payment stack の追加手段として提供されている。

## Differentiation

- `crypto checkout 専用 UI` ではなく既存 enterprise payment method portfolio の一部として見せている。
- MiCA や GENIUS Act など規制明確化を adoption signal として前面に出している。
- merchant 導入の焦点を wallet novelty ではなく operational simplicity に置いている。

## Operational Notes

- refund / dispute / settlement asset choice は一次ソースだけでは未確認。
- 導入対象は `eligible enterprise merchants` とされており、地域や underwriting 制約の確認が必要。
- stablecoin acceptance を既存 checkout/conversion stack の延長で扱うため、finance / risk / reconciliation の artifact がどこまで既存のまま使えるかが評価ポイント。

## Risks / Open Questions

- merchant settlement が fiat 固定なら、stablecoin treasury use case には弱い可能性がある。
- wallet / chain coverage が限定的だと consumer demand capture は部分最適に留まる。
- launch wording は強いが、live corridors と merchant availability は追加確認が必要。

## Sources

- https://www.checkout.com/newsroom/checkout-com-enables-stablecoin-acceptance-for-merchants-in-partnership-with-coinbase
