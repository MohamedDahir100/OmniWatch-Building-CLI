import mqtt_manager
import time
from utils import login, choose_room, get_num_users

# Main function for CLI application:
def main():

    print(f"Welcome to the GuardianScribe building interaction simulator! \n")
    # Login before going through building
    print("Please Enter your login: \n")
    while True:
        login_success, user = login()

        if(login_success):
            break;

    # Initialize mqtt client:
    mqttClient = mqtt_manager.MQTTClient()

    # Timeout to wait for mqtt connectino to be established:
    time.sleep(1)

    # Initialize amount of students, teachers, deans in the frontend:
    get_num_users(mqttClient)

    # Start loop of moving between rooms:
    choose_room(user, mqttClient)

    # Passed this logic means that we have exited the building:
    mqttClient.disconnect()
    print("Exited building, Goodbye!")




if __name__ == "__main__":
    main()