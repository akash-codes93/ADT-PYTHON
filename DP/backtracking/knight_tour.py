"""
Below code uses backtracking
"""


class Solution:
    n = 5

    def is_valid(self, position, covered):

        i = position[0]
        j = position[1]

        if i < 0 or j < 0 or i >= self.n or j >= self.n or covered[i][j] == 1:
            return False

        return True

    def get_next_moves(self, position, covered):

        positions = []

        i = position[0]
        j = position[1]

        pos = (i + 2, j + 1)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i + 2, j - 1)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i - 2, j + 1)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i - 2, j - 1)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i + 1, j + 2)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i + 1, j - 2)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i - 1, j + 2)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i - 1, j - 2)
        if self.is_valid(pos, covered):
            positions.append(pos)

        return positions

    def knight_tour(self, position, total_pos, path, covered):

        if total_pos == (self.n * self.n):
            print(path)
            exit(0)
            return

        positions = self.get_next_moves(position, covered)
        # print(position, positions, total_pos)
        for each_position in positions:
            path.append(each_position)
            covered[each_position[0]][each_position[1]] = 1
            self.knight_tour(each_position, total_pos + 1, path, covered)

            path.pop()
            covered[each_position[0]][each_position[1]] = 0

    def driver(self, position=(0, 0)):
        path = []
        covered = [[0 for __ in range(self.n)] for _ in range(self.n)]
        self.knight_tour(position, 0, path, covered)


# Solution().driver()

"""
Below code uses warnsdroff algorithm
"""


class Solution2:
    n = 5

    def is_valid(self, position, covered):

        i = position[0]
        j = position[1]

        if i < 0 or j < 0 or i >= self.n or j >= self.n or covered[i][j] >= 0:
            return False

        return True

    def get_next_moves(self, position, covered):

        positions = []

        i = position[0]
        j = position[1]

        pos = (i + 2, j + 1)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i + 2, j - 1)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i - 2, j + 1)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i - 2, j - 1)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i + 1, j + 2)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i + 1, j - 2)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i - 1, j + 2)
        if self.is_valid(pos, covered):
            positions.append(pos)

        pos = (i - 1, j - 2)
        if self.is_valid(pos, covered):
            positions.append(pos)

        return positions

    def warnsdroff(self, covered):
        """Instead of going to every next move, we go the move which as minimum next moves"""
        counter = 0

        initial_pos = (0, 0)

        for i in range((self.n * self.n) - 1):
            positions = self.get_next_moves(initial_pos, covered)

            if len(positions) == 0:
                print('No solution possible')
                break
            min_pos = positions[0]

            for position in positions:

                if len(self.get_next_moves(position, covered)) < len(self.get_next_moves(min_pos, covered)):
                    min_pos = position

            initial_pos = min_pos
            counter += 1
            covered[initial_pos[0]][initial_pos[1]] = counter

        print(covered)

    def driver(self):
        covered = [[-1 for __ in range(self.n)] for _ in range(self.n)]
        covered[0][0] = 0

        self.warnsdroff(covered)


Solution2().driver()
