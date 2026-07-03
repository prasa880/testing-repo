# ---- Build stage ----
FROM python:3.12 AS builder
WORKDIR /app
COPY app.py .

# ---- Runtime stage ----
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/app.py .
EXPOSE 8080
CMD ["python3", "app.py"]
