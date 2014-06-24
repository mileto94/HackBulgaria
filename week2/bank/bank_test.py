import bank
import unittest

class BankAccountTest(unittest.TestCase):
    """docstring for BankAccountTest"""
    def setUp(self):
        self.new_bank_account = bank.BankAccount()

    def test__init__new_bank_account(self):
        self.assertEqual(0, self.new_bank_account.get_balance())


    def test_deposit_money(self):
        self.new_bank_account.deposit_money(34)
        self.assertEqual(34, self.new_bank_account.get_balance())

    def test_invalid_deposit_with_minus_deposit_and_empty_account(self):
        self.new_bank_account.deposit_money(-45436536)
        self.assertEqual(0, self.new_bank_account.get_balance())

    def test_withdraw(self):
        self.new_bank_account.deposit_money(50)
        self.new_bank_account.withdraw(30)
        self.assertEqual(20, self.new_bank_account.get_balance())

    def test_empty_bank_account(self):
        self.assertEqual(0, self.new_bank_account.get_balance())


if __name__ == '__main__':
    unittest.main()
