---
title: "ERC-8183: Agentic Commerce — AIエージェント間エスクロー・決済標準"
date: 2026-04-24
source: Ethereum EIPs / Ethereum Magicians
source_url: https://eips.ethereum.org/EIPS/eip-8183
entity: Ethereum Foundation dAIチーム / Virtuals Protocol
category: protocol
tags:
  - erc
  - agentic-commerce
  - protocol
  - stablecoin
  - x402
summary: >
  AIエージェント同士が中央集権的プラットフォームや人間の仲裁なしに、
  ジョブを委託・受注・決済できるオンチェーン・エスクロー標準。
  Ethereum Foundation dAIチームと Virtuals Protocol が共同提案。
  x402（決済実行）・ERC-8004（信頼確立）と組み合わせ、
  エージェント経済の取引レイヤーを担う。
status: draft
---

## 概要

- **プロトコル名**: ERC-8183（Agentic Commerce）
- **開発主体**: Davide Crapis（Ethereum Foundation Head of AI）、Bryan Lim・Tay Weixiong・Chooi Zuhwa（Virtuals Protocol）
- **対象ユースケース**: AIエージェント間の自律的なジョブ委託・成果物評価・ステーブルコイン決済
- **対応チェーン / ネットワーク**: Ethereum + EVM互換チェーン（Base・BNB Chain・Arc testnet等で稼働確認済み）
- **ライセンス**: ERC（オープン標準）

---

## 何を解決するプロトコルか

### 課題

AIエージェント同士が仕事を発注・受注・決済する際、以下が欠如していた：

- **信頼できるエスクロー**: 成果物を受け取る前に資金を安全に預ける共通仕組みがない
- **評価者の標準化**: 成果物の完了・拒否を判定する主体の役割が定義されていない
- **オンチェーン合意**: 人間の仲裁や中央集権プラットフォームへの依存なしに取引を完結できない

### アプローチ

「資金を預けておき、仕事完了が証明されてから支払う」エスクロー＋評価者アテステーションの仕組みをオンチェーンで標準化する。Virtuals Protocol が内部向けに構築した Agentic Commerce Protocol（ACP）が 3,400以上のエージェント・$3M超の取引処理実績を経て、Ethereum Foundation とともにオープン標準化したもの。

---

## 技術仕様

### アーキテクチャ

6状態のステートマシンで1つのジョブライフサイクルを管理する。データの多くはオフチェーン（IPFS等）に保持し、オンチェーンはステート遷移・エスクロー管理・アテステーションのみを担う。

### ステートマシン（6状態）

| 状態 | 許可されるアクション |
|------|-------------------|
| Open | クライアントが資金投入または拒否。プロバイダーが予算提案 |
| Funded | プロバイダーが成果物を提出（→ Submitted）。評価者が拒否可能。期限後は払い戻し |
| Submitted | 評価者のみが完了または拒否を実行可能 |
| Completed | 終端状態。報酬がプロバイダーへ（手数料控除後） |
| Rejected | 終端状態。エスクローがクライアントへ返還 |
| Expired | 終端状態。Rejectedと同様に期限後返還 |

### 主要コンポーネント

**3つの役割**:
- **Client**: ジョブを作成し、バジェットを設定し、エスクローに資金を入れる
- **Provider**: 成果物（bytes32コンテンツハッシュ）を提出し、Funded → Submitted へ遷移させる
- **Evaluator**: Submitted ジョブのみ完了/拒否を実行できる唯一の権限者。AIエージェント・ZKプルーフ・マルチシグウォレット・クライアント自身も担当可能

**コア関数**:
- `createJob(...)` — Client: Open ジョブを初期化
- `setBudget(jobId, amount)` — Client または Provider: 価格合意
- `fund(jobId, expectedBudget)` — Client: エスクロー資金投入 → Funded
- `submit(jobId, deliverable)` — Provider: 成果物ハッシュ提出 → Submitted
- `complete(jobId, reason)` — Evaluator のみ: 終端・報酬解放
- `reject(jobId, reason)` — Client（Open時）/ Evaluator（Funded/Submitted時）
- `claimRefund(jobId)` — Anyone: 期限後の返還（フック不可の安全パス）

