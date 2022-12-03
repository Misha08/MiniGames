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
            print('\n' * 2)
            Lottery.print_hello_text()
            Lottery.print_the_rules()
            print('\n')
            choice = int(input("How many players do you want to init?: "))
            number_to_find = int(input("How many numbers do you want to guess?: "))
            number_from_find = int(input("From how many digits do you want to guess these numbers ?: "))
            rounds = int(input("and how many rounds will there be?: "))
            l = Lottery(choice, number_to_find, number_from_find, rounds)
            l.init_players()
            l.play()
            # print(L.get_players())


def main():
    print_hello_text()
    choice_func()


if __name__ == "__main__":
    main()
    sys.exit(0)
