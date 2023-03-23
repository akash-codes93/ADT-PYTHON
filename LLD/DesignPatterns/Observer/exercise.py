"""
Imagine a game where one or more rats can attack a player. Each individual rat has an initial attack value of 1.
However, rats attack as a swarm, so each rat's attack value is actually equal to the total number of rats in play.

Given that a rat enters play through the initializer and leaves play (dies) via its __exit__ method,
please implement the Game and Rat classes so that, at any point in the game,
the Attack value of a rat is always consistent.

Here's a sample unit test your code should pass:

def test_three_rats_one_dies(self):
    game = Game()

    rat = Rat(game)
    self.assertEqual(1, rat.attack)

    rat2 = Rat(game)
    self.assertEqual(2, rat.attack)
    self.assertEqual(2, rat2.attack)

    with Rat(game) as rat3:
        self.assertEqual(3, rat.attack)
        self.assertEqual(3, rat2.attack)
        self.assertEqual(3, rat3.attack)

    self.assertEqual(2, rat.attack)
    self.assertEqual(2, rat2.attack)
"""

# import unittest
#
#
# class Game:
#     def __init__(self):
#         self.rats = []
#
#     def add_rat(self, rat):
#         self.rats.append(rat)
#
#
# class Rat:
#     def __init__(self, game):
#         self.game = game
#         self._attack = 1
#         self.game.add_rat(self)
#
#     def __enter__(self):
#         return self
#
#     @property
#     def attack(self):
#         attack = 0
#         for rat in self.game.rats:
#             attack += rat._attack
#         return attack
#
#     @attack.setter
#     def attack(self, value):
#         self._attack = value
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.game.rats.remove(self)

import unittest


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.rat_enters = Event()
        self.rat_dies = Event()
        self.notify_rat = Event()


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1

        game.rat_enters.append(self.rat_enters)
        game.notify_rat.append(self.notify_rat)
        game.rat_dies.append(self.rat_dies)

        self.game.rat_enters(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rat_dies(self)

    def rat_enters(self, which_rat):
        if which_rat != self:
            self.attack += 1
            self.game.notify_rat(which_rat)

    def notify_rat(self, which_rat):
        if which_rat == self:
            self.attack += 1

    def rat_dies(self, which_rat):
        self.attack -= 1


class TestObserver(unittest.TestCase):
    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)


if __name__ == '__main__':
    unittest.main()
    # game = Game()
    #
    # rat = Rat(game)
    # print(rat.attack)
    #
    # rat2 = Rat(game)
    # print(rat.attack)
    # print(rat2.attack)
