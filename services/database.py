from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
            result = mongo.db.users.insert_one(
                {"_id": user_id, "email": email, "password": password, "joined_rooms": [], "friends": []})
            return True
        except:
            return False

    def create_room(self, name, description, public: bool, creator: str):
        try:
            result = mongo.db.rooms.insert_one({"name": name, "description": description, "public": public, "admin": [
                                               creator], "members": [creator], "date": datetime.datetime.utcnow()})
            return True
        except:
            return False

    def get_public_rooms(self):
        try:
            rooms = []
            result = mongo.db.rooms.find({"public": "on"})

            for item in result:
                rooms.append({
                    "id": item.get("_id"),
                    "name": item.get("name"),
                    "description": item.get("description"),
                    "public": item.get("public"),
                    "admin": item.get("admin"),
                    "members": item.get("members"),
                    "member_count": len(item.get("members"))
                })
            print("Public room fetch complete")
            return rooms
        except:
            print("Public room fetch failed")
            return rooms

    def get_private_rooms(self, _id: str):
        try:
            rooms = []
            result = mongo.db.rooms.find({"members": _id,  "public": "off"})

            for item in result:
                if item.get("public") == "off":
                    rooms.append({
                        "id": item.get("_id"),
                        "name": item.get("name"),
                        "description": item.get("description"),
                        "public": item.get("public"),
                        "admin": item.get("admin"),
                        "members": item.get("members"),
                        "member_count": len(item.get("members"))
                    })
            
            print("Private room fetch complete")
            return rooms
        except:
            print("Private room fetch failed")
            return False
    
    def get_room_by_user(self, _id: str):
        try:
            rooms = []
            result = mongo.db.rooms.find({"members": _id})

            for item in result:
                rooms.append({
                    "id": item.get("_id"),
                    "name": item.get("name"),
                    "description": item.get("description"),
                    "public": item.get("public"),
                    "admin": item.get("admin"),
                    "members": item.get("members"),
                    "member_count": len(item.get("members"))
                })
            
            print("Private room fetch complete")
            return rooms
        except:
            print("Private room fetch failed")
            return rooms

    # TODO this needs fixing fr fr
    def get_all_accessible_rooms(self, user_id: str):
        try:
            rooms = []

            public_rooms = self.get_public_rooms()
            print(public_rooms)
            for item in public_rooms:
                print("started public fetch")
                if item:
                    rooms.append(item)
            print(f"public rooms: {rooms}".format(rooms = rooms))

            private_rooms = self.get_private_rooms(user_id)
            for item in private_rooms:
                print("Started private room fetch")
                if item:
                    print(item)
                    rooms.append(item)
            print("{private_rooms} PRIVATE ")
           

            print(rooms)

            return rooms
        except:
            print(rooms)
            print("All accessible rooms fetch failed")
            return False

    def get_room_by_id(self, id: str):
        try:
            result = mongo.db.rooms.find({"_id": ObjectId(id)})        
            for item in result: 
                room = {
                    "_id": item.get("_id"),
                    "name": item.get("name"),
                    "description": item.get("description"),
                    "public": item.get("public"),
                    "admin": item.get("admin"),
                    "members": item.get("members"),
                }
                print(room)
                return room
                
        except:
            return False
            # TODO When connecting update the user
    def add_room_to_user(self, user: str, room_id: str):
        NotImplemented

    def add_member_to_room(self, user, room):
        try:
            mongo.db.rooms.update({'_id': ObjectId(room)}, {'$push': {'members': user}})
            mongo.db.users.update({'_id': user}, {'$push': {'joined_rooms': ObjectId(room)}})
            return True

        except:
            return False