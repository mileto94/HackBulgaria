import solution
import unittest

class TestIsMemberOfFibonacciList(unittest.TestCase):
    """docstring for TestIsMemberOfFibonacciList"""
    def test_1(self):
        self.assertEqual(False, solution.member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))

    def test_2(self):
        self.assertEqual(True, solution.member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))

    def test_3(self):
        self.assertEqual(True, solution.member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))

    def test_4(self):
        self.assertEqual(False, solution.member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))
if __name__ == '__main__':
    unittest.main()
