#!/usr/bin/env bash
# fetch_assets_locally.sh — download all official Drive assets into this repo.
# Run from the repository root. Requires: python3 -m pip install gdown
set -uo pipefail
cd "$(dirname "$0")/.."

command -v gdown >/dev/null || { echo "Installing gdown..."; pip3 install --user gdown || pipx install gdown; }

FAIL=0
while IFS='|' read -r id dest; do
  [ -z "$id" ] && continue
  mkdir -p "$(dirname "$dest")"
  if [ -s "$dest" ]; then echo "SKIP (exists): $dest"; continue; fi
  if ! gdown --quiet "https://drive.google.com/uc?id=${id}" -O "$dest"; then
    echo "gdown failed for $dest — curl fallback"
    curl -sSL --retry 3 -o "$dest" "https://drive.usercontent.google.com/download?id=${id}&export=download&confirm=t" || true
  fi
  if [ ! -s "$dest" ]; then echo "EMPTY: $dest"; FAIL=1
  elif head -c 500 "$dest" | grep -qi "<!doctype html\|<html"; then echo "HTML-ERROR-PAGE: $dest"; FAIL=1
  else echo "OK: $dest ($(stat -c%s "$dest") bytes)"; fi
done < tools/manifest.txt

echo "== summary =="
echo "images:  $(ls -1 images 2>/dev/null | wc -l)/54"
echo "logo:    $(ls -1 logo 2>/dev/null | wc -l)/4"
echo "png:     $(find assets/png -type f 2>/dev/null | wc -l)/6"
echo "profile: $(find assets/profile -type f 2>/dev/null | wc -l)/9"
echo "ref:     $(find reference -type f -name '*.pdf' 2>/dev/null | wc -l)/2"
exit $FAIL
