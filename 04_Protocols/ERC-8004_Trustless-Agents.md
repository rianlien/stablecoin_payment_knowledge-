---
title: "ERC-8004: Trustless Agents — AI エージェント間信頼インフラ"
date: 2026-04-24
source: Ethereum EIPs / Ethereum Magicians
source_url: https://eips.ethereum.org/EIPS/eip-8004
entity: Ethereum コミュニティ（主導: Davide Crapis et al.）
category: protocol
tags:
  - erc
  - agentic-commerce
  - protocol
  - x402
  - wallet
summary: >
  AI エージェントが事前の信頼関係なしに相互発見・認証・評判評価できる
  オンチェーン・レジストリ群を定義する ERC 規格。x402 と組み合わせることで
  エージェント間のステーブルコイン決済スタックの「信頼レイヤー」を担う。
status: draft
---

## 概要

- **プロトコル名**: ERC-8004（Trustless Agents）
- **開発主体**: Davide Crapis（davidecrapis.eth）、Marco De Rossi、Jordan Ellis、Erik Reppel。Consensys・Nethermind・Google・TensorBlock がフィードバック参加
- **対象ユースケース**: AI エージェント間の自律的なサービス発見・信頼確立・説明責任
- **対応チェーン / ネットワーク**: Ethereum メインネット（L2 互換設計）
- **ライセンス**: ERC（オープン標準）

---

## 何を解決するプロトコルか

### 課題

Google の A2A や Anthropic の MCP は、エージェント間の通信フォーマットや機能広告の仕組みは定義しているが、以下が欠如している：

- **エージェント発見**: 組織の壁を越えてエージェントを見つける共通基盤がない
- **信頼の確立**: 事前関係なしに相手の信頼性を検証できない
- **説明責任**: エージェントの行動履歴を追跡・評価するオンチェーン基盤がない

### アプローチ

3 つの軽量オンチェーン・レジストリを標準化することで、エージェントが「信頼できる相手かどうか」を自律的に判断できる共通インフラを提供する。

---

## 技術仕様

### アーキテクチャ

軽量なオンチェーン・レジストリ群として設計。データの多くはオフチェーン（URI 参照）に保持し、オンチェーンは ID・評判・検証の最小限のアンカーのみを管理する。

### 主要コンポーネント

#### 1. Identity Registry（アイデンティティ・レジストリ）
- ERC-721（NFT）の URIStorage 拡張を基盤に実装
- 各エージェントに検閲耐性のある永続的識別子を付与
- URI が指す「登録ファイル」にサービス内容・エンドポイントを記述

#### 2. Reputation Registry（評判レジストリ）
- クライアントが署名付き評価をオンチェーンに投稿する標準インターフェース
- タグ付け・ファイルベースの評価に対応
- 高度な集計はオフチェーンで行うことを想定

#### 3. Validation Registry（バリデーション・レジストリ）
- エージェントがタスクを約束通り完了したかを独立した検証者が確認する汎用フック
- リスクレベルに応じた複数の信頼モデルに対応：
  - ステーク担保型の再実行（Re-execution）
  - zkML（Zero-Knowledge Machine Learning）証明
  - TEE（Trusted Execution Environment）オラクル

### API / インターフェース

ERC 標準インターフェースとして定義。スマートコントラクト間の呼び出しよりもオフチェーンの集計処理との組み合わせを主ユースケースと想定している。

### 対応通貨・アセット

直接の決済機能は持たない。決済は x402 や ERC-4337 に委譲する設計。

---

## エコシステム・採用状況

### 主要参加者・パートナー

- 提案者チーム：Davide Crapis（主導）、Marco De Rossi、Jordan Ellis、Erik Reppel
- フィードバック参加：Consensys、Nethermind、Google、TensorBlock

### 実採用事例

- 2026年1月29日、Ethereum メインネットにデプロイ
- 草案段階（Draft）のため本番採用事例は限定的

### 競合・類似プロトコル

| プロトコル | 違い |
|-----------|------|
| Google A2A | 通信フォーマット・機能広告の標準化が主目的。信頼確立・評判はスコープ外 |
| Anthropic MCP | ツール呼び出しの標準化が主目的。エージェント ID・評判管理は範囲外 |
| ERC-8028 | ERC-8004 の姉妹提案。エージェント経済のアセット・資産モデル（トークンエコノミクス）に特化 |

---

## 決済事業者・PSP としての評価

### 統合のしやすさ

- 直接の決済処理機能を持たないため、PSP が単独で統合する場面は限られる
- x402 ＋ ERC-8004 ＋ ERC-4337 のスタックとして評価する必要がある
- レジストリ自体は ERC 標準準拠のコントラクトで、L2 へのデプロイも容易

### コンプライアンス対応

- KYC/AML への直接対応は仕様スコープ外
- Validation Registry の zkML・TEE オラクル機能を活用したコンプライアンス拡張は理論的に可能
- 規制上の扱い（エージェント ID を法的に有効な本人確認と見なせるか）は未整理

### スケーラビリティ・コスト

- Identity Registry は ERC-721 ベースのため、L2 上では$0.001 以下でのミント・参照が見込まれる
- 評判・バリデーションのオンチェーン書き込みは頻度と設計次第でコストが変動
- x402 の $0.001 以下のマイクロペイメントと組み合わせて経済的に成立する設計

### リスク・懸念点

- **オンチェーン・コンポーザビリティの不足**: スマートコントラクトがバリデーション結果をオンチェーンで読み取れない設計のため、DeFi 連携が制限される
- **評判集計の中央集権化リスク**: 単一の集計スコア事業者が市場支配力を持つ恐れ
- **決済・エスクロー機能の欠如**: 標準化はアプリケーション層に委ねられており、フラグメンテーションが起きる可能性
- **Draft ステータス**: 仕様変更のリスクがあり、現時点での本番採用には慎重さが必要

---

## 我々への示唆

- いま検討すべきこと：
  - x402 との組み合わせを前提に「信頼レイヤーとして ERC-8004 をどう評価するか」を整理する
  - エージェント向けサービスを提供する場合、Identity Registry への自動登録フローの設計を検討する
- 後で深掘りすべきこと：
  - Validation Registry と KYC/AML ソリューション（chainalysis 等）の接続可能性
  - ERC-8028 との連携によるエージェント経済のトークンモデル
  - zkML・TEE を使った検証コストの実測
- 今は優先度が低いこと：
  - Draft 段階であり、仕様確定前の大規模な実装投資

---

## 未解決の論点

- エージェントの法的主体性問題：ERC-8004 の Identity は法的な契約主体として認められるか
- Reputation Registry の評判操作耐性：シビル攻撃への対策が仕様に含まれていない
- オフチェーン集計の標準化：誰が集計するかで中立性が損なわれる可能性

---

## 参考リンク

- 公式ドキュメント: https://eips.ethereum.org/EIPS/eip-8004
- 仕様書 / GitHub: https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098
- 補足情報:
  - https://www.chainup.com/blog/x402-erc8004-ai-agent-payments-agentic-web/
  - https://learn.backpack.exchange/articles/erc-8004-explained
  - https://www.payram.com/blog/mcp-a2a-ap2-acp-x402-erc-8004
  - https://lazai.network/blog/the-two-layers-of-decentralized-ai-agent-operations-8004-and-asset-economics-8028

---

## 重要度

- **High** — エージェント経済の信頼インフラとして x402 との組み合わせが注目されており、ステーブルコイン決済スタックの重要な構成要素になり得る

## 確からしさ

- **Medium** — Draft ステータスであり仕様変更の余地がある。メインネットデプロイは確認済みだが採用事例は初期段階
