# AnChain AML MCP

## Overview

AnChain AML MCP は、AnChain.AI の AML API を MCP server として公開し、crypto address screening や sanctions checks を agent workflow から呼べるようにする project。

## User Goal

stablecoin payment flow や wallet review flow の前後に、agent から compliance check を自動実行したい。

## Business Goal

AnChain.AI が blockchain risk / sanctions data を AI-native tool surface に広げること。

## Category

compliance, agent-payments

## Core Workflow

builder は MCP server を設定し、agent から wallet address や entity 情報を渡して screening を実行する。server は sanctions、IP risk、blockchain risk を返し、agent 側の review や routing に使える。

## Pricing / Business Model

server 自体は open-source。実利用は AnChain.AI AML API key が必要で、基盤収益はそこにある。

## Differentiation

compliance product を dashboard ではなく MCP tool として見せている点が新しい。payment ops を agent-assisted にするときの glue layer になり得る。

## Operational Notes

Bitcoin、Ethereum、Solana、Stellar、Tron など複数 chain をサポートする。実運用では block / allow の自動化範囲、人手レビュー接続、evidence logging の設計が必要。

## Risks / Open Questions

- advisory data と automated decisioning の境界が不明
- chain ごとの coverage quality 差があり得る
- audit trail と case management 連携がどこまで標準か未確認

## Sources

- https://github.com/anchainai/aml-mcp
- https://aml.anchainai.com/
