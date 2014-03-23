import solution
import unittest

class TestCountConsonants(unittest.TestCase):
    """docstring for TestCountConsonants"""
    def test_1(self):
        self.assertEqual(4, solution.count_consonants("Python"))

    def test_2(self):
        self.assertEqual(11, solution.count_consonants("Theistareykjarbunga"))

    def test_3(self):
        self.assertEqual(7, solution.count_consonants("grrrrgh!"))

    def test_4(self):
        self.assertEqual(44, solution.count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_5(self):
        self.assertEqual(6, solution.count_consonants("A nice day to code!"))

if __name__ == '__main__':
    unittest.main()
