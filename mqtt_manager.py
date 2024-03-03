import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv
import certifi

# Loading credentials from .env:
load_dotenv()
broker_address = os.getenv('MQTT_BROKER_ADDRESS')
port = int(os.getenv('MQTT_PORT'))
username = os.getenv('MQTT_USERNAME')
password = os.getenv('MQTT_PASSWORD')

class MQTTClient:
    def __init__(self, broker_address=broker_address, port=port, username=username, password=password):
        # Establishing connection:
        self.client = mqtt.Client(transport='websockets')
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(username, password)
        self.client.tls_set(ca_certs=certifi.where())
        self.client.connect(broker_address, port)
        self.client.loop_start()

    def connect(self):
        self.client.connect(self.broker_address, self.port, 60)
        # Removed loop_start here

    def disconnect(self):
        self.client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")

    def on_message(self, client, userdata, msg):
        print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

    def publish(self, message, topic):
        self.client.publish(topic, message)

    def subscribe(self, topic):
        self.client.subscribe(topic)

