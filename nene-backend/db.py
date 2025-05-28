
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["nene_barbearia"]

users_collection = db["users"]
appointments_collection = db["appointments"]
