#!/bin/bash

set -e
(
cd /workspace/src/store-api
if [ -z "$DATABASE_URL" ]; then
    exit 1
fi
uv run alembic upgrade head
)