#!/bin/bash

echo "[Host] Iniciando preparativos en el sistema anfitrión..."

OS_TYPE=$(uname -s)
case "$OS_TYPE" in
    Darwin)
        echo "[Host] Detectado entorno macOS."
        ;;
    Linux)
        echo "[Host] Detectado entorno Linux. Asegurando huellas de ~/.ssh..."
        mkdir -p ~/.ssh && chmod 700 ~/.ssh
        ;;
    *)
        echo "[Host] Sistema operativo no identificado: $OS_TYPE"
        ;;
esac

echo "[Host] Preparativos completados con éxito."