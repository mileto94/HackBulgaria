import solution
import unittest

class TestStringInString(unittest.TestCase):
    """docstring for TestStringInString"""
    def test_1(self):
        self.assertEqual(2, solution.count_substrings("This is a test string", "is"))

    def test_2(self):
        self.assertEqual(2, solution.count_substrings("babababa", "baba"))

    def test_3(self):
        self.assertEqual(4, solution.count_substrings("Python is an awesome language to program in!", "o"))

    def test_4(self):
        self.assertEqual(0, solution.count_substrings("We have nothing in common!", "really?"))

    def test_5(self):
        self.assertEqual(2, solution.count_substrings("This is this and that is this", "this"))

if __name__ == '__main__':
    unittest.main()
