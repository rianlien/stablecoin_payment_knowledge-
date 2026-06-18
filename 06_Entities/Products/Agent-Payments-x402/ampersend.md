# ampersend

## Overview

ampersend は、x402 を使う agent payment の management platform。SDK で agent に payment capability を入れつつ、Platform 側で budget、policy、approval、audit trail を管理する。

## User Goal

AI agent に stablecoin payment を持たせたいが、無制限 spend や監査不能な支払いを避けたい。

## Business Goal

agent payment の実行面ではなく control plane を押さえ、enterprise 向けの運用責任レイヤを product にする。

## Category

agent-payments, x402, compliance

## Core Workflow

開発者は SDK で agent に x402 payment client を組み込み、wallet と treasurer を設定する。運用側は Platform で agent ごとの budget、allowed merchants、approval rule を定義する。agent が支払いを実行すると、policy check と logging を通過した取引だけが進み、finance / risk team は dashboard から追跡・承認・停止できる。

## Pricing / Business Model

site 上では pricing 未確認。価値訴求は rail 手数料ではなく、payment governance と operational visibility の bundled 提供にある。

## Differentiation

wallet SDK ではなく、`agent payments and operations` を主語にしている点が特徴。buy side / sell side の両方を管理対象に置き、policy engine、approval、人手介入、audit trail を前面に出している。

## Operational Notes

enterprise で重要な `誰が承認するか`、`どこまで agent に任せるか`、`記録をどう残すか` を最初から product scope に含めている。stablecoin payment は transport ではなく governed workflow として扱われている。

## Risks / Open Questions

- custody boundary と signer ownership が docs 上でまだ曖昧
- accounting / ERP export の深さは未確認
- x402 exact scheme 以外の対応は未実装
- manual review queue の UX と SLA は要確認

## Sources

- https://ampersend.ai/
- https://docs.ampersend.ai/
- https://www.x402.org/ecosystem
