import sys
from HelloText import print_hello_text
from player import Player
from Games.Lottery import Lottery
from Games.Snake import Snake
from Games.Nim import Nim
from filework import *


# Parameters
doc_name = "Switches.txt"


# Function to select between games
def choice_func():

    # The list of the choice of the games
    while True:
        print("What the game do you want to play? ")
        print("1) Lottery - 1")
        print("2) Snake - 2")
        print("3) Nim - 3")
        print("Exit the program - 0")
        choice = int(input("Write your choice here: "))

        if choice == 0:
            break

        # Make choice
        if choice == 1:

            # The Lottery game launch algorithm

            # Output of welcome text and rules of the game
            print('\n' * 2)
            Lottery.print_hello_text()
            Lottery.print_the_rules()
            print('\n')

            # Collecting data to form the game
            choice = int(input("How many players do you want to init?: "))
            number_to_find = int(input("How many numbers do you want to guess?: "))
            number_from_find = int(input("From how many digits do you want to guess these numbers ?: "))
            rounds = int(input("and how many rounds will there be?: "))

            # Creating the Lottery game itself
            l = Lottery(choice, number_to_find, number_from_find, rounds)
            l.init_players()
            l.play()

        elif choice == 2:
            choice = int(input("How many players do you want to init?: "))
            s = Snake(choice)
            s.init_players()
            s.play()

        elif choice == 3:
            print("Do you play with players?: ")
            print("1 and other values - play with players")
            print("0 - don't play with players")
            choice = int(input("Type here: "))
            n = Nim(choice)
            if choice:
                n.init_players()
                n.play()
            else:
                n.play()


# The main function
def main():
    print_hello_text()
    choice_func()


# Entry point
if __name__ == "__main__":
    main()
    sys.exit(0)
