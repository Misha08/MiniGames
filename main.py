import sys
from HelloText import print_hello_text
from player import Player
from Games.Lottery import Lottery
from filework import *


# Parameters
doc_name = "Switches.txt"


def choice_func():
    print("What the game do you want to play? ")
    print("1) Lottery")
    print("2) Mini Casino")
    print("3) Snake")
    print("4) Nim")
    choice = int(input("Write your choice here: "))
    match choice:
        case 1:
            choice = int(input("How many players do you want to init?: "))
            L = Lottery(choice)
            L.init_players()
            print(L.get_players())


def main():
    print_hello_text()
    choice_func()


if __name__ == "__main__":
    main()
    sys.exit(0)
