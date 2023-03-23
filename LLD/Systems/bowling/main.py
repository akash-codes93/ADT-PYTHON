ALLEY = [1, 2, 3, 4]


class Game:

    def __init__(self, id, players=[]):
        self.players = players
        self.id = id
        self.alley = self._get_alley()
        self.completed = False

    def _get_alley(self):
        if len(ALLEY) == 0:
            print("No empty alley")
            return
        else:
            return ALLEY.pop()

    def roll(self, player, pin):
        if self.completed:
            print("Game is completed")
            return
        player.roll(pin)

    def declare_winner(self):
        winner_player = None
        winner_player_score = 0
        for player in self.players:
            if player.score > winner_player_score:
                winner_player = player
                winner_player_score = player.score

        return winner_player

    def complete(self):
        self.completed = True
        ALLEY.append(self.alley)


class PinBoard(dict):
    TOTAL_SETS = 10

    def __init__(self):
        base = {
            i: [0, 0] for i in range(PinBoard.TOTAL_SETS)
        }
        base[PinBoard.TOTAL_SETS - 1].append(0)
        self._current_set = 0
        self._round = 0
        super().__init__(base)

    def is_set_valid(self):
        if self.current_set < PinBoard.TOTAL_SETS:
            return True
        return False

    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, round_number):
        self._round = round_number

    def is_final_set(self):
        if self.current_set == PinBoard.TOTAL_SETS:
            return True
        return False

    def next_set(self):
        self._current_set += 1

    @property
    def current_set(self):
        return self._current_set

    @current_set.setter
    def current_set(self, set_number):
        self._current_set = set_number


class Player:

    def __init__(self, name):
        self.score = 0
        self.name = name
        self.pin_board = PinBoard()

    def is_strike(self):
        pass

    def is_spare(self):
        pass

    def roll(self, pins):
        if not self.pin_board.is_set_valid():
            print("Set not valid")
            return
        self.pin_board[self.pin_board.current_set][self.pin_board.round] = pins
        self.update_score()

    def update_score(self):
        is_strike = False
        is_spare = False
        # print(self.pin_board.current_set)
        # print(self.pin_board.round)
        # print("---")
        if self.pin_board.round == 0:
            if self.pin_board[self.pin_board.current_set][self.pin_board.round] == 10:  # strike
                is_strike = True
                self.score += 20
                self.pin_board.current_set += 1
            else:
                self.score += self.pin_board[self.pin_board.current_set][self.pin_board.round]
                self.pin_board.round = 1
        elif self.pin_board.round == 1:
            self.score += self.pin_board[self.pin_board.current_set][self.pin_board.round]
            if sum(self.pin_board[self.pin_board.current_set]) == 10:  # spare
                is_spare = True
                self.score += 5
            self.pin_board.current_set += 1
            self.pin_board.round = 0
        elif self.pin_board.round == 2:
            self.score += self.pin_board[self.pin_board.current_set][self.pin_board.round]

        if self.pin_board.is_final_set() and (is_strike or is_spare):
            self.pin_board.current_set -= 1
            self.pin_board.round = 2

    def __str__(self):
        return f"Player: {self.name}"


p1 = Player('Akash')

g = Game(1, [p1])

g.roll(p1, 8)
g.roll(p1, 1)
g.roll(p1, 10)
g.roll(p1, 10)
g.roll(p1, 10)
g.roll(p1, 10)
g.roll(p1, 10)
g.roll(p1, 10)
g.roll(p1, 10)
g.roll(p1, 8)
g.roll(p1, 2)
g.roll(p1, 8)
g.roll(p1, 2)
g.roll(p1, 1)

# print(p1.score)
# print(p1.pin_board)

print(g.declare_winner())