FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY src/store-api/pyproject.toml src/store-api/uv.lock ./

RUN uv pip install --system -r pyproject.toml

COPY src/store-api/app ./app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]