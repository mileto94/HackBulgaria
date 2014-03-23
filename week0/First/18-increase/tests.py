import solution
import unittest

class TestIsIncreasing(unittest.TestCase):
    """docstring for TestIsIncreasing"""
    def test_1(self):
        self.assertEqual(True, solution.is_increasing([1,2,3,4,5]))

    def test_2(self):
        self.assertEqual(True, solution.is_increasing([1]))

    def test_3(self):
        self.assertEqual(False, solution.is_increasing([5,6,-10]))

    def test_4(self):
        self.assertEqual(False, solution.is_increasing([1,1,1,1]))

if __name__ == '__main__':
    unittest.main()