**オプショナルフック（IACPHook）**:
- `beforeAction` / `afterAction` コールバックで6つの関数に拡張ロジックを挿入可能
- 評判チェック・SLA検証・ERC-8004連携などをコアロジックを変更せずに実装
- `claimRefund` は意図的にフック不可にして悪意あるフックによる返還ブロックを防止

**手数料構造**: プラットフォーム手数料＋評価者手数料をベーシスポイントで設定可能。完了ジョブからのみ控除（返還時は控除なし）。上限10,000bp。

### API / インターフェース

ERC標準インターフェースとして定義。リファレンス実装 `AgenticCommerce.sol` は OpenZeppelin パターン・UUPSプロキシによるアップグレード可能な設計。ERC-2771（メタトランザクション）と ERC-2612（permit）を任意でサポートし、ガスレス実行が可能。

### 対応通貨・アセット

単一の ERC-20 トークンを 1 コントラクトインスタンスとして扱う。USDC・DAI 等を同時に受け付ける場合は通貨ごとに別コントラクトが必要。

---

## エコシステム・採用状況

### 主要参加者・パートナー

- **Ethereum Foundation dAIチーム**: Davide Crapis が主導。ERC-8004・ERC-8028・ERC-8183 を含む dAI スタック全体を推進
- **Virtuals Protocol**: 共同提案者。内部 ACP 実装で 3,400以上のエージェントが稼働、$3M超の取引処理実績
- **Arc（Circle関連）**: testnet で ERC-8183 + USDC + Circle Wallets の統合スタックを提供
- **BNB Chain / BNBAgent SDK**: EIP ファイナライズ前に最初のライブ実装を出荷
- **UFX Agentic Commerce**: Base Mainnet で評判・SLA フック付きデプロイ
- **ThoughtProof**: マルチモデル評価者（コンセンサス必須）、Base Mainnet 稼働
- **Taskmarket.daydreams.systems**: 2025年中頃から本番稼働

### 実採用事例

- 2026年2月25日 EIP PR 提出、2026年3月10日 Draft マージ
- Sepolia テストネット・Base Mainnet・Arc testnet・BNB Chain 等で稼働確認
- Arc testnet: `ERC_8183=0x0747EEf0706327138c69792bF28Cd525089e4583`（USDC 利用）

### 競合・類似プロトコル

| プロトコル | 違い |
|-----------|------|
| OpenAI Agent Commerce Protocol | 2026年2月ローンチ。APIモデルで中央集権プラットフォームに依存 |
| Google Universal Checkout Protocol | 2026年1月ローンチ。同様に中央集権的 |
| Alkahest | 組成可能なアービタと EAS（Ethereum Attestation Service）を使用した既存監査済みエスクロー。より成熟 |
| Task Market Protocol（beau） | より広い agentic commerce カバレッジを主張する代替提案 |

---

## dAI スタックにおける位置づけ

ERC-8183 は Ethereum Foundation dAI チームが推進するスタックの「取引レイヤー」を担う：

| 標準 | 役割 |
|------|------|
| **x402** | HTTP決済プロトコル。API呼び出し単位のマイクロペイメント（「どう支払うか」） |
| **ERC-8004** | AIエージェントの ID・評判レジストリ（「誰が相手か・信頼できるか」） |
| **ERC-8183** | ジョブベースのエスクロー＋評価者アテステーション（「どう合意して取引するか」） |
| **ERC-8028** | Data-Anchored Token（AIアセットのトークン化と使用権・収益分配） |

x402 が支払いを実行 → ERC-8183 がジョブ合意・エスクロー管理 → 完了後に ERC-8004 へ評判データをフィードバックする「発見→取引→評判の好循環」が設計思想の核。

---

## 決済事業者・PSP としての評価

### 統合のしやすさ

- ERC-2771 によるガスレス実行が可能で、ユーザーがガスを意識しない UX を構築できる
- 単一 ERC-20 トークンのみ対応のため、複数通貨を扱う PSP は通貨ごとのコントラクト管理が必要
- フック機能により既存の KYC・コンプライアンスフローを埋め込み可能
- Draft ステータスのため API 変更リスクがあり、本番統合は仕様確定後が望ましい

### コンプライアンス対応

- KYC/AML への直接対応は仕様スコープ外
- Validation Registry（ERC-8004）と組み合わせた評価者フックで Chainalysis 等の KYT ソリューションを接続する拡張は理論的に可能
- 規制上の責任主体（Client・Provider・Evaluator のどれが法的義務を負うか）は未整理

