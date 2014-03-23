import solution
import unittest

class TestSigns(unittest.TestCase):
    """docstring for TestSigns"""
    def test_1(self):
        self.assertEqual("Leo", solution.what_is_my_sign(5,8))

    def test_2(self):
        self.assertEqual("Aquarius", solution.what_is_my_sign(29,1))

    def test_3(self):
        self.assertEqual("Cancer", solution.what_is_my_sign(30,6))

    def test_4(self):
        self.assertEqual("Gemini", solution.what_is_my_sign(31,5))

    def test_5(self):
        self.assertEqual("Aquarius", solution.what_is_my_sign(2,2))

    def test_6(self):
        self.assertEqual("Taurus", solution.what_is_my_sign(8,5))

    def test_7(self):
        self.assertEqual("Taurus", solution.what_is_my_sign(8,5))

if __name__ == '__main__':
    unittest.main()
