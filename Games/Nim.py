from player import Player
from Games.Game import Game
import random


# The Nim game class
class Nim(Game):
    '''

    The Nim game class, works according to the following algorithm:

    1) When choosing when playing for 2, a pre-prepared list for players is created,
       When choosing "game with a computer", nothing is created, and the player is left alone
    2) The game works on the classic "Nim" algorithm
       https://www.geeksforgeeks.org/combinatorial-game-theory-set-2-game-nim/

    '''

    # Function Validation
    @staticmethod
    def checking(choice):
        return choice

    # Initialization
    def __init__(self, choice):
        self.choice = choice

        # Checking of choosing
        if self.checking(choice):
            self.players = ["Null", "Null"]

    # Specific redefined method
    def init_players(self):

        # Generate the sentences of creating the players
        string_of_count = 0
        for i in range(1, 3):
            if i == 1:
                string_of_count = f"{i}-st"
            elif i == 2:
                string_of_count = f"{i}-nd"

            # Request for first and last name
            name = input(f"What's the name of the {string_of_count} player: ")
            surname = input(f"What's the surname of the {string_of_count} player: ")

            # creating an instance of the player class, with the given first and last name, respectively
            player = Player(name, surname)
            self.players[i - 1] = player


    # Play with the computer
    @staticmethod
    def play_1(self):
        count = int(input("Initial number of stones in the first pile: "))
        count2 = int(input("Initial number of stones in the second pile: "))

        # The main game loop
        while count >= 0 or count2 >= 0:
            if count == 0 and count2 == 0:
                break
            else:

                # Checking for the presence of stones in the game
                if (count != 0 and count2 != 0 or count == 0 and count2 != 0 or
                        count != 0 and count2 == 0):

                    # The computer's turn
                    digit = random.randint(1, 10)
                    if count == 0:
                        pile = 2
                    elif count2 == 0:
                        pile = 1
                    else:
                        pile = random.randint(1, 2)

                    # The rest count
                    count_comp = count

                    if pile == 1:

                        # Collecting stones from the first pile
                        count_pile = count
                        count -= digit
                        if count <= 0:
                            digit = count_pile
                            count = 0

                    elif pile == 2:

                        # Collecting stones from the second pile
                        count2_pile = count
                        count2 -= digit
                        if count2 <= 0:
                            digit = count2_pile
                            count2 = 0

                    if count <= 0 and count2 <= 0:

                        # Calculating the computer's Victory
                        print("The computer took", count_comp, "stones are left",
                              '0')
                        print("The computer wins!")
                        break
                    else:

                        # Displaying the number of stones in the pile after the computer's turn
                        print("The computer took", digit, "stones from", pile,
                              "heap are left", count, count2)
                        takes = int(input("Select number of stones: "))
                        your_pile = int(input("Pick a bunch: "))

                        if your_pile == 1:

                            # Displaying the number of stones in the pile after the player's turn
                            count -= takes
                            print("The player took", takes, "stones from", your_pile,
                                  "heap are left", count, count2)
                        elif your_pile == 2:

                            # Displaying the number of stones in the pile after the player's turn
                            count2 -= takes
                            print("The player took", takes, "stones from", your_pile,
                                  "heap are left", count, count2)
                        if count <= 0 and count2 <= 0:

                            # Calculating the Player's Victory
                            print("The player took", takes, "stones are left",
                                  "0", "0")
                            print("The user wins!")
                            break

    # Play with the players
    def play_2(self):
        count = int(input("Initial number of stones in the first pile: "))
        count2 = int(input("Initial number of stones in the second pile: "))

        # The main game loop
        while count >= 0 or count2 >= 0:
            if count == 0 and count2 == 0:
                break
            else:

                # Checking for the presence of stones in the game
                if (count != 0 and count2 != 0 or count == 0 and count2 != 0 or
                        count != 0 and count2 == 0):

                    # The first player turn
                    digit = int(input(f"First player {self.players[0]} turn: "))
                    if count == 0:
                        pile = 2
                    elif count2 == 0:
                        pile = 1
                    else:
                        pile = int(input(f"First player {self.players[0]} turn: "))

                    # The rest count
                    count_comp = count

                    if pile == 1:

                        # Collecting stones from the first pile
                        count_pile = count
                        count -= digit
                        if count <= 0:
                            digit = count_pile
                            count = 0

                    elif pile == 2:

                        # Collecting stones from the second pile
                        count2_pile = count
                        count2 -= digit
                        if count2 <= 0:
                            digit = count2_pile
                            count2 = 0

                    if count <= 0 and count2 <= 0:

                        # Calculating the First Player's Victory
                        print(f"The first player {self.players[0]} took", count_comp, "stones are left",
                              '0')
                        print(f"The first player {self.players[0]} wins!")
                        self.players[0].add_super_score()

                        break

                    else:

                        # Displaying the number of stones in the pile after the first player's turn
                        print(f"The first player {self.players[0]} took", digit, "Stones from", pile,
                              "heap are left", count, count2)

                        takes = int(input("Select number of stones:"))
                        your_pile = int(input("Pick a bunch: "))

                        if your_pile == 1:
                            count -= takes

                            # Displaying the number of stones in the pile after the second player's turn
                            print(f"the second player {self.players[1]} took", takes, "second from", your_pile,
                                  "heap are left", count, count2)

                        elif your_pile == 2:
                            count2 -= takes

                            # Displaying the number of stones in the pile after the second player's turn
                            print(f"the second player {self.players[1]} took", takes, "stones from", your_pile,
                                  "heap are left", count, count2)

                        if count <= 0 and count2 <= 0:

                            # Calculating the Second Player's Victory
                            print(f"the second player {self.players[1]} took", takes, "stones are left",
                                  '0', '0')
                            print(f"The second player {self.players[1]} wins!")
                            self.players[1].add_super_score()

                            break

        # Call the function for getting info about the players
        self.get_players()

    # The main logical play function
    def play(self):
        if self.checking(self.choice):
            self.play_2()
        else:
            self.play_1()


# The Entry point for testing
if __name__ == "__main__":
    n = Nim(1)
    n.init_players()
    n.play()