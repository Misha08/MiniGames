from random import randint, shuffle
from player import Player
from field_creation_algorithm import *


class Lottery(object):

    @classmethod
    def validate_the_size_numbers(cls, count_of_ntf: int, count_of_nff: int):
        if 4 > count_of_ntf or count_of_ntf > count_of_nff:
            return False

        if 20 > count_of_nff or count_of_nff > 131:
            return False

        return True

    @classmethod
    def validate_the_count_of_rounds_and_players(cls, players: int, rounds: int):
        return (0 < rounds < 30) and (0 < players < 30)

    def __init__(self, count_of_players=0, number_to_find=4, number_from_find=20, rounds=1):
        if (Lottery.validate_the_count_of_rounds_and_players(count_of_players, rounds) and
                Lottery.validate_the_size_numbers(number_to_find, number_from_find)):
            self.players = list()
            self.count_of_players = count_of_players
            self.number_to_find = number_to_find
            self.number_from_find = number_from_find
            self.rounds = rounds
        else:
            raise(TypeError("Your data is wrong"))

    def init_players(self):
        for i in range(1, self.count_of_players + 1):
            match i:
                case 1:
                    string_of_count = f"{i}-st"
                case 2:
                    string_of_count = f"{i}-nd"
                case _:
                    string_of_count = f"{i}-th"

            name = input(f"What's the name of the {string_of_count} player: ")
            surname = input(f"What's the surname of the {string_of_count} player: ")

            player = Player(name, surname)
            self.players.append(player)

    def get_players(self):
        for player in self.players:
            print(player.get_info())

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
        set_of_guess_numbers = set()

        for _ in range(self.rounds):
            for player in self.players:
                result_turn = set()
                print(f"now it's turn of {player}")
                print("Do you want to guess numbers on one's own?")
                print("Type 0 here to have the game choose the numbers for you.")
                numbers = int(input("Type here: "))
                if numbers == 0:
                    while len(set_of_guess_numbers) < self.number_to_find:
                        num = randint(1, self.number_from_find)
                        set_of_guess_numbers.add(num)

                else:
                    while len(set_of_guess_numbers) < self.number_to_find:
                        num = int(input("Type here your number: "))
                        if 0 < num <= self.number_from_find and (num not in set_of_guess_numbers):
                            set_of_guess_numbers.add(num)
                        else:
                            print(f"Your number is too much bigger or smaller than {self.number_from_find}")
                            print("or maybe already in array of your guessed numbers")
                            print("Please type correct values!")

                while len(result_turn) < self.number_to_find:
                    num = randint(1, self.number_from_find)
                    result_turn.add(num)

                result_of_result = get_beautiful_field(self.number_from_find, field, set_of_guess_numbers, result_turn)

                beautiful_field = result_of_result[0]
                result_of_matching = result_of_result[1]

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
                    player.add_score(len(result_of_matching), 1)
                    get_field(beautiful_field)

                else:
                    print("/*!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!*/")
                    print("/*YOU HAVE BEEN GUESSING ALL THE NUMBERS!!!*/")
                    print("/*              GET A JACKPOT              */")
                    player.add_super_score()
                    get_field(beautiful_field)

        self.get_players()
