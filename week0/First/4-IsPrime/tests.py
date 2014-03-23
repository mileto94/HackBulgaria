import solution
import unittest

class TestIsPrime(unittest.TestCase):
    """docstring for TestSumOfDigits"""
    def test_1(self):
        self.assertEqual(False, solution.is_prime(1))

    def test_2(self):
        self.assertEqual(True, solution.is_prime(2))

    def test_3(self):
        self.assertEqual(False, solution.is_prime(8))

    def test_4(self):
        self.assertEqual(True, solution.is_prime(11))

    def test_5(self):
        self.assertEqual(False, solution.is_prime(-10))

if __name__ == '__main__':
    unittest.main()
