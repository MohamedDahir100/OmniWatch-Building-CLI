from mongo_connect import db
from bson.objectid import ObjectId


def populate_building():
    building_layout = {
        "Lobby": ["Classroom", "Library", "Laboratory", "Staff Lounge", "Dean's Office", "Cafeteria"],
        "Classroom": ["Lobby"],
        "Library": ["Lobby"],
        "Laboratory": ["Lobby"],
        "Staff Lounge": ["Lobby"],
        "Dean's Office": ["Lobby"],
        "Cafeteria": ["Lobby"]
    }   
    
    building_collection = db.buildings
    building_collection.insert_one(building_layout)

def list_adjacent_rooms(curr_room):
    building = db.buildings.find_one({'_id': ObjectId('65e4465d15b35d4489e1f96e')})
    adjacent_rooms = building[curr_room]

    # Print the adjacent rooms, numbered
    for index, room in enumerate(adjacent_rooms, start=1):
        print(f"{index}. {room}")

def print_building(layout_file):
    try:
        with open(layout_file, 'r') as file:
            for line in file:
                print(line, end='')  # end='' to avoid adding extra newline characters
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



populate_building()