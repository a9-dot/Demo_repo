class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 0.0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds for withdrawal")
        elif amount > 0:
            self.__balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive")

    def get_balance(self):
        return self.__balance

# Example usage
account = BankAccount("John Doe")
account.deposit(100)
print(account.get_balance())  # Output: 100
account.withdraw(50)
print(account.get_balance())  # Output: 50

