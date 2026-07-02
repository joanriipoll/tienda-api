#!/bin/bash
set -e
cd "$(dirname "$0")/../.."
cd src/store-api
if [ "$1" == "--fix" ]; then
    RUFF_CHECK_ARG="--fix"
    RUFF_FORMAT_ARG=""
else
    RUFF_CHECK_ARG=""
    RUFF_FORMAT_ARG="--check"
fi
uv run ruff check $RUFF_CHECK_ARG "$(pwd)"
uv run ruff format $RUFF_FORMAT_ARG "$(pwd)"
uv run pyrefly check "$(pwd)"