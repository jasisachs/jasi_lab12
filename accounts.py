class Account:
    MINIMUM = 100  # Class variable
    RATE = 0.02  # Class variable

    def __init__(self, name, balance=0):
        self.set_name(name)
        self.set_balance(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= Account.MINIMUM:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def set_balance(self, value):
        if value < 0:
            self.balance = 0
        else:
            self.balance = value

    def set_name(self, value):
        self.name = value

    def __str__(self):
        return f"Account name: {self.get_name()}, Balance: ${self.get_balance()}"


class SavingsAccount(Account):
    def __init__(self, name):
        super().__init__(name, balance=Account.MINIMUM)
        self.deposit_count = 0

    def apply_interest(self):
        if self.deposit_count % 5 == 0:
            interest = self.get_balance() * Account.RATE
            self.deposit(interest)

    def deposit(self, amount):
        if super().deposit(amount):
            self.deposit_count += 1
            self.apply_interest()
            return True
        return False

    def withdraw(self, amount):
        if super().withdraw(amount):
            self.apply_interest()
            return True
        return False

    def __str__(self):
        return f"Savings Account name: {self.get_name()}, Balance: ${self.get_balance()}, Deposit Count: {self.deposit_count}"


if __name__ == "__main__":
    account1 = Account("John Doe", 100)
    print(account1)

    savings_account = SavingsAccount("Jane Smith")
    print(savings_account)

    savings_account.deposit(100)
    print(savings_account)

    savings_account.deposit(100)
    print(savings_account)

    savings_account.deposit(100)
    print(savings_account)

    savings_account.deposit(100)
    print(savings_account)

    savings_account.deposit(100)
    print(savings_account)

    savings_account.withdraw(50)
    print(savings_account)
