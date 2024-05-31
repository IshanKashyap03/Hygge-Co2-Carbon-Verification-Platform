FROM python:3.10-slim

WORKDIR /app

# Install PostgreSQL client and development libraries
RUN apt-get update && \
    apt-get install -y libpq-dev gcc postgresql-client && \
    apt-get clean

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /contract
COPY src/contract /contract

COPY src/backend .

CMD ["./wait-for-postgres.sh", "db", "uvicorn", "endpoints:app", "--host", "0.0.0.0", "--port", "8000"]

