import unittest

from players import Player, PlayerManager
from piece import PieceType

class TestPlayer(unittest.TestCase):

    def test_players_count(self):
        p1 = Player('p1', PieceType.X)
        p2 = Player('p2', PieceType.O)
        pm = PlayerManager()
        pm.add_player(p1)
        pm.add_player(p2)

        self.assertEqual(pm.players_count, 2)


if __name__ == '__main__':
    unittest.main()



