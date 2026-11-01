#!/usr/bin/env bash
# install symlinks in harness dirs

set -euo pipefail
repo="$(cd "$(dirname "$0")" && pwd)"
for target in ~/.agents/skills ~/.claude/skills; do
  mkdir -p "$target"
  for skill in "$repo"/*/; do
    name="$(basename "$skill")"
    [ -f "$skill/SKILL.md" ] || continue
    ln -sfn "$skill" "$target/$name"
  done
done
