#!/bin/bash
set -e
(
  cd /workspace/src/store-api
  if [ -z "$DATABASE_URL" ]; then
    exit 1
  fi
  PYTHONPATH=$(pwd) uv run python -m pytest ../../tests/store-api -v
)