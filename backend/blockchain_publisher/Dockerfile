# Use a base Python image
FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .
COPY .env.test .

COPY backend/blockchain_publisher ./backend/blockchain_publisher
COPY backend/common ./backend/common

# Copy the configuration files
COPY pyproject.toml setup.cfg setup.py ./
RUN pip install -e .

# Make sure that the logging directory exists
ENV LOGGER_DIR=/var/log/app/
RUN mkdir -p ${LOGGER_DIR}

CMD cd /app/backend/blockchain_publisher && python -m main
