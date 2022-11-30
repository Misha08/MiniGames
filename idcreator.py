from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

general_collection = ascii_uppercase + ascii_lowercase + digits


class Id(object):
    def __init__(self):
        self.__id = ""

    def generate_id(self):
        for _ in range(6):
            self.__id += choice(general_collection)
        return self.__id


if __name__ == "__main__":
    id = Id()
    print(id.generate_id())