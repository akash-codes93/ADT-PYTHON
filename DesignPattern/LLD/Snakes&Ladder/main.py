import random


class Game:

    def __init__(self, board, players):
        self.players = players
        self.board = board
        self.winner = None

    def check_winner(self, player):
        if player.pos == self.board.MAX_POS:
            return True
        return False

    def declare_winner(self, p):
        self.winner = p
        print(str(p) + " is winner")
        exit(0)

    def is_move_valid(self, move):
        if 0 <= move <= 6:
            return True
        return False

    def update_position(self, player, move):
        new_pos = player.pos + move
        if new_pos > self.board.MAX_POS:
            print(f"Move not possible for {player}, move: {move}")
            return

        player.pos = new_pos
        element = self.board.get_element_exists(new_pos)
        if element:
            print(element)
            player.pos = element.end

    def roll(self, player, move):
        if not self.is_move_valid(move):
            print("Bad Move")

        self.update_position(player, move)
        print(str(player) + f" after move: {move}")
        if self.check_winner(player):
            self.declare_winner(player)


class Player:

    def __init__(self, name):
        self.name = name
        self.pos = 0

    def check_reached_final(self):
        pass

    def __str__(self):
        return f'Player: {self.name} is at pos: {self.pos}'


class Board(list):
    MAX_POS = 100

    def append(self, *args, **kwargs):
        # can check if ladder or snake already not present
        print(args[0])
        element = args[0]
        if isinstance(element, Snake) or isinstance(element, Ladder):
            super().append(*args, **kwargs)
            return
        print("Not a snake/ladder type")

    def get_element_exists(self, pos):
        for element in self:
            if element.is_present(pos):
                return element
        return None


class BoardElement:

    def __init__(self, start, end):
        if not self.is_valid(start, end):
            print("Bad element")
        self.start = start
        self.end = end

    def is_valid(self, start, end):
        pass

    def is_present(self, pos):
        return self.start == pos


class Snake(BoardElement):

    def is_valid(self, start, end):
        if start < end :
            return False
        return True

    def __str__(self):
        return f"Snake at pos: {self.start}"


class Ladder(BoardElement):

    def is_valid(self, start, end):
        if start > end:
            return False
        return True

    def __str__(self):
        return f"Ladder at pos: {self.start}"


if __name__ == "__main__":
    b = Board()
    s1 = Snake(99, 14)
    s2 = Snake(47, 23)
    s3 = Snake(23, 12)

    l1 = Ladder(10, 80)
    l2 = Ladder(27, 49)
    l3 = Ladder(62, 73)

    b.append(s1)
    b.append(s2)
    b.append(s3)
    b.append(l1)
    b.append(l2)
    b.append(l3)

    p1 = Player("John")
    p2 = Player("Jane")

    g = Game(b, [p1, p2])

    while True:
        move1 = random.randint(1, 6)
        g.roll(p1, move1)

        move2 = random.randint(1, 6)
        g.roll(p2, move2)
