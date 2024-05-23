import json
import paho.mqtt.client as mqtt
from controller import create_certificate
from config import (
    CERTIFICATE_DATA_BROKER_USERNAME,
    CERTIFICATE_DATA_BROKER_PORT,
    CERTIFICATE_DATA_BROKER_URL,
    CERTIFICATE_DATA_BROKER_PASSWORD,
    CERTIFICATE_DATA_BROKER_TOPIC,
)


# Callback function when a message is received
def on_message(client, userdata, message):
    decoded_message = message.payload.decode()
    message_dict = json.loads(decoded_message)

    # TODO: Check data for validity
    certificate_id = message_dict.get("certificate_number")
    amount = message_dict.get("total_co2_emissions")
    start_time = message_dict.get("start_date")
    end_time = message_dict.get("end_date")
    company_name = message_dict.get("company_name")

    create_certificate(
        certificate_id, float(amount), start_time, end_time, company_name
    )


# Callback function when connecting to the broker
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(CERTIFICATE_DATA_BROKER_TOPIC)
    else:
        print(f"Failed to connect, return code {reason_code}")


# Set up the MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(
    CERTIFICATE_DATA_BROKER_USERNAME, CERTIFICATE_DATA_BROKER_PASSWORD
)
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(CERTIFICATE_DATA_BROKER_URL, CERTIFICATE_DATA_BROKER_PORT)

# Start the loop to process received messages
client.loop_forever()
