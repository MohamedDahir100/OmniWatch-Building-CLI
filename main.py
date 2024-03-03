import mqtt_manager
import time
from user_model import populate_users
from utils import login
from building import print_building

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


    


if __name__ == "__main__":
    main()