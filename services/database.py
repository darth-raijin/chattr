from flask_pymongo import PyMongo
import datetime

mongo = PyMongo()

class Database:


    def __init__(self):
        return

    def get_mongo(self):
        # Used in app.py to set configs
        print("Mongo retrieved")
        return mongo

    def get_user_by_id(self, user_id: str):
        result = mongo.db.users.find({"_id": user_id})
        result_dict = {}

        for item in result: 
            print("User found")       
            result_dict = {
                "id": item.get("_id"),
                "email": item.get("email"),
                "joined_rooms": item.get("joined_rooms"),
                "friends": item.get("friends"),
                "password": item.get("password")
                }
            print(result_dict)
        if not result_dict:
            return None

        return result_dict

    def create_user(self, user_id: str, email: str, password: str):
        try:
            result = mongo.db.users.insert_one({"_id": user_id, "email": email, "password": password, "joined_rooms": [], "friends": []})
            return True
        except:
            return False

    def create_room(self, name, description, public: bool, creator: str):
        try:
            result = mongo.db.rooms.insert_one({"name": name, "description": description, "public": public, "admin": [creator], "members": [creator], "date": datetime.datetime.utcnow()})
            return True
        except:
            return False