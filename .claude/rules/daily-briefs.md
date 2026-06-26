---
paths:
  - "01_Daily-Briefs/**/*.md"
---

# Daily Brief の Contract

`01_Daily-Briefs/YYYY-MM/YYYY-MM-DD.md` が満たすべき形。層 = Contract（出力）。
作り方の手順は `.claude/skills/daily-news/SKILL.md`、テンプレートは `90_Templates/daily_brief_template.md`。

## 出力ルール
- その run で**新規採用した項目だけ**を書く。
- 重要項目がない日も作成または更新し、「該当なし」と明記する。
- `新規追加ノート` 内 `リンク:` は必ず `[Source Name（YYYY-MM-DD）](URL)` 形式で書く（裸の URL や別形式は不可）。
  - この形式制約の Mechanism 上の理由（Slack 投稿スクリプトが裸 URL を認識しない）は `_meta/ARCHITECTURE.md` を参照。
- ユーザーが会話中に手動で記事 URL を渡した場合（routine 自動実行ではないケース）は、追記先を当日ではなく **翌日**（JST currentDate + 1）の `01_Daily-Briefs/YYYY-MM/YYYY-MM-DD.md` にする。翌日ファイルが無ければ新規作成する。
