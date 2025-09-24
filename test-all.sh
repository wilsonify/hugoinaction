#!/usr/bin/env bash
set -euo pipefail

# Top-level build script for Hugo in Action checkpoints
# Runs `make all` for every discovered makefile in the repo.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ">>> Starting full build under: $ROOT_DIR"

# Find all tests
find "$ROOT_DIR" -type f -name "test*" ! -path "*/__pycache__/*" | sort | while read -r mk; do
    dir="$(dirname "$mk")"
    echo
    echo ">>> Testing in: $dir"
    (
        cd "$dir"
        pytest || {
            echo "!!! Build failed in $dir"
            exit 1
        }
    )
done

echo
echo ">>> All tests completed"
