# Stage 1: Build
FROM ubuntu:20.04 AS builder
WORKDIR /app
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3.11-dev gcc curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
COPY requirements.txt .
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim-buster AS runner
WORKDIR /app
RUN useradd -m appuser
USER appuser
COPY --from=builder /usr/lib/python3/dist-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/bin /usr/local/bin
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
