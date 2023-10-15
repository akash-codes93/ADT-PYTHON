class Player:
    def __init__(self, name, piecetype):
        self.name = name
        self.piecetype = piecetype


class PlayerManager:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __getitem__(self, idx):
        if idx >= len(self.players):
            raise Exception("Invalid Player")
        return self.players[idx]

    @property
    def players_count(self):
        return len(self.players)
