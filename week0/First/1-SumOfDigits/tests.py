import solution
import unittest

class TestSumOfDigits(unittest.TestCase):
    """docstring for TestSumOfDigits"""
    def test_1(self):
        self.assertEqual(43, solution.sum_of_digits(1325132435356))

    def test_2(self):
        self.assertEqual(6, solution.sum_of_digits(123))

    def test_3(self):
        self.assertEqual(6, solution.sum_of_digits(6))

    def test_4(self):
        self.assertEqual(1, solution.sum_of_digits(-10))

if __name__ == '__main__':
    unittest.main()
