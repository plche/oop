class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def show_account_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def make_transfer(self, user, amount):
        user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self