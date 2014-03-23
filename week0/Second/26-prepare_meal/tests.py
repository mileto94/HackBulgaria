import solution
import unittest

class TestPrepareMeal(unittest.TestCase):
    """docstring for TestPrepareMeal"""
    def test_prepare_meal_with_5(self):
        self.assertEqual("eggs", solution.prepare_meal(5))

    def test_prepare_meal_with_3(self):
        self.assertEqual("spam", solution.prepare_meal(3))

    def test_prepare_meal_with_27(self):
        self.assertEqual("spam spam spam", solution.prepare_meal(27))

    def test_prepare_meal_with_15(self):
        self.assertEqual("spam and eggs", solution.prepare_meal(15))

    def test_prepare_meal_with_45(self):
        self.assertEqual("spam spam and eggs", solution.prepare_meal(45))

    def test_prepare_meal_with_7(self):
        self.assertEqual("", solution.prepare_meal(7))

if __name__ == '__main__':
    unittest.main()
