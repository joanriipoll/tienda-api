#!/bin/bash 
set -e

sudo chmod 666 /var/run/docker.sock

git config --global core.autocrlf false

cd /workspace/src/store-api

uv sync

echo "========================================================"
echo "Environment completed and dependencies deployed"
echo "========================================================"