import solution
import unittest

class TestSumDivisors(unittest.TestCase):
    """docstring for TestSumOfDigits"""
    def test_1(self):
        self.assertEqual(15, solution.sum_of_divisors(8))

    def test_2(self):
        self.assertEqual(8, solution.sum_of_divisors(7))

    def test_3(self):
        self.assertEqual(1, solution.sum_of_divisors(1))

    def test_4(self):
        self.assertEqual(2340, solution.sum_of_divisors(1000))

if __name__ == '__main__':
    unittest.main()
