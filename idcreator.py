from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

# Collection of the ascii symbols
general_collection = ascii_uppercase + ascii_lowercase + digits


# ID class
class Id(object):
    # Initialization
    def __init__(self):
        self.__id = ""

    # The function of generate ID
    def generate_id(self):

        # Filling the id with the six random ascii characters
        for _ in range(6):
            self.__id += choice(general_collection)

        # Return id for the player
        return self.__id