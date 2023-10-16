"""

Transactions:

Action      Amount  Request timestamp       Status

"Deposit",  1000,   "13/05/2022 12:00:00",  "Success"

"Deposit",  500,    "18/05/2022 13:15:00",  "Success"

"Withdraw", 700,    "20/05/2022 08:30:00",  "Success"

"Withdraw", 1000,   "20/05/2022 09:00:00",  "Error – Insufficient Funds"



Balance requests:

Requested timestamp     Balance

"14/05/2022 00:00:00",  1000

"18/05/2022 13:30:00",  1500

"20/05/2022 08:45:00",  800

"20/05/2022 09:15:00",  800


--
testcases
Withdrawl  -> 0 balance
Deposit/Withdrawl -> before last trasaction has happened [not allowed]
withdrawl  -> balance < amount requested [not allowed]
deposite/ withdraw -> -ve is [not allowed]
balance timeframe is correct -> valid output
future time for balance
"""

import unittest
from code2 import Bank


class TestBank(unittest.TestCase):

    def test_withdrawl(self):
        bank = Bank()

        bank.deposite(1000, "13/05/2022 12:00:00")
        bank.deposite(500, "18/05/2022 13:15:00")
        bank.withdrawl(700, "20/05/2022 08:30:00")
        status = bank.withdrawl(1000, "20/05/2022 09:00:00")
        self.assertEqual("Error – Insufficient Funds", status)

    def test_balance(self):
        bank = Bank()

        bank.deposite(1000, "13/05/2022 12:00:00")
        bank.deposite(500, "18/05/2022 13:15:00")
        bank.withdrawl(700, "20/05/2022 08:30:00")
        bank.withdrawl(1000, "20/05/2022 09:00:00")

        balance = bank.getbalance("14/05/2022 00:00:00")
        balance1 = bank.getbalance("18/05/2022 13:30:00")
        balance3 = bank.getbalance("20/05/2022 08:45:00")
        balance4 = bank.getbalance("20/05/2022 09:15:00")

        self.assertEqual(1000, balance)
        self.assertEqual(1500, balance1)
        self.assertEqual(800, balance3)
        self.assertEqual(800, balance4)

