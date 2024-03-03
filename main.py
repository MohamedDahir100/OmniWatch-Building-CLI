import mqtt_manager
import time
from utils import login, choose_room, get_num_users, sign_up

# Main function for CLI application:
def main():

    print(f"Welcome to the GuardianScribe building interaction simulator! \n")

    # Initialize mqtt client:
    mqttClient = mqtt_manager.MQTTClient()

    # Timeout to wait for mqtt connectino to be established:
    time.sleep(1)

    # Login before going through building
    while True:
        print("Would you like to login or sign up?\n")
        response = input("Enter: ")

        if response.capitalize() == "login".capitalize():
            login_success, user = login()

            if(login_success):
                break;
        elif response.capitalize() == "sign up".capitalize():
            signup_success, user = sign_up(mqttClient)

            if(signup_success):
                break;

        else:
            print("Please choose to login or sign up\n")

    # Initialize amount of students, teachers, deans in the frontend:
    get_num_users(mqttClient)

    # Start loop of moving between rooms:
    choose_room(user, mqttClient)

    # Passed this logic means that we have exited the building:
    mqttClient.disconnect()
    print("Exited building, Goodbye!")




if __name__ == "__main__":
    main()