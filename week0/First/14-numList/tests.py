import solution
import unittest

class TestNumberToList(unittest.TestCase):
    """docstring for TestNumberToList"""
    def test_1(self):
        self.assertEqual([1, 2, 3], solution.number_to_list(123))

    def test_2(self):
        self.assertEqual([9, 9, 9, 9, 9], solution.number_to_list(99999))

    def test_3(self):
        self.assertEqual([1, 2, 3, 0, 2, 3], solution.number_to_list(123023))

if __name__ == '__main__':
    unittest.main()

