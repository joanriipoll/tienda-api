ARG VARIANT="3.13-trixie"
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ENV DEBIAN_FRONTEND=noniteractive
ENV TZ=Europe/Madid


ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=1000


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"


#Tools for development
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    procps \
    file \
    unzip \
    python3 \
    python3-pip \
    pipx \
    locales \
    tree \
    && locale-gen en_US.UTF-8 \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip uv ruff

WORKDIR /workspace
USER vscode