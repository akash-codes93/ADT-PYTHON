class ExpenseStrategy:
    def split(self):
        pass


class ExpenseStrategyEqual(ExpenseStrategy):

    def split(self):
        pass


class ExpenseStrategyPercentage(ExpenseStrategy):
    def split(self):
        pass


class ExpenseStrategyExact(ExpenseStrategy):

    def split(self):
        pass


class Split():

    def parse_expense(self, string):
        text = string.split(' ')

        spender = text[1]
        amount = int(text[2])
        friends_count = int(text[3])
        friends = []
        for i in range(1, friends_count + 1):
            friends.append(text[3 + i])

        stragtegy = text[i]


        if stragtegy == 'EQUAL':
            pass

        elif stragtegy == 'EXACT':
            pass

        else:
            pass






