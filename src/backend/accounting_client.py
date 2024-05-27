import json
from typing import Callable
import paho.mqtt.client as mqtt

from config import (
    CERTIFICATE_DATA_BROKER_USERNAME,
    CERTIFICATE_DATA_BROKER_PORT,
    CERTIFICATE_DATA_BROKER_URL,
    CERTIFICATE_DATA_BROKER_PASSWORD,
    CERTIFICATE_DATA_BROKER_TOPIC,
)
from utils import is_float

PAHO_LOG_LEVELS = {
    mqtt.MQTT_LOG_INFO: "INFO",
    mqtt.MQTT_LOG_NOTICE: "SUCCESS",
    mqtt.MQTT_LOG_WARNING: "WARNING",
    mqtt.MQTT_LOG_ERR: "ERROR",
    mqtt.MQTT_LOG_DEBUG: "DEBUG",
}


class CertificateDataClient:
    def __init__(self, data_process_callback: Callable, logger) -> None:
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.set_username_password(
            CERTIFICATE_DATA_BROKER_USERNAME, CERTIFICATE_DATA_BROKER_PASSWORD
        )
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_log = self._on_log
        self.data_process_callback = data_process_callback
        self.logger = logger
        self.url = CERTIFICATE_DATA_BROKER_URL
        self.port = CERTIFICATE_DATA_BROKER_PORT
        self.topic = CERTIFICATE_DATA_BROKER_TOPIC
        self.logger.info("Certificate Data Client Initialized")

    def start(self):
        """Starts the client by connecting to the broker and starting the loop"""
        self.logger.info("Connecting to MQTT Broker")
        self.client.connect(self.url, self.port)
        self.logger.info("Starting MQTT Client")
        self.client.loop_start()

    def stop(self):
        """Stops the client by disconnecting from the broker and stopping the loop"""
        self.logger.info("Disconnecting from MQTT Broker")
        self.client.loop_stop()

    def set_username_password(self, username: str, password: str) -> None:
        self.client.username_pw_set(username, password)

    def set_url_port(self, url: str, port: int) -> None:
        """Sets the url and port to allow the client to connect to the broker using the provided URL and port"""
        self.url = url
        self.port = port

    def set_topic(self, topic: str) -> None:
        """Sets the topic to allow the client to subscribe to the provided topic"""
        self.topic = topic

    def _validate_data(self, data_name: str, data: str | None) -> bool:
        """Validates if the data is provided. If not, logs an error message and returns True"""
        if data is None:
            self.logger.critical("{data_name} must be provided", data_name=data_name)
            return True
        return False

    def _on_log(self, client, userdata, paho_log_level, messages) -> None:
        """Callback function used for logging"""
        log_level = PAHO_LOG_LEVELS.get(paho_log_level)
        if log_level is not None:
            self.logger.log(
                log_level,
                "PAHO: {messages}",
                messages=messages,
            )
        else:
            self.logger.error(
                "PAHO log level provided is invalid. Messages:{messages}", messages
            )

    def _on_message(self, client, userdata, message) -> None:
        """Callback function when a message is received"""
        payload = message.payload
        self.logger.info("Received message: {payload}", payload=payload)
        decoded_message = message.payload.decode()
        message_dict = json.loads(decoded_message)

        certificate_id = message_dict.get("certificate_number")
        if self._validate_data("certificate_number", certificate_id):
            return

        amount = message_dict.get("total_co2_emissions")
        if self._validate_data("total_co2_emissions", amount):
            return
        if not is_float(amount):
            self.logger.critical("total_co2_emissions is not a float")
            return

        start_time = message_dict.get("start_date")
        if self._validate_data("start_date", start_time):
            return

        end_time = message_dict.get("end_date")
        if self._validate_data("end_date", end_time):
            return

        company_name = message_dict.get("company_name")
        if self._validate_data("company_name", company_name):
            return

        # TODO: Change this back to info and remove the return statement
        self.logger.warning(
            "Received message: {certificate_id}, {amount}, {start_time}, {end_time}, {company_name}",
            certificate_id=certificate_id,
            amount=amount,
            start_time=start_time,
            end_time=end_time,
            company_name=company_name,
        )

        self.data_process_callback(
            certificate_id, float(amount), start_time, end_time, company_name
        )

    def _on_connect(self, client, userdata, flags, reason_code, properties) -> None:
        """Callback function when connecting to the broker"""
        if reason_code == 0:
            self.logger.info("Connected to MQTT Broker!")
            client.subscribe(self.topic)
        else:
            self.logger.error(
                "Failed to connect, return code {reason_code}", reason_code=reason_code
            )
