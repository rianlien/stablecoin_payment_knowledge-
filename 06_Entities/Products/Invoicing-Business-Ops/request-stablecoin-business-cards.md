# Request Stablecoin Business Cards

## Overview

Request Stablecoin Business Cards は、Request Finance 内の USDC 残高を funding source に使う virtual business cards。invoice / payable / regulated verification の延長で spend controls を提供する。

## User Goal

stablecoin treasury を受け取った後、そのまま日常的な business spend に接続したい。

## Business Goal

Request Finance が invoicing / AP product から spend management まで領域を広げ、finance workflow の滞在時間を伸ばすこと。

## Category

invoicing, wallet-ux, compliance

## Core Workflow

business は Request Finance で verification を完了し、virtual cards を発行して USDC balance から 1:1 で funding する。管理者は spending limit、freeze / cancel、card activity review を同一 UI で行う。

## Pricing / Business Model

finance ops / spend management 型。カード手数料や issuance pricing の詳細は source 上で未確認。

## Differentiation

stablecoin invoice / payable 管理の次のステップとして、受け取った USDC の downstream spend を同じ product で持とうとしている点が practical。

## Operational Notes

導入前に issuance geography、employee eligibility、expense categorization、accounting sync、settlement timing、refund / dispute handling を確認したい。

## Risks / Open Questions

- 現時点では coming soon で一般提供前
- card transaction と onchain balance の同期モデルが未確認
- regulated verification の friction がどこまであるか要確認

## Sources

- https://help.request.finance/en/articles/12888867-cards-overview
