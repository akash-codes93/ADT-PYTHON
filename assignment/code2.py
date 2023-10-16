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



"""
import datetime


class Bank:

    def __init__(self):
        self.ledger = []
        self.balance = 0
        self.last_transaction_timestamp = None

    def deposite(self, amount: int, timestamp: str) -> str:

        timestamp = datetime.datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S')

        if not self.last_transaction_timestamp:
            self.last_transaction_timestamp = timestamp
        elif timestamp < self.last_transaction_timestamp:
            return "Not a valid timestamp"
        else:
            self.last_transaction_timestamp = timestamp

        if amount < 0:
            return "Not a valid amount"

        self.balance += amount
        self.ledger.append(
            [timestamp, self.balance]
        )
        return "Success"

    def withdrawl(self, amount: int, timestamp) -> str:
        timestamp = datetime.datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S')

        if not self.last_transaction_timestamp:
            self.last_transaction_timestamp = timestamp
        elif timestamp < self.last_transaction_timestamp:
            return "Not a valid timestamp"
        else:
            self.last_transaction_timestamp = timestamp

        if amount < 0:
            return "Not a valid amount"

        balance = self.balance - amount
        if balance < 0:
            return "Error – Insufficient Funds"

        self.balance = balance
        self.ledger.append(
            [timestamp, self.balance]
        )
        return "Success"

    def getbalance(self, timestamp) -> int:
        timestamp = datetime.datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S')

        if len(self.ledger) == 0:
            return 0

        for index, (ledger_timestamp, balance) in enumerate(self.ledger):
            if timestamp <= ledger_timestamp:
                if index > 0:
                    return self.ledger[index-1][1]

        if len(self.ledger) > 0:
            return self.ledger[-1][1]
        return 0








