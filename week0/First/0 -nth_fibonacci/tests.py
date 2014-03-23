import solution
import unittest

class TestNthFibonacci(unittest.TestCase):
    """docstring for TestNthFibonacci"""
    def test_nth_fibonacci1(self):
        self.assertEqual(1, solution.nth_fibonacci(1))

    def test_nth_fibonacci2(self):
        self.assertEqual(1, solution.nth_fibonacci(2))

    def test_nth_fibonacci3(self):
        self.assertEqual(2, solution.nth_fibonacci(3))

    def test_nth_fibonacci4(self):
        self.assertEqual(55, solution.nth_fibonacci(10))

if __name__ == '__main__':
    unittest.main()
