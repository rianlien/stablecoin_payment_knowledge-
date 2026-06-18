# Gbits

## Overview

Gbits は Swiss QR invoice payment と ISO 20022 accounting bridge を stablecoin でつなぐ product 群。`Gbits Pay` で QR invoice を stablecoin 支払いし、`Solana ISO20022 Gateway` で onchain transaction を Swiss accounting / banking format に戻す。

## User Goal

merchant や finance ops team が既存の Swiss invoice / accounting interface を壊さずに stablecoin payments を導入したい。

## Business Goal

stablecoin rail を front-end novelty ではなく back-office compatibility で差別化し、Swiss payments 向け infrastructure layer を握ること。

## Category

checkout, wallet-ux, invoicing

## Core Workflow

buyer は Swiss QR invoice を scan または upload し、VCHF、EURC、USDC などの Solana stablecoin で支払う。payment reference を memo に持たせ、merchant 側は camt.054 や camt.053 などの ISO 20022 statement / notification として accounting system に戻せる。

## Pricing / Business Model

明示 pricing は未確認。支払い app、gateway、accounting / ERP integration、possibly enterprise support が収益化ポイントと見られる。

## Differentiation

多くの stablecoin payment product が wallet UX か merchant acceptance に寄る中、Gbits は Swiss QR-bill と ISO 20022 という既存 interface を主語にしている。会計インポートまで product に含めている点が重要。

## Operational Notes

公式 site では `pain.001`、`camt.053`、`camt.054`、`semt.002` への対応を示し、Bexio / SAP / Abacus への import を前提にしている。現状は hackathon / beta 色が強いので、本番運用では identity verification、refund correction、ops support の確認が必要。

## Risks / Open Questions

- merchant / buyer verification を production でどう運用するか未確認
- Solana availability と Swiss corporate adoption の相性が未確認
- reconciliation support が single-corridor 以上に拡張できるか未確認

## Sources

- https://gbits.io/
