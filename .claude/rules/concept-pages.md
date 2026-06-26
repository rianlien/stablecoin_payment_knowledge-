---
paths:
  - "03_Topics/**/*.md"
  - "04_Protocols/**/*.md"
  - "05_MOCs/**/*.md"
  - "06_Entities/**/*.md"
---

# 概念ページの Contract

`03_Topics` / `04_Protocols` / `05_MOCs` / `06_Entities` の概念ページが満たすべき形。
層 = Intent〜Contract（論点の枠組み・横断マップ＝**保護資産**）。思想は `_meta/PHILOSOPHY.md`。

## 非対称ルール（最重要）
- 新しい事実（`00_Inbox`）が既存の枠組みと矛盾しても、**枠組みを黙って上書きしない**。矛盾は当該ページ上で明示（surface）して残す。
- 概念ページは frontmatter に `type:`（topic / protocol / company / moc 等）を持ち、層マーカーを兼ねる。

## 来歴（根拠ノートの紐付け）
- ニュースノート作成時、対応する概念ページに当該ノートのリンクを追記する。
  - `06_Entities/Companies|Networks|Organizations/` — "Inbox との紐付け" テーブル
  - `04_Protocols/` — "関連ニュース" テーブル
  - `05_MOCs/` / `03_Topics/` — 関連する MOC / トピック
- 追記は既存テーブルに合わせ `| 日付 | [[ノート名]] | 位置づけ一行 |` の形式を維持する。
- 対応する概念ページが存在しない場合は、リンク追加をスキップしてよい（無理に作成しない）。
- リンク追記はニュースノート作成と同じ run で行う。
