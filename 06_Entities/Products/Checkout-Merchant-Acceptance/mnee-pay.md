# MNEE Pay

## Overview

MNEE Pay は、stablecoin checkout widget / hosted link / API を提供し、merchant 側には MNEE で instant settlement を返す checkout product。

## User Goal

merchant として stablecoin acceptance を早く始めたいが、settlement と treasury handling を自前で抱えたくない。

## Business Goal

MNEE が checkout と settlement asset の両方を支配する payment surface を作ること。

## Category

checkout, compliance

## Core Workflow

merchant は account を作成し、widget か hosted link か API で checkout を埋め込む。payer は ERC-20 stablecoin で支払い、smart conversion により merchant は MNEE で受け取る。

## Pricing / Business Model

merchant checkout / settlement product。詳細 pricing は source 上で未確認。

## Differentiation

payer asset と merchant settlement asset を分け、merchant 側の treasury experience を単純化しようとしている点。

## Operational Notes

導入前に MNEE exposure、bank withdrawal route、refund semantics、jurisdiction coverage、merchant reporting を確認したい。

## Risks / Open Questions

- MNEE 受取が merchant に追加リスクとして見える可能性
- supported jurisdictions と withdrawal partners が未確認
- chargeback / refund の operational model が不透明

## Sources

- https://www.mnee.io/mnee-pay
