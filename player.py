from idcreator import Id

id = Id()


class Player(object):
    def __init__(self, name: str, surname: str, score=0):
        self.__id = id.generate_id()
        self.__name = name
        self.__surname = surname
        self.__score = score

    def get_info(self):
        return f"{self.__name} {self.__surname} has the {self.__score} points"

    def add_score(self):
        self.__score += 1

    def __str__(self):
        return f"Player: {self.__name} {self.__surname}"

    def __repr__(self):
        return f"<Player: id: {self.__id }, name:'{self.__name}'," \
               f" surname:'{self.__surname}', score:{self.__score}>"
