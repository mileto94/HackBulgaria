import unittest
import solution


class TestDevisionByZero(unittest.TestCase):
    """docstring for TestDevisionByZero"""
    def test_division_by_zero_1(self):
        self.assertEqual(3, solution.count_numbers([9, 2]))

    def test_division_by_zero_2(self):
        self.assertEqual(3, solution.count_numbers([8, 2]))

    def test_division_by_zero_3(self):
        self.assertEqual(1, solution.count_numbers([50]), 1)

    def test_division_by_zero_4(self):
        self.assertEqual(11, solution.count_numbers([1, 5, 8, 30, 15, 4]))

    def test_division_by_zero_5(self):
        self.assertEqual(7, solution.count_numbers([1, 2, 4, 8, 16, 32, 64]))

    def test_division_by_zero_6(self):
        self.assertEqual(7, solution.count_numbers([6, 2, 18]))

    def test_division_by_zero_7(self):
        self.assertEqual(10, solution.count_numbers([5, 3, 28, 6, 7]))


if __name__ == '__main__':
    unittest.main()
