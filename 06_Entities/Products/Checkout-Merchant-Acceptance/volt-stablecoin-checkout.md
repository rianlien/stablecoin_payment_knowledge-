# Volt stablecoin checkout

## Overview

Volt stablecoin checkout は、online merchant 向けに wallet-based stablecoin acceptance を追加する checkout product。wallet connect、stablecoin selection、fiat conversion、reconciliation を Volt が吸収する。

## User Goal

merchant が既存 checkout を大きく崩さずに stablecoin 決済を受け付けたい。

## Business Goal

Volt の real-time payments stack に stablecoin acceptance を加え、borderless commerce 向けの checkout abstraction を強めること。

## Category

checkout, wallet-ux

## Core Workflow

merchant は Volt 経由で checkout に stablecoin option を追加する。buyer は wallet を接続し、指定された stablecoin で支払う。Volt は transfer、conversion、reconciliation、settlement choice を裏側で処理する。

## Pricing / Business Model

pricing の詳細は source 上で未確認。merchant 向け payment infrastructure / acceptance revenue model とみられる。

## Differentiation

merchant が stablecoin を直接扱わずに済む点と、checkout 内に fiat conversion と reconciliation を含めている点が重要。

## Operational Notes

merchant が accept する stablecoin と settlement asset を選べる設計で、user-facing は wallet checkout、merchant-facing は既存 payment ops に近い。

## Risks / Open Questions

- refund / fraud / dispute handling の詳細不明
- 対応 wallet と地域展開の広さが不明
- merchant economics と FX / conversion spread が不明

## Sources

- https://www.volt.io/newsroom/volt-launches-stablecoins-checkout/
