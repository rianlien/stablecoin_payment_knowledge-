---
title: FinCEN・OFAC、GENIUS Act に基づくステーブルコイン発行者向け AML/制裁コンプライアンス規則案を公表
date: 2026-04-10
source: U.S. Department of the Treasury（公式プレスリリース）
source_url: https://home.treasury.gov/news/press-releases/sb0435
category: regulation
tags:
  - regulation
  - kyt
  - stablecoin
  - payments
summary: 財務省の FinCEN と OFAC が共同で、GENIUS Act に基づく許可済み決済ステーブルコイン発行者（PPSI）向けの AML/CFT・制裁コンプライアンスプログラム要件の規則案（NPRM）を連邦官報に掲載。コメント期限は 2026 年 6 月 9 日。
implications: >
  ステーブルコイン発行者に対して銀行秘密法（BSA）に類似したリスクベース AML プログラムの義務化が明確化された。PPSI はトランザクションブロッキング機能付き制裁コンプライアンスプログラムが必要になる。PSP・PayFac として PPSI と連携する場合も、そのコンプライアンス体制の確認が必要となる。
follow_up: コメント期限（6月9日）後の最終規則化スケジュール、FDIC 規則との整合性
---

## Summary

2026 年 4 月 10 日、米財務省の金融犯罪取締ネットワーク（FinCEN）と外国資産管理局（OFAC）は、GENIUS Act に基づく許可済み決済ステーブルコイン発行者（Permitted Payment Stablecoin Issuers、PPSI）向けの AML/CFT および制裁コンプライアンスプログラム要件を規定する規則案を公表した。同案は連邦官報（Federal Register）に掲載され、コメント募集期間は 2026 年 6 月 9 日まで。FDIC が同日に別途公表した GENIUS Act 実施規則案（発行基準・資本要件等）と合わせて、米国ステーブルコイン規制の主要骨格が出揃った形となる。

## Facts

- 発表日：2026 年 4 月 10 日（連邦官報掲載日）
- 発表機関：FinCEN（金融犯罪取締ネットワーク）＋ OFAC（外国資産管理局）、共同 NPRM
- 対象：GENIUS Act に基づく PPSI（許可済み決済ステーブルコイン発行者）
- 主な要件：
  - リスクベース AML/CFT プログラムの策定・維持（BSA 準拠機関に類似、ただし同一ではない）
  - トランザクションブロッキング機能を含む実効的な制裁コンプライアンスプログラムの維持
- FDIC は同日、PPSI の資本要件・償還要件（2 営業日以内）等を規定する別途 NPRM を公表
- コメント期限：2026 年 6 月 9 日

## Implications

- **コンプライアンス要件の具体化**：PPSI は既存の銀行・MSB に課されるものと同等レベルの AML 体制構築が求められる。FinCEN への SAR 提出・顧客確認（CDD）・制裁スクリーニングが義務となる見込み。
- **PSP・PayFac への影響**：PPSI と連携してステーブルコイン決済を提供する PSP は、PPSI のコンプライアンス体制の十分性を確認するデューデリジェンスが必要になる。
- **KYT（Know Your Transaction）の重要性増大**：制裁コンプライアンスプログラムにトランザクションブロッキング機能が必須とされており、オンチェーン KYT ツール（Chainalysis 等）の採用が実質的に不可欠となる。
- **規則確定後の移行期間**：FDIC 規則では承認後 180 日以内に AML 認定書の提出が求められており、最終規則化後の準備期間は限られる。

## Open Questions

- 最終規則化のタイムラインは？（コメント期限 6 月 9 日以降、いつ最終規則が施行されるか）
- 外国ステーブルコイン発行者（Tether 等）への適用範囲は？
- PPSI でない当事者（ブリッジ・PSP・取引所）への波及義務はどの程度生じるか？
- FinCEN の「銀行秘密法に類似するが同一でない」という表現が意味する具体的な差異は何か？

## Links

- [Treasury 公式プレスリリース](https://home.treasury.gov/news/press-releases/sb0435)
- [FinCEN 規則案 PDF](https://www.fincen.gov/system/files/2026-04/PPSI-AMLCFT-NPRM.pdf)
- [Holland & Knight 解説](https://www.hklaw.com/en/insights/publications/2026/04/fincen-and-ofac-propose-aml-sanctions-rules-for-stablecoin-issuers)
- [DLA Piper 解説](https://www.dlapiper.com/en-us/insights/publications/2026/04/treasury-proposes-aml-cft-and-sanctions-compliance-rules-for-stablecoin-issuers-under-the-genius-act)

## Importance
- High

## Confidence
- High
