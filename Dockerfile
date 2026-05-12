# syntax=docker/dockerfile:1.7

FROM python:3.12-alpine AS builder

WORKDIR /app

COPY requirements.txt .

# Instalacja zależności
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.12-alpine

LABEL org.opencontainers.image.authors="Nikodem Kamiński"

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY app.py .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8080

# Sprawdzenie działania aplikacji
HEALTHCHECK CMD wget --no-verbose --tries=1 --spider http://localhost:8080 || exit 1

CMD ["python", "app.py"]