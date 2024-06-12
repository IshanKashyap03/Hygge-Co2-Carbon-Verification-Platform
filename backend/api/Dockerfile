FROM python:3.10-slim

WORKDIR /app

# Make sure that the logging directory exists
ENV LOGGER_DIR=/var/log/app/
RUN mkdir -p ${LOGGER_DIR}

# Install PostgreSQL client and development libraries (so we can use psql)
RUN apt-get update && \
    apt-get install -y libpq-dev gcc postgresql-client && \
    apt-get clean

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy environment variables
COPY .env ./
COPY .env.test ./

# Copy the api code
COPY backend/api ./backend/api
COPY backend/common ./backend/common

# Copy the configuration files
COPY pyproject.toml setup.cfg setup.py ./
RUN pip install -e .

CMD cd /app/backend/api && ./wait-for-postgres.sh db && uvicorn backend.api.endpoints:app --host 0.0.0.0 --port 7090
