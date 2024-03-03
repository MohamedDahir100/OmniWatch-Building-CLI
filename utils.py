import json
from mongo_connect import db
import bcrypt
from user_model import User
from building import list_adjacent_rooms, print_building
from datetime import datetime

# Login function
def login():
    username = input("Username: ")
    password = input("Password: ")

    user = db.users.find_one({'username': username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        print("Login successful!")
        curr_user = User(user['username'], user['permission'], user['room'])

        return True, curr_user
    else:
        print("Login failed. Please try again.")
        return False, None

def choose_room(user, client):
    while True:
        room_list = ["Lobby", "Classroom", "Library", "Staff Lounge", "Dean's Office", "Laboratory", "Cafeteria"]
        # List adjacent rooms for the user to move through:
        print("Choose the next room to move to: \n")
        list_adjacent_rooms(user.room)
        print("\nPress q to exit building, press p to print building layout")
        print(f"Your current room is: {user.room}")


        newRoom = input("\nEnter: ")

        if newRoom in room_list:
            # Store the room the user is leaving
            old_room = user.room
            user.change_room(newRoom)
            print(f"Moved to {newRoom}")

            # Send new change to the frontend log
            notify_log(user, client, old_room)
        elif newRoom == 'p':
            print_building("layout.txt")
        elif newRoom == 'q':
            return;
        else:
            print("Error: please enter a valid command.\n")

def notify_log(user, client, old_room):
    room_permissions = get_room_permissions(user.room)
    stored_user = db.users.find_one({'username': user.username})

    access = user.has_access(room_permissions)

    # Send "Granted" or "Not Granted" for access:
    if access:
        access_str = "Granted"
    else:
        access_str = "Not Granted"
    


    log = {
        "id": str(stored_user['_id']),
        "username": user.username,
        "time": datetime.now().isoformat(),
        "enter": not user.in_lobby(),
        "exit": user.in_lobby(),
        "room": user.room,
        "prevRoom": old_room,
        "accessGranted": access_str
        }
    
    client.publish("backend/logs", json.dumps(log))
    return
            
        
def get_room_permissions(room):
    if room == "Dean's Office":
        return "admin"
    elif room == "Staff Lounge":
        return "staff"
    else:
        return "student"

def get_num_users(client):
    permissions = ["student", "staff", "admin"]

    for permission in permissions:
        count = db.users.count_documents({"permission": permission})

        # publish to topic with count and permission type:
        log = {"user_count": count, "user_type": permission}
        client.publish("backend/user_count", json.dumps(log))


        