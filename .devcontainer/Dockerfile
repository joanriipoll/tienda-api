FROM ubuntu:24.04


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


RUN userdel -r ubuntu 2>/dev/null || true \
    && groupdel ubuntu 2>/dev/null || true \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME


WORKDIR /workspace
USER $USERNAME