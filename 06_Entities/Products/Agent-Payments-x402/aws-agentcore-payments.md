# AWS AgentCore Payments

## Overview

Amazon Bedrock AgentCore payments は、AI agent 向けの managed payment capability。wallet 接続、x402 negotiation、支払い上限、observability をまとめて提供する。

## User Goal

本番 agent に安全な支払い機能を短期間で組み込みたい。

## Business Goal

enterprise agent stack の中で payments / governance / observability を AWS 管理領域に取り込むこと。

## Category

agent-payments, x402, compliance

## Core Workflow

開発者は payment connector を設定し、session ごとに spend limit を付与する。agent が paid resource に遭遇すると AgentCore が `402` 処理、wallet 認証、支払い、proof delivery を代行する。

## Pricing / Business Model

preview のため詳細 economics は未確認。value は managed service 化による開発工数削減と enterprise control にある。

## Differentiation

決済 rail 自体ではなく、governance と observability を product として前面に出している。enterprise 向けの実務設計。

## Operational Notes

予算上限、transaction trace、wallet connector 分離は、社内ガバナンスや監査対応に直結する。導入主体は PM ではなく platform team になりやすい。

## Risks / Open Questions

- chain / asset coverage がどこまで広がるか未確認
- failure recovery と dispute handling がどこまであるか未確認
- wallet ownership と end-user consent の実装責任分界が要確認

## Sources

- https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments.html

