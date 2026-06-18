# StableInvoicing

## Overview

StableInvoicing は、freelancer と small business 向けに stablecoin invoice 発行、payment link、on-chain detection、PDF invoice をまとめた invoicing SaaS。

## User Goal

国際請求を PayPal や wire より安く早くしたいが、wallet address のやり取りだけでなく invoice artifact と paid status も欲しい。

## Business Goal

StableInvoicing が SMB 向け stablecoin invoicing の軽量 default tool になること。

## Category

invoicing, checkout, wallet-ux

## Core Workflow

user は invoice を作成し、対応 stablecoin と chain を選び、payment link を client に送る。client は stablecoin か bank transfer で支払い、platform は on-chain detection で invoice を paid に更新する。

## Pricing / Business Model

free plan は月 5 invoice。zero platform fee を打ち出し、上位プランで recurring billing や client portal を提供する構成。

## Differentiation

stablecoin invoicing を crypto-native 向けではなく、`PDF invoice + bank transfer coexistence + EIP-681 QR` の実務 UX に落としている。

## Operational Notes

税務適合 PDF の jurisdiction 範囲、accounting export、wrong-chain payment 対応、customer support、bank transfer reconciliation を確認したい。

## Risks / Open Questions

- small-business tool として support operation の厚みが未確認
- invoice volume が増えた時の ops / accounting integration が不明
- non-custodial 前提で返金や誤送金の handling が難しい可能性

## Sources

- https://stableinvoicing.com/
