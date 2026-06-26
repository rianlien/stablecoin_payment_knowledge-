# 設計思想: Intent → Contract → Mechanism

この vault がどういう原理で組み立てられているかを定義する内部ドキュメント。
ここは公開サイト（MkDocs）には載せない統治用ドキュメントであり、運用ルールの「なぜ」を保持する。
日々の実務ルール（何をどう書くか）は [`CLAUDE.md`](../CLAUDE.md) に、配線図は [`ARCHITECTURE.md`](ARCHITECTURE.md) にある。

---

## 1. 三層の定義

| 層 | 問い | 誰のためか | 性質 |
| --- | --- | --- | --- |
| **Intent** | なぜ作るか（目的 / 意図的制約） | 人間が与える北極星 | 再生成できない唯一の資産 |
| **Contract** | 何を満たすか（外部から見た要件・境界） | Intent を実現する約束 | 安定。変えるときは意図的に |
| **Mechanism** | どう実現するか（実装・手段・都合） | Contract を満たす道具 | 変化が多い。差し替え可能 |

流れは **Intent → Contract → Mechanism の一方向**。上流が下流を規定する。

### 非対称ルール（最重要）

**Mechanism（実装・都合）が Contract や Intent を黙って書き換えてはいけない。**

- 実装の都合で何かを変えたくなったら、まず上流（Contract / Intent）を更新し、その後で Mechanism を直す。順番を逆にしない。
- Intent は再生成できない。コードやスクリプトはいつでも作り直せるが、「なぜそれを集めるのか」「どう解釈するのか」という視座は失うと復元できない。だから最優先で保護する。

---

## 2. この vault への翻訳

この vault は性質の異なる **2 つの層** を内包する。思想は両方に再帰的に適用される。

### OS 層（ノートを生産する自動化ソフト）

| 層 | vault 上の場所 | 役割 |
| --- | --- | --- |
| Intent | この `PHILOSOPHY.md` ＋ `CLAUDE.md` の「Intent — 目的と意図的制約」節 | なぜ集めるか / 何を捨てるか |
| Contract | `CLAUDE.md` の「Contract」節 ＋ `90_Templates/` | ノート・出力・リンクが満たすべき形と境界 |
| Mechanism | `.claude/{skills,prompts,hooks}` / `mkdocs.yml` / `.github/workflows/` | どう実現するか |

### コンテンツ層（知識本体）

| 層 | vault 上の場所 | 役割 |
| --- | --- | --- |
| Intent | `03_Topics` / `05_MOCs` の「問題の本質・論点枠組み」、各ノートの「我々への示唆」 | 我々の視座＝再生成できない資産 |
| Contract | frontmatter スキーマ ＋「事実と解釈の分離 / 出典必須 / 重要度≠確からしさ」 | 各ノートが満たす約束 |
| Mechanism | `00_Inbox` の事実本文、ノート間のリンク網 | 再収集可能な素材 |

---

## 3. 非対称ルールの具体化

### OS 層

- スクリプト（Mechanism）の都合を最上位ルール（Contract / Intent）に直書きしない。必要なら **抽象化して Contract に昇格**させ、具体理由は Mechanism 側（`ARCHITECTURE.md` や各スクリプト）に置く。
  - 例: 「Daily Brief のリンクは `[Source（YYYY-MM-DD）](URL)` 形式」は **出力 Contract**（外から見たノートの約束）。その理由「Slack 投稿スクリプトが裸 URL を認識しないから」は Mechanism 側に置く。Contract を読む人が Slack の実装を知らなくても従える状態にする。
- ルールを変えるときの順番: **Intent / Contract を更新 → 然る後に skill / prompt / hook を直す。**

### コンテンツ層

- 新しい事実（`00_Inbox` ＝ Mechanism）が、既存の枠組み（`03_Topics` / `05_MOCs` ＝ Intent）と矛盾しても、**枠組みを黙って上書きしない**。矛盾は surface する（明示して残す）。
  - これは親ワークスペースの `CLAUDE.md`「Surface conflicts, do not average them」と一致する。
