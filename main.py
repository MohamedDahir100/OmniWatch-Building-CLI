import mqtt_manager
import time

# Main function for CLI application:
def main():
    mqttClient = mqtt_manager.MQTTClient()

    # Testing to see if a connection can be established:
    while True:
        mqttClient.subscribe("log/update")
        mqttClient.publish("Wassup dude", "log/update")
        print("published message")
        time.sleep(5)  # Publish every 5 seconds


if __name__ == "__main__":
    main()