# Used for deployment only
FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .
COPY .env.test .

# Copy the api code
COPY backend/api ./backend/api
COPY backend/common ./backend/common

# Setup api
COPY pyproject.toml setup.cfg setup.py ./
RUN pip install -e .

# Make sure that the logging directory exists
ENV LOGGER_DIR=/var/log/app/
RUN mkdir -p ${LOGGER_DIR}

CMD cd /app/backend/api && uvicorn backend.api.endpoints:app --host 0.0.0.0 --port 7090

