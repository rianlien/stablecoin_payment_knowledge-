# Circle CPN Managed Payments

## Overview

Circle CPN Managed Payments は、PSP、fintech、bank 向けの turnkey stablecoin settlement stack。partner は fiat workflow を保ちつつ、stablecoin settlement を単一統合で導入できる。

## User Goal

デジタル資産を直接保有せずに stablecoin rails を導入したい。

## Business Goal

Circle が issuance、liquidity、compliance、orchestration を束ね、stablecoin payments の managed layer を押さえること。

## Category

compliance, checkout

## Core Workflow

partner は API で sub-wallet、funding、payin / payout を操作する。裏側では Circle が mint / burn、onchain settlement、compliance、blockchain connectivity を処理する。

## Pricing / Business Model

managed service model。手数料や FX economics は要確認だが、value proposition は「build せず launch できる」点にある。

## Differentiation

custody、license、compliance build を不要化し、金融機関が fiat edge を保ったまま stablecoin rail を使える。

## Operational Notes

このモデルは導入障壁を下げる一方、regulatory perimeter と pricing power を Circle 側に集める。導入先は self-custody より managed adoption を選びやすい。

## Risks / Open Questions

- corridor / jurisdiction coverage の詳細要確認
- spread / compliance cost の実態要確認
- managed から self-managed への移行パスがどれだけ滑らかか不明

## Sources

- https://www.circle.com/en/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement
- https://developers.circle.com/cpn/managed-payments

