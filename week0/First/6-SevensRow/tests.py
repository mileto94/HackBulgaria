import solution
import unittest

class TestSevensIvRow(unittest.TestCase):
    """docstring for TestSevensIvRow"""
    def test_1(self):
        self.assertEqual(True, solution.sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))

    def test_2(self):
        self.assertEqual(False, solution.sevens_in_a_row([1,7,1,7,7], 4))

    def test_3(self):
        self.assertEqual(True, solution.sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
    def test_4(self):
        self.assertEqual(True, solution.sevens_in_a_row([7,2,1,6,2], 1))

if __name__ == '__main__':
    unittest.main()
