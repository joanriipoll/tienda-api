#!/bin/bash

cd "$(dirname "$0")/../.."

cd src/store-api

uv run uvicorn app.main:app --app-dir "$(pwd)" --host 0.0.0.0 --port 8000 --reload