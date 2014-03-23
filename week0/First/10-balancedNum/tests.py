import solution
import unittest

class TestIsNumberBalanced(unittest.TestCase):
    """docstring for TestIsNumberBalanced"""
    def test_1(self):
        self.assertEqual(True, solution.is_number_balanced(9))

    def test_2(self):
        self.assertEqual(True, solution.is_number_balanced(11))

    def test_3(self):
        self.assertEqual(False, solution.is_number_balanced(13))

    def test_4(self):
        self.assertEqual(True, solution.is_number_balanced(121))

    def test_5(self):
        self.assertEqual(True, solution.is_number_balanced(4518))

    def test_6(self):
        self.assertEqual(False, solution.is_number_balanced(28471))

    def test_7(self):
        self.assertEqual(True, solution.is_number_balanced(1238033))

if __name__ == '__main__':
    unittest.main()
