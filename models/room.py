class Room:

    def __init__(self, id, name, description = None, members = [], public = True, admin = []):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__members = members
        self.__public = public
        self.__admin = admin

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description
    
    def get_members(self):
        return self.__members

    def add_member(self, member_id: str):
        self.__members.append()
    
    def get_public(self):
        return self.__public
    
    def set_public(self, public: bool):
        return self.__public
        
    def get_admin(self):
        return self.__admin

    def set_admin(self, admin: str):
        self.__admin.append(admin)
