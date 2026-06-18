# AIP

## Overview

AIP は、MCP / A2A / HTTP をまたぐ multi-agent delegation で、identity、attenuated authorization、provenance を Invocation-Bound Capability Tokens として結びつける protocol / reference implementation。

## User Goal

複数 agent が tool access や payment intent を引き回す環境で、`誰が誰の権限で何を実行したか` を後から検証できるようにしたい。

## Business Goal

delegated agent workflows を安全に拡張し、payment や sensitive action を provenance-aware に制御できる基盤を作ること。

## Category

compliance, agent-payments

## Core Workflow

1. principal が task-scoped capability を agent に委譲する。
2. agent 間 delegation が起きるたび、authorization と provenance を token chain に継ぎ足す。
3. execution point で token の署名、scope、delegation depth、transport binding を検証する。
4. completion record を残し、後続監査や dispute review に使う。

## Pricing / Business Model

research artifact。商用化ポイントは identity middleware、delegated payment governance、enterprise audit layer、agent orchestration platform にある。

## Differentiation

単なる agent auth ではなく、`delegation provenance` を transport 境界を跨いで持ち運ぶ点が、stablecoin payments の spend governance と噛み合う。

## Operational Notes

- stablecoin wallet や custody layer と組み合わせるなら、capability scope と spend limit の整合が重要。
- Python / Rust reference implementation があるため、概念止まりではなく control-plane prototype として扱える。
- payment execution 自体ではなく authorization chain を補うので、x402 や wallet SDK の上位レイヤーとして見るのが自然。

## Risks / Open Questions

- payment-specific claims をどの粒度で token に埋めるべきか未確定。
- revocation、budget refresh、long-running workflow の扱いを実務で詰める必要がある。
- key custody と human override の設計が別途必要。

## Sources

- https://arxiv.org/abs/2603.24775
