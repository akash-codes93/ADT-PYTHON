from enum import Enum, auto


class Split(Enum):
    Exact = auto()
    Equal = auto()
    Percentage = auto()


class ExpenseSheet(dict):

    def print_expense_sheet(self):
        sheet = {}
        for user, expenses in self.items():
            sheet.update({
                user.name: round(sum(expenses), 2)
            })

        return sheet


class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name

        self.__expense_sheet = ExpenseSheet()

    def add_user_expense(self, user, expense):

        if user not in self.__expense_sheet:
            self.__expense_sheet[user] = [expense]
        else:
            self.__expense_sheet[user].append(expense)

    @property
    def total_expense(self):
        total_expense = 0
        for _, expense in self.__expense_sheet.items():
            total_expense += sum(expense)
        return round(total_expense, 2)

    def get_expense_sheet(self):
        return self.__expense_sheet.print_expense_sheet()

    def __str__(self):
        return self.name


class Group:

    def __init__(self, name):
        self.name = name
        self.__users = []
        self.__expense_sheet = ExpenseSheet()

    def add_user(self, user):
        if not isinstance(user, User):
            print("User should be of type user")
            return
        if user in self.__users:
            print("user already present in group")

        self.__users.append(user)

    def update_expense(self, user, expense):

        if user not in self.__expense_sheet:
            self.__expense_sheet[user] = [expense]
        else:
            self.__expense_sheet[user].append(expense)

    def verify_user(self, user):

        if user not in self.__users:
            return False
        return True

    def add_expense(self, user, expense):
        if not self.verify_user(user):
            print("user not present in group please add first")
            return
        self.calculate_expense(user, expense)

    def calculate_expense(self, user, expense):

        if expense.type == Split.Equal:
            equal_amount = expense.amount / len(self.__users)

            for group_user in self.__users:
                if group_user != user:
                    group_user.add_user_expense(user, -equal_amount)
                    self.update_expense(group_user, -equal_amount)
                else:
                    group_user.add_user_expense(user, expense.amount - equal_amount)
                    self.update_expense(group_user, expense.amount - equal_amount)
        elif expense.type == Split.Exact:
            for group_user, amount in expense.exact_distribution:
                if not self.verify_user(group_user):
                    print(f"Invalid user: {group_user} in distribution, not present in group")
                    return

            for group_user in self.__users:
                amount = expense.exact_distribution.get(group_user)
                group_user.add_user_expense(user, amount)
                self.update_expense(group_user, amount)

        elif expense.type == Split.Percentage:
            for group_user, amount in expense.percentage_distribution:
                if not self.verify_user(group_user):
                    print(f"Invalid user: {group_user} in distribution, not present in group")
                    return

            for group_user, perc in expense.percentage_distribution:

                if user != group_user:
                    amount = -(expense.amount * perc) / 100
                else:
                    amount = (expense.amount * (100 - perc)) / 100

                group_user.add_user_expense(user, amount)
                self.update_expense(group_user, amount)

    def get_expense_sheet(self):
        return self.__expense_sheet.print_expense_sheet()


class Expense:

    def __init__(self, id, amount, type=Split.Equal, description=""):
        self.id = id
        self.amount = amount
        self.description = description
        self.type = type

        self.exact_distribution = None
        self.percentage_distribution = None

    def set_split_exact(self, expenses):
        if sum(expenses.values()) != 0:
            print(f"Sum does not match amount: {self.amount} of expense")
            return

        self.type = Split.Exact
        self.exact_distribution = expenses

    def set_percentage_distribution(self, expenses):
        if sum(expenses.values()) != 100:
            print("Percentage sum not 100")

        self.type = Split.Percentage
        self.percentage_distribution = expenses


jane = User(1, "Jane")
john = User(2, "John")
peter = User(3, "Peter")
uma = User(3, "Uma")

g1 = Group("house")
g1.add_user(jane)
g1.add_user(john)
g1.add_user(peter)
g1.add_user(uma)

ex1 = Expense(1, 100)
g1.add_expense(jane, ex1)
print(g1.get_expense_sheet())
ex1 = Expense(1, 100)
g1.add_expense(john, ex1)
print(g1.get_expense_sheet())
ex1 = Expense(1, 100)
g1.add_expense(peter, ex1)
print(g1.get_expense_sheet())

print(uma.get_expense_sheet())
print(uma.total_expense)
