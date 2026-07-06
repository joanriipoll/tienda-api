#!/bin/bash

set -e
(
cd "$(dirname "$0")/../../"
uv run --project src/store-api pytest tests/ -v
)
