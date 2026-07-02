#!/bin/bash
set -e
cd "$(dirname "$0")/../.."
cd src/store-api
uv run ruff check "$(pwd)"
uv run ruff format --check "$(pwd)"
uv run pyrefly check "$(pwd)"
