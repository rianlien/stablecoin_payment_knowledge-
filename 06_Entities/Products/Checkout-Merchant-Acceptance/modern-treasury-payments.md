# Modern Treasury Payments

## Overview

Modern Treasury Payments は、fiat と stablecoin を単一 API、ledger、reporting、compliance layer で扱う PSP。2026-04-29 には Polygon 上の USDC を統合した。

## User Goal

platform や fintech が、複数 rail を横断する money movement product を少ない統合コストで出したい。

## Business Goal

fiat/stablecoin 複合の payment stack を Modern Treasury の orchestration と ledger に集約すること。

## Category

checkout, compliance

## Core Workflow

customer は Modern Treasury を通じて account を開設し、ACH、wire、RTP/FedNow、push-to-card、stablecoin を同じ integration で扱う。compliance、ledgering、reporting は platform 側に統合される。

## Pricing / Business Model

usage-based pricing。value proposition は BaaS 的な長い銀行導入を省きながら、成長後も同じ integration を維持できる点。

## Differentiation

stablecoin を別プロダクトにせず、multi-rail PSP の一部として扱っている。bank onboarding、compliance、ledgering をまとめる enterprise 向け abstraction。

## Operational Notes

Polygon 統合の打ち出しから、stablecoin rail 自体の差ではなく「既存の payment ops にどう埋め込むか」が主戦場になっている。

## Risks / Open Questions

- stablecoin rail ごとの economics と support 差分が不明
- end-user facing reconciliation UX の深さが不明
- direct bank relationship へ移る際の migration friction が不明

## Sources

- https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-launches-payments
- https://www.moderntreasury.com/newsroom/press-releases/modern-treasury-integrates-with-polygon-to-accelerate-stablecoin-payments
