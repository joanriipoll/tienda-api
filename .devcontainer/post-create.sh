#!/bin/bash

sudo chmod 666 /var/run/docker.sock

git config --global core.autocrlf false

cd /workspace/src/store-api && pip install -r requirements.txt --break-system-packages

echo "========================================================"
echo "Environment completed and dependencies deployed"
echo "========================================================"