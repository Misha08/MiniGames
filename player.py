from idcreator import Id
from Games.ValidExcept import ValidExcept

# ID object
Id = Id()


class Player(object):

    '''

    The Player class which describes its methods and parameters.

    '''

    # The validate function
    @staticmethod
    def validation_of_name_and_surname(check_name: str, check_surname: str):
        '''

        Here the parameters are checked: first name and last name for emptiness,
        in case of emptiness (equality of an empty string)
        at least one of the parameters is returned false

        '''
        return check_name.replace(" ", "") and check_surname.replace(" ", "")

    # Magic function for initialization class object
    def __init__(self, name: str, surname: str, score=0):
        '''

        :param name:
        :param surname:
        :param score:
        '''
        if Player.validation_of_name_and_surname(name, surname):
            self.__id = Id.generate_id()
            self.__name = name
            self.__surname = surname
            self.__score = score
        else:
            raise ValidExcept

    # Get result function
    def get_info(self):
        return f"{self.__name} {self.__surname} has the {self.__score} points"

    # Adding points for achievements in the game
    def add_score(self, multiplier=1, outp=0):
        self.__score = self.__score + 100 * multiplier
        if outp:
            print(f"You have got {100 * multiplier} points")
            print('\n')
        else:
            pass

    # Adding points for special achievements in the game
    def add_super_score(self):
        self.__score += 20000

    # View representations of a class object for users
    def __str__(self):
        return f"Player {self.__name} {self.__surname}"

    # View representations of a class object for developers
    def __repr__(self):
        return f"<Player: id: {self.__id }, name:'{self.__name}'," \
               f" surname:'{self.__surname}', score:{self.__score}>"