- `03_Topics` / `05_MOCs` は **保護資産**。事実は再収集できるが、論点の立て方・比較の枠組み・我々の解釈は失うと復元しにくい。

---

## 4. トレーサビリティ（来歴）

各層は前の層に紐付き、来歴をたどれる。dg402 ではタグマーカー（`<rfp raw-rfps="...">` 等）で表現していたが、この vault では既存の仕組みを来歴チェーンとして再定義する。

```
raw（一次情報）          news note（事実）         synthesis（解釈・枠組み）
source_url          →   /00_Inbox/*.md       →   /03_Topics, /05_MOCs
3 つの日付で来歴を保持        type: news               type: topic / moc
                          ↑ 上向きに「根拠ノート」セクションでたどれる
```

- **下向き**: Topic / MOC は「根拠ノート」を列挙し、どの Inbox ノートに支えられているかを示す（既存の "Inbox との紐付け" / "リンク一覧テーブル" を形式化したもの）。
- **上向き**: news note は `source_url` と 3 つの日付（`article_published_date` / `underlying_event_date` / `primary_source_date`）で一次情報まで遡れる。
- 層はディレクトリ位置と frontmatter で識別する（概念ページは `type:`、news は `category` / `primary_category`）。**新しい層フィールドは発明しない。**

---

## 5. フラクタル配置

Intent → Contract → Mechanism はあらゆる抽象度で再帰する。ディレクトリも同じ:

- **ルートに近いほど安定・抽象**（`05_MOCs` / `03_Topics` / `CLAUDE.md`）。
- **末端ほど具体・変化が多い**（`00_Inbox` の個別ニュース）。

各主要ディレクトリの `index.md` 冒頭に短い「層宣言」（この場所の層 / 安定度 / してはいけないこと）を置く。dg402 のように各サブディレクトリへ `docs/CODEMAP` を物理再帰させるのではなく、**既存の `index.md` を使った軽量な翻訳版**とする。

---

## 6. dg402 との対応と、移植しない判断

| dg402（ソフトウェアレポ） | この vault での対応 |
| --- | --- |
| `docs/raw-rfp` → `rfp` | `source_url`（一次情報）＋ news note の summary |
| `docs/requirements` | `CLAUDE.md` Contract 節 ＋ `90_Templates/` |
| `docs/internal-design`（コードから読めない intent を補完） | `03_Topics` / `05_MOCs` の論点枠組み、各ノートの「我々への示唆」 |
| タグマーカー `<rfp raw-rfps="...">` | 3 つの日付 ＋ 「根拠ノート」セクション ＋ frontmatter（`type:` / `category`） |
| 各パッケージ配下の `docs/CODEMAP` | 各 `index.md` の層宣言（軽量翻訳版） |

**物理構造（`raw-rfp/` 等の新設）は移植しない。** 理由:

- この vault は software ではなく知識ベースで、既に `type:` / 3 日付 / MOC / index.md という形で思想を部分的に体現している。
- 親ワークスペース `CLAUDE.md` の「Simplicity before structure」に従い、新しい階層を増やすより既存構造を層として**再定義**するほうが理解・運用コストが低い。

---

## 7. 実務チェックリスト

何かを変更するとき、以下を自問する:

1. **層の判定**: 自分が触っているのは Intent / Contract / Mechanism のどれか。
2. **方向**: Mechanism の都合で上流（Contract / Intent）を黙って書き換えていないか。逆順になっていないか。
3. **昇格 or 委譲**: スクリプト固有の都合が Contract に漏れていないか。漏れているなら抽象化して昇格し、理由は Mechanism 側へ。
4. **来歴**: 新しい解釈（Topic / MOC）に根拠ノートが紐付いているか。新しい事実が枠組みと矛盾するなら surface したか。
5. **安定度**: ルートに近い安定層を、末端の都合で頻繁に揺らしていないか。

関連: [`CLAUDE.md`](../CLAUDE.md)（実務ルール本体） / [`ARCHITECTURE.md`](ARCHITECTURE.md)（配線図・CODEMAP）
