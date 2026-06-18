# SpherePay Offloader Wallets

## Overview

SpherePay Offloader Wallets は、顧客専用 wallet への stablecoin 着金を自動で fiat に変換し、銀行口座へ送る conversion automation product。

## User Goal

stablecoin を受け取っても treasury に残さず、顧客ごとに attribution を保ったまま bank payout したい。

## Business Goal

SpherePay が off-ramp automation を wallet primitive として押さえること。

## Category

wallet-ux, compliance

## Core Workflow

platform は customer ごとに Offloader Wallet を作成する。顧客はその address に stablecoin を送金し、SpherePay が linked bank account へ fiat 変換して送る。

## Pricing / Business Model

API / infrastructure 型。詳細 pricing は source 上で未確認。

## Differentiation

都度 payout API を叩くモデルではなく、wallet 自体を auto-conversion endpoint にしている点。

## Operational Notes

導入時は customer-per-wallet 運用、webhook 不在時の監視、bank return handling、attribution failure を確認したい。

## Risks / Open Questions

- webhooks 非対応で運用監視に工夫が必要
- shared wallet 不可のため address 数が増えやすい
- beneficiary check と payout failure 時の責任分界が未確認

## Sources

- https://docs.spherepay.co/platform/offloader-wallets/
