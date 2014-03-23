import solution
import unittest

class TestSolution(unittest.TestCase):
    """docstring for TestSolution"""
    def test_1(self):
        self.assertEqual(False, solution.contains_digit(123, 4))

    def test_2(self):
        self.assertEqual(True, solution.contains_digit(42, 2))

    def test_3(self):
        self.assertEqual(True, solution.contains_digit(1000, 0))

    def test_4(self):
        self.assertEqual(False, solution.contains_digit(12346789, 5))

if __name__ == '__main__':
    unittest.main()
