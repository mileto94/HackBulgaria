import solution
import unittest

class TestCountVowels(unittest.TestCase):
    """docstring for TestCountVowels"""
    def test_1(self):
        self.assertEqual(2, solution.count_vowels("Python"))

    def test_2(self):
        self.assertEqual(8, solution.count_vowels("Theistareykjarbunga"))

    def test_3(self):
        self.assertEqual(0, solution.count_vowels("grrrrgh!"))

    def test_4(self):
        self.assertEqual(22, solution.count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_5(self):
        self.assertEqual(8, solution.count_vowels("A nice day to code!"))

if __name__ == '__main__':
    unittest.main()
