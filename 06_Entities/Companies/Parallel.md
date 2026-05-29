---
title: "Parallel"
type: company
updated: 2026-05-29
category: agent-infrastructure
tags:
  - agentic-commerce
  - agent-payments
  - api-billing
  - machine-payments
  - x402
  - company
aliases:
  - Parallel Web Systems
  - Index by Parallel
---

# Parallel

Parallel Web Systems は、AIエージェントが情報にアクセスするためのウェブAPIインフラを提供する企業。「エージェントはいずれ人間よりも1000倍ウェブを使うようになる」という前提のもと、エージェントビルダーが情報インフラを自前で構築せずに済む基盤を目指している。

CEO は Parag Agrawal（Twitter在籍11年、元CEO）。

---

## 現状の要約

### 何をしているか

- **エージェント向けウェブAPI**: Deep Research API / Search API / Task API を per-query で提供。HTMLのパース・クリーニング・出典追跡・クロスリファレンス検証を代行する。
- **Index**: コンテンツオーナーへの貢献度ベース補償プラットフォーム。AIエージェントがコンテンツを使ってタスクを完了した際の「実質的な貢献度（Shapley value）」に応じて対価を支払う。
- **一次データへのアクセス**: PitchBook、ZoomInfo、Enigma、RocketReach などIndexパートナーの一次データをAPIに含め、汎用クロールとの差別化を図る。

### 見立て

Indexの本質はコンテンツオーナーへの慈善ではなく、**APIのコンテンツ品質・独自性を変動コストで確保する調達戦略**。ライセンス料の一括契約ではなく、使った分だけ払う構造にすることで、パブリッシャーを囲い込みながらコストを収益に連動させている。

ただのウェブwrapper（SerpAPI、Brave Search API等）と異なるのは、処理済み・出典追跡済みの情報を返す点。「検索結果を返す」より「リサーチを代行する」に近いポジション。

---

## 主要レイヤー

| レイヤー | 内容 | 意味 |
|---|---|---|
| Deep Research API | 複雑な多段階調査タスクを代行 | 法務・金融・営業インテリジェンス用途 |
| Search API | エージェント向けウェブ検索 | RAGのリトリーバル層を置き換える |
| Task API | データ充実化・データセット構築 | バックグラウンドエージェントの定常処理 |
| Index | コンテンツオーナーへの分配 | コンテンツ調達コストのレベニューシェア化 |

---

## Indexの補償モデル

**Shapley value方式**（ゲーム理論）

```
あるソースの報酬
= 「そのソースあり」と「そのソースなし」での
  タスク完了品質の差分の平均（全組み合わせで推定）
```

- クロール回数・引用回数ではなく「タスクへの実質的な貢献度」で測る
- ニッチ専門コンテンツは代替困難 → 大手媒体の汎用記事より高評価になりうる
- **ただし計算はParallel内部のブラックボックス**。Parallelが測定者かつ支払者であり、独立検証不可。

**ローンチパートナー（2026年5月時点）**

| カテゴリ | 参加者 |
|---|---|
| パブリッシャー | The Atlantic, Fortune Media, PR Newswire |
| データプロバイダー | PitchBook, ZoomInfo, Enigma, RocketReach, Tracxn, Fiscal AI |
| 独立系クリエイター | Every, Not Boring, The Generalist, Exponential View |

---

## API利用課金：x402 / MPP

Parallel の API は **HTTP 402 Payment Required** を使ったリアルタイム機械決済に対応している。2つの支払いレールが存在する。

| レール | プロトコル | 通貨 | CLIツール | 状態 |
|---|---|---|---|---|
| MPP / Tempo | Machine Payments Protocol | pathUSD | `mppx` | 稼働中 |
| x402 / Base | x402 | USDC on Base | `purl`（Stripe製） | 設定次第で有効化 |

**支払いフロー（エージェント視点）**

```
エージェントが /api/search などを叩く
    ↓
Parallel MPPゲートウェイが 402 Payment Required を返す
    ↓
mppx / purl が自動で署名・支払い処理
    ↓
再リクエスト → APIがデータを返す
```

**価格（2026年5月時点）**

| エンドポイント | 価格 |
|---|---|
| POST /api/search | $0.01/query |
| POST /api/extract | $0.01/URL |
| POST /api/task | $0.10〜$0.30 |

---

## お金の流れ（2層構造）

**Layer 1: API利用課金（x402 / MPP）**
```
エージェント
    ↓ per-queryでリアルタイム支払い（USDC / pathUSD）
  Parallel MPPゲートウェイ
```

**Layer 2: Indexによるコンテンツオーナーへの分配**
```
Parallel
    ↓ 収益の一部をShapley valueで再分配
コンテンツオーナー（Indexパートナー）
```

- エージェントがコンテンツオーナーに直接払うわけではない（Layer 2はParallel経由）
- Layer 1（x402/MPP）とLayer 2（Index分配）は別レイヤー
- 分配率・実際の支払い額は非公開

---

## 調達状況

| ラウンド | 金額 | 主要投資家 | バリュエーション |
|---|---|---|---|
| シリーズA | $100M | Index Ventures + Kleiner Perkins | 非公開 |
| シリーズB | $100M | Sequoia Capital | $2B |

---

## 不確実性・監視ポイント

- **透明性**: Shapley計算の独立検証手段なし。規模拡大時に分配率を下げる誘因がある
- **競合**: Perplexity、Google、OpenAI も同方向（パブリッシャー提携 + 処理済み情報API）に動いており、差別化は不安定
- **外部エージェント開放**: Parallel外部のエージェントビルダーにIndexを開放する意図はあるが、具体的な仕組みは未公開
- **実利用者の評価**: Harvey、Notion、Clay、Sourcegraph、Opendoor が導入しているが、パフォーマンス・コスト感の公開データはない

---

## Agentic commerceとの関連

Parallelは [[MOC_agent-payments-stack]] の文脈で2つの側面を持つ。

**x402 / MPP の実装事例として**
- API利用課金レイヤーで x402（USDC on Base）と MPP（pathUSD on Tempo）を実運用している
- エージェントが HTTP 402 チャレンジに自律的に応答して支払いを完了するフローは、x402が目指す機械決済の具体的な実装例
- `purl`（Stripe製）との統合は、Stripe の MPP / x402 エコシステムとの接続を示している

**Indexの補償モデルとして**
- コンテンツ消費の対価分配は Parallel が中央集権的に管理しており、x402的な「エンドツーエンドの自律決済」とは異なる
- ただし「エージェントのコンテンツ消費に対価が発生する」という経済モデルの実証例として注目に値する
