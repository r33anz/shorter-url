from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

client = MongoClient(f"mongodb://{HOST}:{PORT}")


db = client["url_shortener"]
urls_collection = db["urls"]
