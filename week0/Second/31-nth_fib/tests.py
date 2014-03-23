import solution
import unittest

class TestNthFibonacciLists(unittest.TestCase):
    """docstring for TestNthFibonacciLists"""
    def test_nth_fib_lists1(self):
        self.assertEqual([1], solution.nth_fib_lists([1], [2], 1))

    def test_nth_fib_lists2(self):
        self.assertEqual([2], solution.nth_fib_lists([1], [2], 2))

    def test_nth_fib_lists3(self):
        self.assertEqual([1, 2, 1, 3], solution.nth_fib_lists([1, 2], [1, 3], 3))
    def test_nth_fib_lists4(self):
        self.assertEqual([1, 2, 3, 1, 2, 3], solution.nth_fib_lists([], [1, 2, 3], 4))

    def test_nth_fib_lists5(self):
        self.assertEqual([], solution.nth_fib_lists([], [], 100))

if __name__ == '__main__':
    unittest.main()






