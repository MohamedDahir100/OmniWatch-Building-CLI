import bcrypt
from mongo_connect import db

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Populating default users into the database:
def populate_users():
    users = [
        {"username": "student1", "password": hash_password("password1"), "permission": "student", "room": "Lobby"},
        {"username": "student2", "password": hash_password("password2"), "permission": "student", "room": "Lobby"},
        {"username": "teacher1", "password": hash_password("password3"), "permission": "staff", "room": "Lobby"},
        {"username": "teacher2", "password": hash_password("password4"), "permission": "staff", "room": "Lobby"},
        {"username": "admin", "password": hash_password("adminpass"), "permission": "admin", "room": "Lobby"},
    ]

    users_collection = db.users
    users_collection.insert_many(users)
    print("Users populated successfully.")

# User information (username, permissons, their current room):
class User:
    def __init__(self, username, permission, room):
        self.username = username
        self.permission = permission
        self.room = room
    
    def has_access(self, roomPermission):
        if self.permission == "admin":
            return True
        elif self.permission == "staff" and roomPermission != "admin":
            return True
        elif self.permission == roomPermission:
            return True
        else:
            return False
        
    def change_room(self, newRoom):
        self.room = newRoom
        db.users.update_one(
            {'username': self.username},
            {'$set': {'room': newRoom}}
        )
    
    def in_lobby(self):
        return self.room == "Lobby"
