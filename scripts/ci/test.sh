#!/bin/bash

set -e
cd "$(dirname "$0")/../../"
export PYTHONPATH="$PWD/src/store-api"
uv run --project src/store-api pytest tests/ -v