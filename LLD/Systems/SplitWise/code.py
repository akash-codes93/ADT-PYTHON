'''

Design Splitwise

SPLIT EQUALLY - Splitting the amount equally into all members of a group
Example- 4000 split equally among 8 persons equals 500 as due amount on each person

SPLIT EXACTLY - Exact Split distributes the amount to the exact given amount.
Example- 4000 divided exactly into two persons as 2500, 1500. First person owes 2500 and the second 1500 to the creditor

SPLIT BY PERCENTAGE - Split the given amount as per the given percentage values
Example- 4000 divided among 4 in the percentage 10%, 20%, 20% and 50% would
mean the first user owe an amount of 400, second and third would owe
800 each and the fourth person would owe a total of 2000 to the creditor.

Requirements -

1. Every user who uses the app should be registered. Only registered users can be involved
in expense metrics.
2. Expenses created should be of type EXACT, EQUAL or PERCENT only.
➢ In case of EXACT and PERCENT, verify if the figures match the given total amount
3. At any point of time, the application can print the total sum owed and individual amounts
owed to and by each user.
4. The final amount should be rounded off to two decimal places. And the total should add
up to the principal amount.
'''
import dataclasses
from typing import List, Dict

from abc import ABC, abstractmethod


@dataclasses.dataclass
class User:
    userId: int
    name: str
    totalAmountOwed: float = 0.0
    ledger: Dict[int, float] = dataclasses.field(default_factory=dict)

    def get_total_amount_owed(self) -> float:
        return self.totalAmountOwed

    def print_ledger(self) -> None:
        print("-----Ledger for User: ", self.name, "-----")
        for user_id, amount in self.ledger.items():
            user_name = UserManager().get_user_name(user_id)
            if user_id == self.userId:
                continue
            if amount < 0:
                print(f"{user_name} Debt: ", amount)
            elif amount > 0:
                print(f"{user_name} Credit:", amount)

        print("Total Amount Owed:", self.get_total_amount_owed())

    def update_ledger(self, user_id: int, amount: float):
        if user_id in self.ledger:
            self.ledger[user_id] += amount
        else:
            self.ledger[user_id] = amount

    def update_total_amount_owed(self, amount: float):
        self.totalAmountOwed += amount


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class UserManager(metaclass=Singleton):
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add_user(self, user: User):
        self.users[user.userId] = user

    def print_ledger(self, user: User = None) -> None:
        if user:
            user.print_ledger()
        else:
            for user in self.users.values():
                user.print_ledger()

    def get_user_name(self, user_id: int):
        if user_id in self.users:
            return self.users[user_id].name
        raise Exception("User does not exists")

    def get_user(self, user_id: int):
        if user_id in self.users:
            return self.users[user_id]
        raise Exception("User does not exists")


class ExpenseMetaData:
    spend_user: User
    users: List[User]
    totalAmount: float


class ExpenseStrategy(ABC):
    @abstractmethod
    def split_expense(self, expense_metadata: ExpenseMetaData) -> Dict[int, float]:
        pass


class EquallySplitExpenseStrategy(ExpenseStrategy):

    def split_expense(self, expense_metadata: ExpenseMetaData) -> Dict[int, float]:
        spender = expense_metadata.spend_user
        per_person_amount = expense_metadata.totalAmount / len(expense_metadata.users)

        expense_ledger = {
            spender.userId: expense_metadata.totalAmount - per_person_amount
        }

        for user in expense_metadata.users:
            if user != spender:
                expense_ledger.update({
                    user.userId: -1 * per_person_amount
                })

        return expense_ledger


class ExpenseManager(metaclass=Singleton):

    def __init__(self):
        self.user_manager = UserManager()

    def create_expense(self, expense_meta: ExpenseMetaData, strategy: ExpenseStrategy):
        expenses: Dict[int, float] = strategy.split_expense(expense_meta)
        spend_user = expense_meta.spend_user

        print("Expense:", expenses)

        for each_user, amount in expenses.items():
            user = self.user_manager.get_user(each_user)
            user.update_total_amount_owed(amount)

            if user != spend_user:
                user.update_ledger(spend_user.userId, amount)  # updating ledger of user
                spend_user.update_ledger(user.userId, -1 * amount)  # updating ledger of spender


user1 = User(1, "Prishita")
user2 = User(2, "Akash")
user3 = User(3, "Mayank")

split_equally = EquallySplitExpenseStrategy()

userManager = UserManager()
userManager.add_user(user1)
userManager.add_user(user2)
userManager.add_user(user3)

metaData = ExpenseMetaData()
metaData.spend_user = user1
metaData.users = [user1, user2]
metaData.totalAmount = 2000


manager = ExpenseManager()
manager.create_expense(metaData, split_equally)

userManager.print_ledger()

metaData = ExpenseMetaData()
metaData.spend_user = user2
metaData.users = [user1, user2]
metaData.totalAmount = 4000
#
#
manager.create_expense(metaData, split_equally)
userManager.print_ledger()
