FROM python:3.12-slim

WORKDIR /app

COPY src/store-api/requirements.txt /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY src/store-api/app /app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]