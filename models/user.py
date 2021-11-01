from flask_login import UserMixin
from models.room import Room


class User(UserMixin):

    def __init__(self, id, password = None, email = None, joined_rooms = [], friends = []):
        self.__joined_rooms = joined_rooms
        self.__id = id
        self.__email = email
        self.__password = password
        self.__friends = friends
        self.__current_room = None

    def get_current_room(self):
        return self.__current_room

    def set_current_room(self, room: Room):
        self.__current_room = room
        print(self.__current_room)

    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = None

    def get_friends_amount(self):
        return len(self.__friends)

    def get_rooms_amount(self):
        return len(self.__joined_rooms)

    def get_all(self):
        return f"ID: {self.__id}, email: {self.__email}, Current Room: {self.__current_room} ,password: {self.__password}, joined_rooms: {self.__joined_rooms}, friends: {self.__friends}"