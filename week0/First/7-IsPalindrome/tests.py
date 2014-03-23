import solution
import unittest

class TestIsIntPalindrome(unittest.TestCase):
    """docstring for TestIsIntPalindrome"""
    def test_1(self):
        self.assertEqual(True, solution.is_int_palindrome(1))

    def test_2(self):
        self.assertEqual(False, solution.is_int_palindrome(42))

    def test_3(self):
        self.assertEqual(True, solution.is_int_palindrome(100001))

    def test_4(self):
        self.assertEqual(True, solution.is_int_palindrome(999))

    def test_5(self):
        self.assertEqual(False, solution.is_int_palindrome(123))

if __name__ == '__main__':
    unittest.main()
