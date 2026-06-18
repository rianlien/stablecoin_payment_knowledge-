# UWAPI

## Overview

UWAPI は ETHGlobal Cannes 2026 の checkout + invoicing prototype。payer は任意の対応 crypto asset で支払え、merchant は USDC settlement を受け取れる。

## User Goal

buyer が持つ asset を固定せずに支払いを受け付けつつ、merchant 側の受取通貨と ledger は stablecoin で標準化したい。

## Business Goal

crypto-native payment acceptance の UX friction を減らし、merchant settlement と subscription billing を stablecoin basis に揃えること。

## Category

checkout, invoicing, wallet-ux

## Core Workflow

merchant は invoice や subscription を作成する。payer は wallet-agnostic checkout から支払い、backend が quote 取得と価格検証を行い、merchant には USDC が渡る。invoice と subscription state は chain 上に保存される。

## Pricing / Business Model

demo 段階で pricing は未提示。想定では payment routing、subscription billing、merchant tooling、possibly settlement spread が収益源。

## Differentiation

「merchant が何で受け取りたいか」と「payer が何を持っているか」を分離している点が強い。checkout と invoicing を別機能にせず、一つの payment normalization layer として扱っている。

## Operational Notes

Uniswap quote、Flare pricing、WalletConnect、ENS、subscription executor を組み合わせている。production では quote expiry、failed swap、renewal retry、merchant reconciliation export が導入論点になる。

## Risks / Open Questions

- volatile asset からの swap failure / slippage UX が未確認
- subscription renewal の user consent model が未確認
- chargeback 不在の merchant support flow が未確認

## Sources

- https://ethglobal.com/showcase/uwapi-uz7n4
