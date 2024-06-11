# Used for deployment only
FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .

RUN mkdir /contract
COPY src/contract /contract

COPY src/backend .

# Make sure that the logging directory exists
ENV LOGGER_DIR=/var/log/app/
RUN mkdir -p ${LOGGER_DIR}

CMD ["uvicorn", "endpoints:app", "--host", "0.0.0.0", "--port", "7090"]

