class bankAccount:
    def __init__ (self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    @property
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account Number: {self.account_number}, Owner: {self.owner}, Balance: {self.balance}"

class savingsAccount(bankAccount):
    def __init__(self, account_number, owner, initial_balance, interest_rate):
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance: {self.balance}")
        return interest

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif self.balance - amount < 100:
            print("Cannot withdraw: minimum balance of 100 must be maintained!")
        else:
            return super().withdraw(amount)

    def __str__(self):
        return f"Savings {super().__str__()}, Interest Rate: {self.interest_rate}"
    

if __name__ == "__main__":
    # Regular account
    regular = bankAccount("1001", "Alice", 500)
    print(regular)
    regular.deposit(100)
    print(f"After deposit: ${regular.balance}")
    regular.withdraw(200)
    print(f"After withdrawal: ${regular.balance}")
    print("\n" + "="*40 + "\n")
    # Savings account
    savings = savingsAccount("2001", "Bob", 1000, 0.02)
    print(savings)
    interest = savings.apply_interest()
    print(f"Interest earned: ${interest:.2f}")
    print(f"New balance: ${savings.balance}")
    # Try to go below minimum
    savings.withdraw(950) # Should fail
    savings.withdraw(500) # Should work
    print(f"Final balance: ${savings.balance}")