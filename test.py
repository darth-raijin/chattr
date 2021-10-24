import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
client = pymongo.MongoClient(
            "mongodb+srv://Kaido:{}@cluster0.d1usl.mongodb.net/chattr?retryWrites=true&w=majority".format(os.getenv("MONGO_PASSWORD")))

db = client.chattr

collections = db.list_collection_names()

print(collections)