# Infinite Accounts

## Overview

Infinite Accounts は、dedicated bank account と stablecoin functionality を統合した embedded payments product。ACH、wire、deposit account、stablecoin 決済を単一 API surface にまとめる。

## User Goal

platform や fintech が、自社ブランドで fiat と stablecoin の両方を自然に扱う account experience を提供したい。

## Business Goal

compliance と provider routing を裏側に閉じ込め、embedded stablecoin adoption の enablement layer になること。

## Category

wallet-ux, compliance, checkout

## Core Workflow

事業者は Infinite に一度統合し、end user に dedicated account を発行する。deposit、withdraw、ACH、wire、stablecoin の機能を同一プロダクト内で扱う。

## Pricing / Business Model

B2B platform model と見られる。program terms、transaction limits、banking partner 条件の影響が大きい。

## Differentiation

stablecoin wallet を前面に出さず、bank account UX を保ったまま stablecoin rail を差し込む設計。B2B 導入の現実に寄っている。

## Operational Notes

reconciliation、provider routing、compliance checks を abstraction しているが、実際の onboarding friction と supported corridors が競争力を左右する。

## Risks / Open Questions

- supported stablecoins / networks / countries が未確認
- statement / ledger UX の深さが未確認
- banking partner 依存の制約がどの程度あるか不明

## Sources

- https://www.prnewswire.com/news-releases/infinite-launches-dedicated-bank-accounts-for-embedded-stablecoin-and-fiat-payments-302749555.html

