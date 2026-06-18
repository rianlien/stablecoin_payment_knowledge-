# UQPAY x402 Stablecoin Platform

## Overview

UQPAY x402 Stablecoin Platform は、traditional merchant checkout と AI-initiated x402 payment を、単一の custodial / compliance core で扱う stablecoin acquiring platform。

## User Goal

merchant や platform が human payment と machine payment を別スタックに分けずに導入したい。

## Business Goal

UQPAY が stablecoin gateway ではなく、governed payment core として merchant / platform 導入を取りに行くこと。

## Category

checkout, x402, compliance, agent-payments

## Core Workflow

merchant は API または embedded integration で checkout と x402 gateway を使い、UQPAY の custodial account infrastructure 上で stablecoin acceptance、fiat settlement、transaction state、webhook orchestration を共通運用する。

## Pricing / Business Model

merchant acquiring / platform infrastructure 型。詳細 pricing は source 上で未確認。

## Differentiation

x402 を demo や spec のまま扱わず、intermediate transaction states、webhook reliability、merchant fulfillment coupling まで含む commercial core として位置づけている。

## Operational Notes

導入時は custodial responsibility、supported geographies、settlement timing、fulfillment retry、refund policy、KYB / AML handoff を確認したい。

## Risks / Open Questions

- production availability と live customer breadth が未確認
- custodial model の legal boundary が地域ごとに異なる可能性
- asynchronous settlement と merchant fulfillment の failure mode が要確認

## Sources

- https://www.prnewswire.com/apac/news-releases/uqpay-launches-commercial-grade-x402-stablecoin-platform-powered-by-ucp-302681187.html
