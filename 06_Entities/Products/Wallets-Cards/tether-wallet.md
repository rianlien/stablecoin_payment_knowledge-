# tether.wallet

## Overview

tether.wallet は Tether 公式の self-custodial wallet。USDt、USAt、XAUt、Bitcoin を保管・送受信でき、`tether.me` username による受取導線を持つ。

## User Goal

難しい wallet address 管理を最小化しながら、stablecoin を安全に送受信したい。

## Business Goal

Tether 経済圏の入口として、consumer / prosumer 向けの direct wallet relationship を取ること。

## Category

wallet-ux

## Core Workflow

ユーザーは self-custodial wallet を作成し、password と recovery phrase を保持する。受取時は network address か `tether.me` username / QR を共有し、送金時は対応 network 上で署名する。

## Pricing / Business Model

wallet 自体の課金は source 上で未確認。狙いは token ecosystem の distribution と retention と見られる。

## Differentiation

official Tether wallet として主要 Tether asset を束ねつつ、username 共有を前面に出して受取 UX を単純化している。

## Operational Notes

self-custody のため recovery と device migration の UX が重要。merchant / invoice system との接続はまだ薄く見える。

## Risks / Open Questions

- username discovery と privacy の設計要確認
- recovery / support 導線の実用性要確認
- business payments との接続面がどこまで広がるか不明

## Sources

- https://tether.io/news/tether-launches-tether-wallet-the-peoples-wallet-extending-its-global-financial-infrastructure-directly-to-billions-of-users-left-behind-by-the-traditional-financial-system/
- https://wallet.tether.io/

