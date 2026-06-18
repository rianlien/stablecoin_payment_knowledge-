# PayDAO

## Overview

PayDAO は、real-time POS、QR、payment requests、payment links をまとめた merchant 向け stablecoin acceptance stack。

## User Goal

merchant が wallet address の受け渡しではなく、店頭やオンラインで自然に使える stablecoin checkout を簡単に立ち上げたい。

## Business Goal

PayDAO が small merchant や indie commerce 向けの lightweight stablecoin checkout layer として採用されること。

## Category

checkout, wallet-ux

## Core Workflow

merchant は POS もしくは payment request link を生成し、payer は QR や wallet で stablecoin を支払う。merchant は同じ surface で request と acceptance を扱える。

## Pricing / Business Model

source 上で pricing 明示は未確認。merchant SaaS、transaction fee、hosted checkout fee のいずれかが想定される。

## Differentiation

単なる payment button ではなく、POS と request artifact まで一体にしており、merchant 現場で必要な導線に寄っている。

## Operational Notes

reconciliation export、refund、underpayment、multi-chain confirmation policy、merchant support model を確認したい。

## Risks / Open Questions

- small merchant 向けゆえ support / dispute handling が薄い可能性
- custody boundary が source だけでは明確でない
- accounting export がないと継続運用しづらい

## Sources

- https://paydao.io/pay
