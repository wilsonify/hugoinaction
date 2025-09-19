#!/usr/bin/env bash
set -euo pipefail

# Top-level build script for Hugo in Action checkpoints
# Runs `make all` for every discovered makefile in the repo.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ">>> Starting full build under: $ROOT_DIR"

# Find all makefiles, sort them for reproducibility
find "$ROOT_DIR" -type f -name "makefile" | sort | while read -r mk; do
    dir="$(dirname "$mk")"
    echo
    echo ">>> Building in: $dir"
    (
        cd "$dir"
        make all || {
            echo "!!! Build failed in $dir"
            exit 1
        }
    )
done

echo
echo ">>> All builds completed successfully."
