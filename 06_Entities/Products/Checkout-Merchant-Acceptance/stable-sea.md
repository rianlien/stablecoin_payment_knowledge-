# Stable Sea Enterprise API

## Overview

Stable Sea Enterprise API は、stablecoin collection、conversion、global payout を一つの API surface にまとめる business payments layer。

## User Goal

business / platform が stablecoin rail を使いたいが、collection、conversion、payout、cross-border ops を個別実装したくない。

## Business Goal

Stable Sea が enterprise 向け stablecoin operations API として fintech や marketplace に採用されること。

## Category

checkout, compliance

## Core Workflow

business は API 経由で stablecoin を受け取り、必要に応じて conversion を行い、そのまま global payout や treasury workflow に接続する。

## Pricing / Business Model

enterprise API。pricing は公開 source 上で未確認。volume-based fee または managed service fee が想定される。

## Differentiation

stablecoin payment を wallet UX ではなく `collection / conversion / payout` の業務 API に落としている点が強い。

## Operational Notes

KYB、supported jurisdictions、safeguarding、payout exception handling、ledger export、settlement SLA を事前確認したい。

## Risks / Open Questions

- compliance responsibility boundary が不明確だと enterprise 導入で止まりやすい
- payout failure / reconciliation mismatch 時の運用負荷が見えない
- public docs が薄い場合、実装確度を判断しづらい

## Sources

- https://www.stablesea.com/enterprise-api
