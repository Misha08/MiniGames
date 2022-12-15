from random import randint, shuffle
from field_creation_algorithm import *
from Games.Game import Game
from Games.ValidExcept import ValidExcept


# Main game class
class Lottery(Game):
    '''

    The Lottery Class Game

    Built on the calculation of random values and the formation of fields,
    including those with shaded guessed numbers, see the description of the function algorithms below

    '''

    # The Validate methods
    # Validation of input data to form the playing field
    @staticmethod
    def validate_the_size_numbers(count_of_ntf: int, count_of_nff: int):

        '''

        This function checks the input dimensions, the number of search numbers and field numbers,
        and returns true or false depending on their compatibility with the requirements.

        Allowed values for the formation of the correct field and the number of numbers to be searched:

        a) For number of numbers to look for:
        1) Minimum value: 4
        2) Maximum value: The value of the 'Count of numbers on the playing field'

        b) For number of numbers on the playing field:
        1) Minimum value: 20
        2) Maximum value: 131

        !!! In case of data invalidity, the value false will be returned and
        instead of creating an instance of the class (Object), an exception will be raised !!!

        '''

        # Checking the value of the number of numbers you are looking for
        if count_of_ntf < 4 or count_of_nff < count_of_ntf:
            return False

        # Checking the value of the number of numbers in the playing field
        if 20 > count_of_nff or count_of_nff > 131:
            return False

        return True

    # Validation of rounds in the game
    @staticmethod
    def validate_the_count_of_rounds_and_players(players: int, rounds: int):
        '''

        This function checks the number of rounds and players in the game

        Allowed values for the count of players and the count of the rounds:

        a) For players:
        1) Minimum value: 1
        2) Maximum value: 30

        b) For rounds:
        1) Minimum value: 1
        2) Maximum value: 131

        '''
        return (0 < rounds <= 30) and (0 < players <= 30)

    # Method for initialization The object of the class
    def __init__(self, count_of_players=0, number_to_find=4, number_from_find=20, rounds=1):
        '''

        Magic Initialization Method that creates an instance with parameters such as:

        1) The Number of players in the game (count_of_players)
        2) The Number of numbers to be found (number_to_find)
        3) The Number of numbers from which these numbers will be searched (number_from_find)
        4) The number of rounds (rounds)

        '''

        if (Lottery.validate_the_size_numbers(number_to_find, number_from_find) and\
                Lottery.validate_the_count_of_rounds_and_players(count_of_players, rounds)):

            # Delegation
            super().__init__(count_of_players)
            self.number_to_find = number_to_find
            self.number_from_find = number_from_find
            self.rounds = rounds
        else:
            raise ValidExcept

    # Functions for displaying texts
    @staticmethod
    def print_hello_text():
        print("/*------------------------------*/")
        print("Have you long wanted to try your luck without losing real money?")
        print("Then you just got this opportunity!")

    @staticmethod
    def print_the_rules():
        print("/*------------------------------*/")
        print("The rules are simple, players play in turns,")
        print("first there is a vote on who will still be the first, the rest are distributed")
        print("randomly and no one knows who will move.")
        print("Players ask how many of how many numbers to guess and how many rounds")
        print("and how many rounds will there be.")
        print("Well, good luck to you, my dear)")

    # Function to start the Game (Main logical function in this Class)
    def play(self):
        '''

        A single function that creates the entire gameplay.

        Function algorithm:
        1) Creating a clear playing field with numbers from 1 to 20
        and an empty set of numbers to be chosen by the player or randomly generated
        2) The list of players is shuffled so that it is not known exactly who goes first
        3) A playing field and an empty set are created for randomly generated numbers or guessed by the player.
        4) The beginning of the game itself, lasting 'self.rounds' rounds
        5) Start iterating through the list of players
        6) Creating an empty set that will be filled with random numbers,
        with which the results will be calculated and the choice is given whether numbers will be generated,
        which are to be chosen randomly or by the player
        7) In the case of a random selection of numbers,
        the empty set is filled with random numbers provided that they are absent in the set
        8) In the case of a user choice of numbers, the empty set is filled with the numbers entered by the user,
        provided that they are not in the set. in the case of a user choice of numbers,
        the empty set is filled with the numbers entered by the user, provided they are not in the set;
        9) A set of numbers is filled in, with which the user's numbers must match
        10) There is a comparison of matches between the final numbers selected by the lottery
        and the numbers entered by users, a playing field is formed with crossed out numbers
        and a set of matching user numbers and final numbers is issued
        11) Calculation of issuing points to the player who made the move is performed, in case of a jackpot,
        the method of issuing a large number of points is triggered
        12) At the end of the game, the results of the players are given

        '''

        # Creation a playing field and an empty set are created
        # for randomly generated numbers or guessed by the player.
        field = create_field(self.number_from_find)
        set_of_guess_numbers = set()

        # Shuffle order of players
        shuffle(self.players)

        # The game starts according to the given rounds
        for _ in range(self.rounds):

            # Start the iteration through the list of players
            for player in self.players:
                # Formation of an empty set of given numbers by the player or random numbers
                result_turn = set()

                # Alert, whose turn it is
                print(f"now it's turn of {player}")
                print("Do you want to guess numbers on one's own?")
                print("Type 0 here to have the game choose the numbers for you.")

                # Player choice of number selection method
                choice_to_create_numbers = int(input("Type here: "))
                if choice_to_create_numbers == 0:
                    # Random Number Generation Loop
                    while len(set_of_guess_numbers) < self.number_to_find:
                        num = randint(1, self.number_from_find)
                        set_of_guess_numbers.add(num)

                else:
                    # Beginning of the loop to add random counts in instead of the player's selection
                    while len(set_of_guess_numbers) < self.number_to_find:

                        # Player number
                        num = int(input("Type here your number: "))

                        # Checking the correctness of the entered data
                        if 0 < num <= self.number_from_find and (num not in set_of_guess_numbers):
                            set_of_guess_numbers.add(num)
                        else:
                            # Notification of incorrectly entered data
                            print(f"Your number is too much bigger or smaller than {self.number_from_find}")
                            print("or maybe already in array of your guessed numbers")
                            print("Please type correct values!")

                # Beginning of the player
                while len(result_turn) < self.number_to_find:
                    num = randint(1, self.number_from_find)
                    result_turn.add(num)

                # Displaying a field with filled numbers that the player guessed
                result_of_result = get_beautiful_field(self.number_from_find, field, set_of_guess_numbers, result_turn)

                # Get the result to the field with crossed out numbers, and random number generation result
                beautiful_field = result_of_result[0]
                result_of_matching = result_of_result[1]

                # Check the number of matches, to add points
                if not result_of_matching:
                    print('\n')
                    print("/*------------------------------------------------*/")
                    print("Unfortunately, you didn't guess a single number :(")
                    print("/*------------------------------------------------*/")
                elif result_of_matching != set_of_guess_numbers:
                    print('\n')
                    print("/*------------------------------------------------*/")
                    print(f"you guessed {str(len(result_of_matching))} numbers!")
                    print("/*------------------------------------------------*/")
                    print('\n')

                    # Adding points to the player making the move and getting
                    # a field with guessed numbers crossed out
                    player.add_score(len(result_of_matching), 1)
                    get_field(beautiful_field)
                else:

                    # Jackpot message output
                    print("/*!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!*/")
                    print("/*YOU HAVE BEEN GUESSING ALL THE NUMBERS!!!*/")
                    print("/*              GET A JACKPOT              */")

                    # Adding a large number of points to the player making the move and getting
                    # a field with guessed numbers crossed out
                    player.add_super_score()
                    get_field(beautiful_field)

        # Call the function for getting info about the players
        self.get_players()
