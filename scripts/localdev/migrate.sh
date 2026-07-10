#!/bin/bash

set -e
(
cd /workspace/src/store-api
if [ -z "$DATABASE_URL" ]; then
    echo "❌ ERROR: The DATABASE_URL environment variable is not set."
    echo "Ensure your environment has injected the environment variables correctly."
    exit 1
  fi
uv run alembic upgrade head
)