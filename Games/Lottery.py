from random import randint
from player import Player


class Lottery(object):
    def __init__(self, count_of_players=0, number_to_find=4, number_from_find=20):
        self.players = list()
        self.count_of_players = count_of_players
        self.number_to_find = number_to_find
        self.number_from_find = number_from_find

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
            surname = input(f"What's the name of the {string_of_count} player: ")

            player = Player(name, surname)
            self.players.append(player)

    def get_players(self):
        return self.players

    def play(self):
        size_of_playing_field = self.number_from_find / self.number_to_find
        # print("Now it's up to you which move will be first.")
        # first = randint(1, len(self.players))

        while True:
            pass
