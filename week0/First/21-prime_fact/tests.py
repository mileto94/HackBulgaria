import solution
import unittest

class TestPrimeFactorization(unittest.TestCase):
    """docstring for TestPrimeFactorization"""
    def test_1(self):
        self.assertEqual([(2, 1), (5, 1)], solution.prime_factorization(10))

    def test_2(self):
        self.assertEqual([(2, 1), (7, 1)], solution.prime_factorization(14))

    def test_3(self):
        self.assertEqual([(2, 2), (89, 1)], solution.prime_factorization(356))

    def test_4(self):
        self.assertEqual([(89, 1)], solution.prime_factorization(89))

    def test_5(self):
        self.assertEqual([(2, 3), (5, 3)], solution.prime_factorization(1000))

if __name__ == '__main__':
    unittest.main()
