class User:
    def __init__(self, id, name, email, mob):
        self.id = id
        self.name = name
        self.email = email
        self.mob = mob


class UserManager:

    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    @property
    def total_user(self):
        return len(self.users)