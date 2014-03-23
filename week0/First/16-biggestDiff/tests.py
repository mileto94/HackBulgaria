import solution
import unittest

class TestBiggestDifference(unittest.TestCase):
    """docstring for TestBiggestDifference"""
    def test_1(self):
        self.assertEqual(-1, solution.biggest_difference([1,2]))

    def test_2(self):
        self.assertEqual(-4, solution.biggest_difference([1,2,3,4,5]))

    def test_3(self):
        self.assertEqual(-9, solution.biggest_difference([-10, -9, -1]))

    def test_4(self):
        self.assertEqual(-99, solution.biggest_difference(range(100)))

if __name__ == '__main__':
    unittest.main()
