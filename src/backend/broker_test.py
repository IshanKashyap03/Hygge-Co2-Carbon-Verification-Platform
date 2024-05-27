import json
import paho.mqtt.client as mqtt
from config import (
    CERTIFICATE_DATA_BROKER_URL,
    CERTIFICATE_DATA_BROKER_PORT,
    CERTIFICATE_DATA_BROKER_TOPIC,
)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

if client.connect(CERTIFICATE_DATA_BROKER_URL, CERTIFICATE_DATA_BROKER_PORT) != 0:
    print("Connection failed")
    exit(1)

data = json.dumps(
    {
        "certificate_number": "1",
        "total_co2_emissions": 100.1,
        "start_date": 1715836780,
        "end_date": 1715836780,
        "company_name": "YourCompanyName",
    }
)
client.publish(CERTIFICATE_DATA_BROKER_TOPIC, data)
client.disconnect()
