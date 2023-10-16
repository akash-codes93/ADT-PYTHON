import unittest
from code1 import Solution, PieceType

INVALID_CHAR = "X"

KEYPAD = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    [INVALID_CHAR, "1", "2", "3", INVALID_CHAR]
]


class TestCase(unittest.TestCase):

    def test_result_10(self):
        res = Solution(KEYPAD, PieceType.knight, 10, 2).count_sequences()
        self.assertEqual(res, 1013398)

    def test_result_1(self):
        res = Solution(KEYPAD, 1, 2).count_sequences()
        self.assertEqual(res, 18)

    def test_next_pos_knight(self):
        obj = Solution(KEYPAD)
        valid_next_pos = {
            (0, 0): [(1, 2), (2, 1)],
            (0, 1): [(2, 0), (2, 2), (1, 3)],
            (0, 2): [(2, 1), (2, 3), (1, 4), (1, 0)],
            (0, 3): [(2, 2), (2, 4), (1, 1)],
            (0, 4): [(1, 2), (2, 3)],
            (1, 0): [(0, 2), (2, 2), (3, 1)],
            (1, 1): [(3, 2), (2, 3), (0, 3)],
            (1, 2): [(2, 4), (2, 0), (0, 0), (0, 4), (3, 1), (3, 3)],
            (1, 3): [(0, 1), (2, 1), (3, 2)],
            (1, 4): [(0, 2), (2, 2), (3, 3)],
            (2, 0): [(0, 1), (3, 2), (1, 2)],
            (2, 1): [(0, 2), (1, 3), (3, 3), (0, 0)],
            (2, 2): [(0, 1), (0, 3), (1, 0), (1, 4)],
            (2, 3): [(0, 2), (0, 4), (1, 1), (3, 1)],
            (2, 4): [(1, 2), (3, 2), (0, 3)],
            (3, 1): [(1, 0), (1, 2), (2, 3)],
            (3, 2): [(1, 1), (1, 3), (2, 0), (2, 4)],
            (3, 3): [(1, 2), (2, 1), (1, 4)]
        }
        self.assertEqual(obj.next_pos, valid_next_pos)

    def test_next_pos_rook(self):
        obj = Solution(KEYPAD, PieceType.rook)
        valid = {
            (1, 0): [(0, 0), (2, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
        }

        self.assertEqual(obj.next_pos, valid)

    def test_result_1_rook(self):
        res = Solution(KEYPAD, PieceType.rook, 10, 2).count_sequences()
        self.assertEqual(res, 18)
