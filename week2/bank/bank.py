class BankAccount():
    """docstring for BankAccount"""
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def deposit_money(self, money_to_deposit):
        if money_to_deposit <= 0:
            return False
        else:
            self.balance += money_to_deposit
            return True

    def withdraw(self, withdraw_money):
        if self.balance > withdraw_money:
            self.balance -= withdraw_money
            return True
        else:
            return False
