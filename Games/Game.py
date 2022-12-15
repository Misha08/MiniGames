from player import Player


# The main Game class
class Game(object):
    '''

    The main class from which other classes of the game inherit

    '''

    # Initialization method
    def __init__(self, count_of_players):
        self.count_of_players = count_of_players
        self.players = list()

    # The setter of the list of players
    def init_players(self):
        '''

        This function creates players while displaying a proposal to create certain players,
        the number of which declines depending on the number of the player being created,
        Then an object is created and added to the list of players

        '''

        # Generate the sentences of creating the players
        for i in range(1, self.count_of_players + 1):
            if i == 1:
                string_of_count = f"{i}-st"
            elif i == 2:
                string_of_count = f"{i}-nd"
            else:
                string_of_count = f"{i}-th"

            # Request for first and last name
            name = input(f"What's the name of the {string_of_count} player: ")
            surname = input(f"What's the surname of the {string_of_count} player: ")

            # creating an instance of the player class, with the given first and last name, respectively
            player = Player(name, surname)
            self.players.append(player)

    # The getter of the list of players
    def get_players(self):
        '''

        This function displays data about players (Displays data from the list of players), namely:
        1) Name
        2) Surname
        3) Score

        '''
        for player in self.players:
            print(player.get_info())

    # Main logic game class
    def play(self):
        '''

        In case of absence, for a number of reasons, the method is played in inherited classes.

        '''
        return -1

    # Destructor
    def __del__(self):
        print(f"The end of the Game \"{self.__class__.__name__}\"")
