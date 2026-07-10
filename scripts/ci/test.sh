#!/bin/bash
set -e
(
  cd /workspace/src/store-api
  set -a
  source /workspace/.devcontainer/.env
  set +a
  PYTHONPATH=$(pwd) uv run python -m pytest ../../tests/store-api -v
)