---
title: "GENIUS Act（Guiding and Establishing National Innovation for U.S. Stablecoins Act）"
type: topic
updated: 2026-06-15
tags:
  - regulation
  - stablecoin
  - PPSI
  - AML
  - payments
---

# GENIUS Act

米国初の包括的ステーブルコイン規制法。2025 年 7 月 18 日に大統領署名により成立し、許可済み決済ステーブルコイン発行者（Permitted Payment Stablecoin Issuers、PPSI）の認可要件・準備資産基準・AML/CFT 義務・州制度認定プロセスを定める。CLARITY Act（市場構造法）と並ぶ米国デジタル資産規制の二本柱の一つであり、エージェント決済・x402 等で利用される USDC・RLUSD・PYUSD の発行継続の法的根拠を規定する。

---

## 全体像

### 法案の構造

GENIUS Act は単独の法律文書だが、実施規則の策定は OCC・FDIC・FinCEN・OFAC・財務省の複数機関が独立した NPRM を並行して進める形をとる。2025 年 7 月の成立から 1 年以内（2026 年 7 月 18 日）に最終規則を発行する法的義務が各規制機関に課されている。

**PPSI の二つのルート**

| ルート | 監督機関 | 対象 |
|---|---|---|
| 連邦ルート（PPSI） | OCC または FDIC | 国法銀行・連邦セービング・FDIC 監督機関の子会社、および非銀行 PPSI |
| 州認定ルート | 各州規制機関（例：NYDFS） | 発行残高 100 億ドル未満の発行体（財務省が「実質的に類似」と認定した州制度） |

### 主要 NPRM の進行状況

| NPRM | 発行機関 | コメント期限 | ステータス |
|---|---|---|---|
| OCC 実施規則（国法銀行・連邦適格 PPSI） | OCC | 2026-05-01（終了） | 最終規則化フェーズ |
| FDIC 申請手続き（IDI 子会社） | FDIC | 2026-05-18（終了） | 最終規則化フェーズ |
| 財務省・州制度認定原則 | Treasury | 2026-06-02（終了） | 最終規則化フェーズ |
| FDIC 実体基準（FDIC 監督 PPSI・IDI） | FDIC | 2026-06-09（終了） | 最終規則化フェーズ |
| FinCEN・OFAC 共同 AML/CFT 規則 | FinCEN / OFAC | 2026-06-09（終了） | 最終規則化フェーズ |

### 重要スケジュール

- **2026-07-18**：最終規則の法定発行デッドライン
- **GENIUS Act 発効日**：最終規則公告後 120 日後、または 2027-01-18 のいずれか早い日

---

## 主要ノート

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-04-03 | [[2026-04-03_Treasury_genius-act-state-regime-nprm]] | 財務省が州規制「実質的に類似」判断基準 NPRM を公表。統一要件と州裁量要件に分類。$10B 閾値を規定 |
| 2026-04-10 | [[2026-04-10_FinCEN-OFAC_genius-act-aml-nprm]] | FinCEN・OFAC 共同で PPSI 向け AML/CFT・制裁コンプライアンス NPRM を公表 |
| 2026-04-22 | [[2026-04-22_GENIUS-Act_banks-seek-delay]] | ABA ほか 4 銀行業界団体がコメント期間延長を要請。法定 7 月デッドラインへの黄信号 |
| 2026-05-01 | [[2026-05-01_OCC_genius-act-nprm-comments]] | OCC NPRM コメント期間終了。Circle・AICPA・SIFMA 等が意見書提出 |
| 2026-05-15 | [[2026-05-15_NCUA_genius-act-nprm-credit-union-stablecoin]] | NCUA の信用組合向けステーブルコイン取扱い NPRM |
| 2026-06-03 | [[2026-06-03_Fiserv_fiusd-bank-stablecoin-genius-act]] | Fiserv が GENIUS Act を見越した銀行向けステーブルコイン（FiUSD）を発表 |
| 2026-06-09 | [[2026-06-09_GENIUS-Act_nprm-comment-deadline-fdic-fincen]] | FDIC・FinCEN/OFAC の NPRM コメント期間終了。全 NPRM が最終規則化フェーズへ移行 |
| 2026-06-09 | [[2026-06-09_NYDFS_genius-act-stablecoin-alignment]] | NYDFS が GENIUS Act 準拠の州規制案を発表。Circle USDC の州ライセンス継続への道筋 |

---

## 現状の論点

- **7/18 法定デッドラインの遵守可否**：5 機関が独立した最終規則化を並行して進める。ABA の延長要求は却下されたが、過去の規制スケジュール超過事例から遅延リスクは 20〜30% と推定される
- **州 vs 連邦ルートの選択**：Circle が OCC 連邦チャーター（条件付き承認済み）と NYDFS 州ライセンスのどちらを本命にするかが未決定。NYDFS が 6/9 に GENIUS Act 準拠案を発表し、Circle は NY 州ルートのみで USDC 発行継続できる可能性が出てきた
- **エージェント取引への AML 適用**：FinCEN/OFAC 最終規則で「エージェントが開始するマイクロペイメント」に de minimis 閾値や KYA（Know Your Agent）の具体的な扱いが設けられるかどうかが x402・CPN の実用性に直結する
- **$10B 閾値のロビー圧力**：大規模発行体（Circle の USDC は数十 B ドル規模）への連邦移行強制の例外申請スキームが、最終規則でどう設計されるかが業界再編に影響する
- **AICPA 基準の採用有無**：OCC が毎月の準備金証明審査・年次統制審査・CPA 独立審査の義務化要件として AICPA 提案基準を採用するかがコンプライアンスコストを大きく左右する

---

## 監視ポイント

- **2026-07-18**：OCC・FDIC・FinCEN・OFAC・財務省の最終規則公告——法定デッドライン遵守の有無
- **NYDFS プレコメント期間**（〜2026-06-19）：業界コメント内容、特に Circle・Paxos の立場
- **Treasury の「実質的同等性」認定申請プロセス**：州制度認定 NPRM の最終化後、NYDFS 等が認定申請を行う具体的スケジュール
- **Circle の公式発表**：OCC 連邦チャーター vs NYDFS 州ルートの最終選択
- **GENIUS Act 発効日確定**：最終規則公告タイミング次第で 2026-11 月台か 2027-01-18 か
- **他州の追随動向**：CA・TX・WY 等での GENIUS Act 準拠州規制案の発表

---

## 関連ページ

- [[CLARITY-Act]]
- [[MOC_Regulation]]

---

## 参考リンク

- [Federal Register：財務省 State Regime NPRM（2026-04-03）](https://www.federalregister.gov/documents/2026/04/03/2026-06489/genius-act-broad-based-principles-for-determining-whether-a-state-level-regulatory-regime-is)
- [Federal Register：FinCEN/OFAC AML NPRM（2026-04-10）](https://www.federalregister.gov/documents/2026/04/10/2026-06963/permitted-payment-stablecoin-issuer-anti-money-launderingcountering-the-financing-of-terrorism)
- [Federal Register：FDIC NPRM（2026-04-10）](https://www.federalregister.gov/documents/2026/04/10/2026-06974/genius-act-requirements-and-standards-for-fdic-supervised-permitted-payment-stablecoin-issuers-and)
- [OCC GENIUS Act 実施規則 NPRM（2026-03-02）](https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-3.html)
- [Paradigm GENIUS Act Rulemaking Tracker](https://paradigm.xyz/genius)
- [Chapman & Cutler GENIUS Act Rulemaking Tracker](https://www.chapman.com/publication-genius-act-rulemaking-tracker)
