# Solana pay

## Overview

Solana Foundation の `pay` は、x402 / MPP に対応した payer-side runtime。CLI や MCP client の前段で 402 challenge を処理し、stablecoin payment の署名と retry をまとめて扱う。

## User Goal

paid API や paid MCP tool を agent から使いたいが、private key や API-wide credential を agent に直接持たせたくない。

## Business Goal

402-based machine payments の buyer runtime を標準化し、paid API access を日常の developer workflow に組み込むこと。

## Category

x402, agent-payments, wallet-ux

## Core Workflow

user は `pay setup` でローカル wallet / approval backend を準備する。CLI や agent が paid endpoint を叩くと、`pay` が x402 / MPP challenge を解釈し、stablecoin transaction を用意し、ローカル承認を受けて request を retry する。必要なら built-in MCP server や debugger UI も使える。

## Pricing / Business Model

open-source runtime。収益 model は明示されていないが、paid API ecosystem の利用拡大が主眼に見える。

## Differentiation

merchant-side library ではなく payer-side runtime を前面に出している点が実務的。さらに biometrics approval と local debugger を bundled にしている。

## Operational Notes

Touch ID、Windows Hello、GNOME Keyring / polkit など local approval を利用する。導入時は team wallet、approval delegation、usage logs の扱いを追加確認したい。

## Risks / Open Questions

- enterprise 向け shared wallet / approval flow が弱い可能性
- receipt logging や spend reporting が運用要件を満たすか未確認
- Solana 外の rail 拡張方針がどこまで現実的か

## Sources

- https://github.com/solana-foundation/pay
- https://pay.sh
