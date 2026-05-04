# bank_account.py
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return -1  # Fondos insuficientes
        else:
            self.balance -= amount
            return 0   # Retiro exitoso

    def __str__(self):
        acc_str = str(self.account_number)
        return f"Account Number: **{acc_str[-2:]}\nCurrent Balance: {self.balance:.2f}"