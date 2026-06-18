# Base Account SDK Payments and Subscriptions

## Overview

Base Account SDK は、USDC payment、payment links、subscription、recurring billing を app account の中で扱える developer surface を提供している。stablecoin checkout を一回払いに留めず継続課金まで伸ばす方向。

## User Goal

builder が embedded wallet 体験に近い形で、stablecoin payment と recurring charge をアプリに組み込みたい。

## Business Goal

Base が app account と onchain commerce の default developer stack を取り、USDC payment volume を増やすこと。

## Category

checkout, wallet-ux, invoicing

## Core Workflow

developer は Account SDK で account を作成し、accept-payments ガイドに沿って USDC payment / subscription flow を実装する。user は app-native な payment surface の中で支払いと継続課金の許可を行う。

## Pricing / Business Model

developer platform 型。詳細 pricing は source 上で未確認。

## Differentiation

wallet setup と payment acceptance を分離せず、subscription / recurring billing まで同じ account surface に載せている。

## Operational Notes

consent renewal、failed payment retry、refund、invoice / receipt export、tax handling を product 側でどこまで持つかが adoption の分岐点になる。

## Risks / Open Questions

- recurring consent と authorization refresh の標準 UX が不明
- merchant-side accounting export がどこまであるか未確認
- Base 外部 rail や offchain billing system との接続前提が不明

## Sources

- https://docs.base.org/builderkits/account/guides/accept-payments
