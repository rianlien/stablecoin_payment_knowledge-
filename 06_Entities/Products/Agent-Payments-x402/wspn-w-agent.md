# WSPN W Agent

## Overview

W Agent は、WSPN が 2026-05-15 に公開した stablecoin payment skill。merchant discovery、order orchestration、stablecoin settlement をつなぎ、W Checkout を acquiring layer として使う。

## User Goal

AI agent が enterprise control を保ったまま merchant discovery から purchase completion まで進められるようにしたい。

## Business Goal

W Checkout を buyer-side payment rail ではなく merchant-side acquiring を含む agent commerce platform に拡張すること。

## Category

agent-payments, compliance, checkout

## Core Workflow

buyer-side AI agent が W Agent の hub 経由で merchant discovery と ordering を行い、stablecoin settlement は W Checkout で処理する。hub は orchestration、accounting、receipt を担当するが funds custody はしない。

## Pricing / Business Model

明示 pricing は未確認。W Checkout ベースの payment / acquiring infra として merchant / platform 導入で monetization すると見られる。

## Differentiation

payment execution だけでなく acquiring、receipt、accounting、human-in-the-loop control を一つの surface にまとめている点。multi-chain 前提も実務向き。

## Operational Notes

公式には per-transaction / per-day spending limits を設定でき、multi-chain settlement をサポートする。実運用では merchant onboarding、risk ownership、ERP export、exception handling を確認したい。

## Risks / Open Questions

- W Checkout outside の merchant に広げられるか不明
- general availability と実導入社数が未確認
- dispute、refund、merchant risk の責任分界が未確認

## Sources

- https://www.prnewswire.com/news-releases/wspn-launches-w-agent-a-stablecoin-payment-skill-built-for-the-ai-agent-economy-302773209.html
