# Cash App stablecoins

## Overview

Cash App は 2026-05-27 に、eligible customer 向け USDC send / receive を正式公開した。特徴は stablecoin balance をそのまま見せるのではなく、自動 conversion により app 内の USD balance に吸収する点にある。

## User Goal

standalone crypto wallet を管理せずに、stablecoin rails を使って送受金する。

## Business Goal

59 million monthly customers を open financial rails に乗せつつ、consumer UX を既存 Cash App balance の延長に保つ。

## Category

- wallet-ux

## Core Workflow

1. User は Cash App 内で USDC send / receive を選ぶ。
2. 送金時は USD balance から stablecoin rail に変換される。
3. 受取時は supported network の address を発行し、入金された USDC を自動で USD balance に変換する。
4. User には unified balance として見せる。

## Pricing / Business Model

公式発表では USDC send / receive は開始時点で fee-free。promo 後の恒久 fee model は未確認。

## Differentiation

- token balance を見せず、`USD balance on open rails` として stablecoin を抽象化している。
- Solana、Ethereum、Polygon、Arbitrum をサポートしつつ、consumer UI は 1 つの money app に閉じている。
- bitcoin-first positioning を維持しつつ stablecoin を onboarding rail として使っている。

## Operational Notes

- incompatible network / unsupported asset 送付は irreversible loss と明示されている。
- New York residents は対象外。
- merchant / invoice / recurring billing への接続は一次ソースでは未確認。

## Risks / Open Questions

- abstraction は強いが、誤送金 recovery UX が弱いままだと support cost が高い。
- user が stablecoin そのものを保持したい用途には向かない可能性がある。
- cross-border use case の compliance / payout artifact がどこまで整うか未確認。

## Sources

- https://cash.app/press/cash-app-stablecoins-all-customers
