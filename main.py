from HelloText import print_hello_text
from player import Player
from filework import *
import sys

# Parameters
doc_name = "Switches.txt"
sys.path.append("Games")

def choice_func():
    print("What the game do you want to play? ")
    print("1) Lottery")
    print("2) Mini Casino")
    print("3) Snake")
    print("4) Nim")
    choice = int(input())


def main():
    print_hello_text()


if __name__ == "__main__":
    main()
    sys.exit(0)
