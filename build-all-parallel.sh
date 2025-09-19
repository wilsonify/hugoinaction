#!/usr/bin/env bash
# build-all.sh — run `make all` for every makefile in the repo using GNU Parallel

set -euo pipefail

# Find all makefiles, feed into parallel
find . -type f -name "makefile" \
  | parallel --will-cite -j4 '
      dir=$(dirname {});
      echo ">>> Building in $dir"
      (cd "$dir" && make all)
    '
