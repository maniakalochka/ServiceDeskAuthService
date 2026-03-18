FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    UV_SYSTEM_PYTHON=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl ca-certificates \
    postgresql-client redis-tools \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && ln -s /root/.local/bin/uv /usr/local/bin/uv

WORKDIR /app

COPY . /app/

RUN uv sync --frozen