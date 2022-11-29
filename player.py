class Player(object):
    def __init__(self, name: str, surname: str, score=0):
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
        return f"<Player: name:{self.__name}, surname:{self.__surname}, score:{self.__score}>"
