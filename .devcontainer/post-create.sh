#!/bin/bash

sudo chmod 666 /var/run/docker.sock

git config --global core.autocrlf false

cd /workspace/src/store-api && pip install -r requirements.txt --break-system-packages

echo "========================================================"
echo "👋 ¡ENTORNO COMPLETO Y DEPENDENCIAS DESPLEGADAS, JOAN!"
echo "========================================================"