import solution
import unittest

class TestIsDecreasing(unittest.TestCase):
    """docstring for TestIsDecreasing"""
    def test_1(self):
        self.assertEqual(True, solution.is_decreasing([5,4,3,2,1]))

    def test_2(self):
        self.assertEqual(False, solution.is_decreasing([1,2,3]))

    def test_3(self):
        self.assertEqual(True, solution.is_decreasing([100, 50, 20]))

    def test_4(self):
        self.assertEqual(False, solution.is_decreasing([1,1,1,1]))

if __name__ == '__main__':
    unittest.main()
