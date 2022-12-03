from random import randint, shuffle
from player import Player
from field_creation_algorithm import create_field


class Lottery(object):
    def __init__(self, count_of_players=0, number_to_find=4, number_from_find=20, rounds=1):
        self.players = list()
        self.count_of_players = count_of_players
        self.number_to_find = number_to_find
        self.number_from_find = number_from_find
        self.rounds = rounds

    def init_players(self):
        string_of_count = ""
        for i in range(1, self.count_of_players + 1):
            match i:
                case 1:
                    string_of_count = f"{i}-st"
                case 2:
                    string_of_count = f"{i}-nd"
                case other:
                    string_of_count = f"{i}-th"

            name = input(f"What's the name of the {string_of_count} player: ")
            surname = input(f"What's the surname of the {string_of_count} player: ")

            player = Player(name, surname)
            self.players.append(player)

    def get_players(self):
        return self.players

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

    def play(self):

        field = create_field(self.number_from_find)
        shuffle(self.players)
        arr_of_guess_num = list()
        counter = 0
        summ = 0

        for number_round in range(self.rounds):
            for player in self.players:
                print(f"now it's turn of {player}")
                print("Do you want to guess numbers on one's own?")
                print("Type 0 here to have the game choose the numbers for you.")
                numbers = int(input("Type here: "))
                if numbers == 0:
                    arr_of_guess_num = [randint(1, self.number_from_find + 1) for _ in range(self.number_to_find)]
                else:
                    while counter < self.number_to_find:
                        num = int(input("Type here your number: "))
                        if 0 < num <= self.number_from_find:
                            arr_of_guess_num.append(num)
                            counter += 1
                        else:
                            print(f"Your number is too much bigger or smaller than {self.number_from_find}")
                            print("Please type correct values!")