### スケーラビリティ・コスト

- L2（Base・BNB Chain 等）での稼働実績あり
- ガスコストはステート遷移ごとに発生。マイクロ取引にはオフチェーン台帳＋オンチェーンエスクロー（ハイブリッド）が推奨
- x402 の $0.001 以下のマイクロペイメントと組み合わせて経済的に成立する設計

### リスク・懸念点

- **評価者の信頼問題（最大リスク）**: 悪意ある・低品質な評価者への対処機能がなく「評価者を誰が評価するか」が本質的課題
- **主観的タスクの評価困難**: デザイン・文章作成など客観的検証が難しいタスクへの適用は複雑
- **Draft ステータスのマイグレーションリスク**: 関数シグネチャ・ステートマシンがファイナライズ前に変更される可能性
- **競合標準の並立**: 中央集権的プロトコルを含む複数標準が並存しており、エコシステムが分裂するリスク
- **規制不確実性**: 自律 AI コマースの法的責任・課税・消費者保護が未整理

---

## 我々への示唆

- いま検討すべきこと：
  - x402・ERC-8004・ERC-8183 を「決済実行→信頼確立→エスクロー決済」の三層スタックとして整理し、どの層から評価・実証実験を始めるか方針を決める
  - Arc testnet（USDC + ERC-8183 統合）の動向を追い、ステーブルコイン PSP としての参入機会を評価する
- 後で深掘りすべきこと：
  - Evaluator フックと KYT ソリューションの接続可能性
  - UFX・ThoughtProof の Base Mainnet 実装の詳細調査（フック設計・評判モデル）
  - ERC-8028 との連携によるエージェント向けデータ・モデルの収益分配モデル
- 今は優先度が低いこと：
  - Draft 段階であり、仕様確定前の大規模な実装投資

---

## 未解決の論点

- **評価者の責任モデル**: 評価者が不正・低品質な判定を行った場合のディスピュート解決手段が仕様にない
- **主観的タスクの評価基準**: ZKプルーフや TEE オラクルが使えない創作系タスクをどう評価するか
- **連鎖ジョブの標準化**: 複数エージェントが順番に作業する連鎖ジョブを第一級プリミティブとして標準化すべきか
- **Sybil 攻撃耐性**: 評判蓄積後のシビル攻撃対策が仕様に含まれていない
- **「Agentic」命名の妥当性**: 技術的には汎用エスクローであり「Escrow」への改名を求める声もある（Ethereum Magicians より）

---

## 参考リンク

- 公式ドキュメント: https://eips.ethereum.org/EIPS/eip-8183
- 仕様書 / Ethereum Magicians: https://ethereum-magicians.org/t/erc-8183-agentic-commerce/27902
- 本番実装知見スレッド: https://ethereum-magicians.org/t/accidentally-built-erc-8183-lessons-from-running-an-ai-agent-job-market-in-production/27970
- 補足情報:
  - https://www.arc.network/blog/running-an-agentic-economic-flow-on-arc-with-erc-8183
  - https://blog.quicknode.com/erc-8183-agentic-commerce/
  - https://www.dwellir.com/blog/erc-8183-agentic-commerce-explained
  - https://phemex.com/academy/erc-8183-ai-agents-crypto
  - https://www.kucoin.com/news/flash/ethereum-foundation-and-virtuals-protocol-launch-erc-8183-to-enable-trustless-ai-agent-transactions

---

## 関連ノート

- [[ERC-8004_Trustless-Agents]] — 信頼・評判レイヤー（ERC-8183 の評価者フックと連携）
- [[2026-04-02_x402-Foundation_linux-foundation-launch]] — 決済実行レイヤー（ERC-8183 と補完関係）

---

## 重要度

- **High** — Ethereum Foundation 公認の dAI スタック中核構成要素。複数の本番事例あり。ステーブルコイン（USDC）によるエージェント間取引の標準インフラとなり得る

## 確からしさ

- **Medium-High** — Draft ステータスで仕様変更リスクはあるが、Base Mainnet・BNB Chain 等で稼働実績あり。Ethereum Foundation + Virtuals Protocol の共同提案で信頼性は高い
