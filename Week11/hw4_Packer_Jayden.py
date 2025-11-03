class bankAccount:
    def __init__ (self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance