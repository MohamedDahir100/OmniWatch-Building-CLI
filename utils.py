from enum import Enum
from mongo_connect import db
import bcrypt
from user_model import User

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
