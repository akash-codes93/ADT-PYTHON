from players import PlayerManager, Player
from piece import PieceType
from board import Board


class Game:

    def __init__(self):
        self.player_manager = PlayerManager()
        player1 = Player('p1', PieceType.X)
        player2 = Player('p2', PieceType.O)

        self.player_manager.add_player(player1)
        self.player_manager.add_player(player2)

        self.board = Board(3)
        self.start()

    def start(self):

        i = 0
        while True:
            player = self.player_manager[i]
            x, y = list(map(int, input("Enter position for " + player.name + ": ").split(' ')))

            try:
                self.board.set_place(x, y, player.piecetype)
            except Exception as e:
                print(e)
                continue

            i = (i + 1) % self.player_manager.players_count

            if self.board.check_winner(x, y, player.piecetype):
                print(player.name + " has won")
                print("Final Board: ")
                print(self.board.print())
                exit(0)


            if not self.board.is_pos_left():
                print("No positions left")
                print("Final Board: ")
                print(self.board.print())
                exit(0)
