# Unwind

## Overview

Unwind は stablecoin checkout の弱点である refund を扱う demo で、返金時に元 asset を返すのではなく equivalent fiat value で正規化する設計を提案している。

## User Goal

merchant が stablecoin を受け入れたいが、返金時の価格変動や asset mismatch を customer support issue にしたくない。

## Business Goal

stablecoin checkout の adoption blocker である refund friction を product 化し、merchant 導入障壁を下げること。

## Category

checkout, compliance

## Core Workflow

customer が stablecoin で支払いを行う。merchant が refund を実行する際、Unwind が返金ポリシーに沿って equivalent fiat value を計算し、返金 amount / asset を調整する。

## Pricing / Business Model

showcase demo。商用モデルは未確認。

## Differentiation

acceptance flow ではなく post-payment refund flow を正面から扱っている点が珍しい。stablecoin checkout を導入判断する上で非常に実務的。

## Operational Notes

本番化には price oracle、refund eligibility、customer disclosure、gain/loss accounting、merchant support tooling が必要。refund policy を最初から明示しないと UX 事故になりやすい。

## Risks / Open Questions

- refund rate 固定タイミングが未定
- merchant accounting と consumer protection をどう両立するか不明
- fraud / abuse 対策の詳細が未確認

## Sources

- https://ethglobal.com/showcase/unwind-pqp3a
