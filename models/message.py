import time

class message:

    def __init__(self, sender, message):
        self.__sender = sender
        self.__message = message
        self.__time = time.time()
    
    def get_sender(self):
        return self.__sender

    def get_message(self):
        return self.__message