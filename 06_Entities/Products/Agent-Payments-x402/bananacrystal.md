# BananaCrystal

## Overview

BananaCrystal は、AI agent が guarded な stablecoin 操作を行うための MCP-native payment toolset。balance 取得、KYC 状態確認、approval-based transfer、escrow などをまとめている。

## User Goal

agent に支払い機能を持たせつつ、人間の承認や compliance check を外さずに運用したい。

## Business Goal

agent payments を「自由な送金」ではなく「制御された実務フロー」として product 化すること。

## Category

agent-payments, wallet-ux, compliance

## Core Workflow

agent は MCP tool 経由で残高確認、KYC status 確認、取引リクエスト、承認待ち、approved transaction 実行を行う。必要に応じて escrow や cross-agent approvals を挟む。

## Pricing / Business Model

pricing は source 上で未確認。value は payment capability より risk-controlled execution surface にある。

## Differentiation

approval email、execution token、KYC read tool など、guardrail を初期機能として前面に置いている。agent transfer を安全に product 化する視点が強い。

## Operational Notes

Hedera wallet / stablecoin 前提の記述が多い。agent payment 実装で問題になる human override と recipient verification を product 側で吸収しようとしている。

## Risks / Open Questions

- chain coverage が Hedera 外に広がるか不明
- high-volume approval workflow に耐えるか不明
- custody boundary と liability boundary が不明

## Sources

- https://www.bananacrystal.com/
