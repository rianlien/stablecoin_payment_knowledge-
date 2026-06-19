#!/usr/bin/env bash
# smoke.sh — verify all CLI tools in this knowledge base work correctly
# Run from repo root: bash .claude/skills/run-stablecoin-knowledge-base/smoke.sh

set -euo pipefail
PASS=0; FAIL=0

ok()   { echo "  ✓ $*"; PASS=$((PASS+1)); }
fail() { echo "  ✗ $*"; FAIL=$((FAIL+1)); }

echo "=== check_note_links.py ==="

# Full scan
OUT=$(mktemp /tmp/smoke_full_XXXXXX.json)
python3 .claude/hooks/check_note_links.py --output "$OUT" 2>&1 | grep -q "scanned=" \
  && ok "full scan: runs and prints summary" \
  || fail "full scan: failed"

python3 - <<EOF
import json, sys
d = json.load(open("$OUT"))
keys = {"generated_at","scanned_count","total_unlinked","notes","todo_suggestions"}
missing = keys - set(d.keys())
if missing:
    print("MISSING KEYS:", missing); sys.exit(1)
if d["scanned_count"] < 1:
    print("scanned_count is 0"); sys.exit(1)
EOF
ok "full scan: JSON has required keys and scanned_count > 0"

# --since flag
OUT7=$(mktemp /tmp/smoke_7d_XXXXXX.json)
python3 .claude/hooks/check_note_links.py --since 7 --output "$OUT7" 2>&1 | grep -q "scanned=" \
  && ok "--since 7: runs" \
  || fail "--since 7: failed"

python3 - <<EOF
import json
d7   = json.load(open("$OUT7"))
full = json.load(open("$OUT"))
assert d7["scanned_count"] <= full["scanned_count"], "--since 7 should scan <= full"
assert d7["todo_suggestions"] == [], "--since flag should suppress todo_suggestions"
EOF
ok "--since 7: scanned_count <= full; todo_suggestions empty"

echo ""
echo "=== post_brief_to_slack.py (dry-run, no webhook) ==="

OUTPUT=$(SLACK_WEBHOOK_URL="" python3 .claude/hooks/post_brief_to_slack.py 2>&1)
echo "$OUTPUT" | grep -q "SLACK_WEBHOOK_URL not set" \
  && ok "exits cleanly when SLACK_WEBHOOK_URL is unset" \
  || fail "unexpected output: $OUTPUT"

echo ""
echo "=== post_weekly_to_slack.py (dry-run, no webhook) ==="

OUTPUT_W=$(SLACK_WEBHOOK_URL="" python3 .claude/hooks/post_weekly_to_slack.py 2>&1)
echo "$OUTPUT_W" | grep -qiE "(not set|skipping)" \
  && ok "exits cleanly when SLACK_WEBHOOK_URL is unset" \
  || fail "unexpected output: $OUTPUT_W"

echo ""
echo "=== prompt files present ==="
for f in daily_routine_prompt.txt nightly_link_check_prompt.txt weekly_digest_prompt.txt; do
  [ -f ".claude/prompts/$f" ] && ok "$f exists" || fail "$f missing"
done

echo ""
if [ "$FAIL" -eq 0 ]; then
  echo "ALL $PASS checks passed."
else
  echo "$PASS passed, $FAIL FAILED."
  exit 1
fi
