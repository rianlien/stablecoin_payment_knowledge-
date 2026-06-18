# Onvo

## Overview

Onvo は ETHGlobal Cannes 2026 で公開された B2B stablecoin invoicing demo。invoice PDF hash の onchain anchoring、World ID による issuer gating、USDC / EURC payment link を一つの flow にまとめている。

## User Goal

invoice の真正性を担保しながら、cross-border B2B invoice を stablecoin で支払える workflow を持ちたい。

## Business Goal

paper-based invoicing を cryptographically verified workflow に置き換え、verification と payment status を同じ system で管理すること。

## Category

invoicing, compliance

## Core Workflow

issuer は split-screen form で invoice を作成し、PDF hash を生成して onchain に登録する。World ID proof が通った emitter だけが invoice を発行できる。payer は unique payment link から wallet 接続し、USDC または EURC で支払う。invoice status は onchain で追跡される。

## Pricing / Business Model

demo 段階で pricing は未提示。将来的には invoice issuance、compliance / verification、payment processing、commission split が収益源になりうる。

## Differentiation

stablecoin invoice product の論点を「payment acceptance」ではなく、issuer verification と tamper-proof source of truth に置いている点が強い。Factur-X XML まで視野に入れているのも実務的。

## Operational Notes

Arc testnet 上の `InvoiceRegistry`、World ID 4.0 verification、configurable commission split が明示されている。production を考えるなら、business verification、invoice correction、region-specific e-invoicing compliance を別途詰める必要がある。

## Risks / Open Questions

- World ID だけで business-grade KYC / KYB を置き換えられない
- legal invoice requirements を jurisdictions ごとに満たせるか未確認
- cancellation、credit note、partial payment の UX が未確認

## Sources

- https://ethglobal.com/showcase/onvo-f69m7
