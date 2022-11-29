from player import Player


class Lottery(object):
    def __init__(self, count_of_players=0, regime="4 from 20"):
        self.count_of_players = count_of_players
        self.players = list()

    def init_players(self):
        string_of_count = ""
        for i in range(1, self.count_of_players + 1):
            if i == 1:
                string_of_count = f"{i}-st"
            elif i == 2:
                string_of_count = f"{i}-nd"
            else:
                string_of_count = f"{i}-th"

            name = input(f"What's the name of the {string_of_count} player: ")
            surname = input(f"What's the name of the {string_of_count} player: ")

            player = Player(name, surname)
            self.players.append(player)

    def get_players(self):
        return self.players
