import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# MongoDB setup
connection_string = os.getenv('MONGODB_URI')
client = MongoClient(connection_string)
db = client.GuardianScribe