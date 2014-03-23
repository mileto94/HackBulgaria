import solution
import unittest

class TestCountUniqueWords(unittest.TestCase):
    """docstring for TestCountUniqueWords"""
    def test_count_unique_words1(self):
        self.assertEqual(3, solution.unique_words_count(["apple", "banana", "apple", "pie"]))

    def test_count_unique2(self):
        self.assertEqual(2, solution.unique_words_count(["python", "python", "python", "ruby"]))

    def test_unique_words_count(self):
        self.assertEqual(1, solution.unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    unittest.main()
