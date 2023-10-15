class Balance:

    def __init__(self, user_manager):
        self.user_manager = user_manager

        self.expense_sheet = {}
        for i in range(0 , len(self.user_manager.users)):
            ui = self.user_manager.users[i]
            for j in range(i+1, len(self.user_manager.users)):
                uj = self.user_manager.users[j]
                self.expense_sheet[(ui, uj)] = 0

    def update_balance(self):
        pass

