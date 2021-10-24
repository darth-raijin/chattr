from flask_pymongo import PyMongo

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
        
        result_dict = {
            "id": result.get("__id"),
            "email": result.get("email"),
            "joined_rooms": result.get("joined_rooms"),
            "friends": result.get("friends")
            }
        return result_dict

    def create_user(self, user_id: str, email: str, password: str):
        try:
            result = mongo.db.users.insert_one({"_id": user_id, "email": email, "password": password, "joined_rooms": [], "friends": []})
            return True
        except:
            return "Username not unique"