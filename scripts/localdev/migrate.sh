#!/bin/bash

set -e
set -a
source /workspace/.devcontainer/.env
set +a
cd /workspace/src/store-api
uv run alembic upgrade head
