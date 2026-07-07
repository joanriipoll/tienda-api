#!/bin/bash

set -e
(
cd "$PROJECT_PATH"
uv run --project src/store-api pytest tests/ -v
)
