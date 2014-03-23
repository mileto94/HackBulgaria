import unittest
import solution
import sys


class TestWordCounter(unittest.TestCase):
    """docstring for TestWordCounter"""
    def test_count_characters(self):
        sys.argv.append("chars")
        sys.argv.append("story.txt")
        command = sys.argv[1]
        file_to_open = sys.argv[2]
        file_open = open(file_to_open, "r")
        contents = file_open.read()
        expect = len(contents)
        self.assertEqual(expect, solution.count_characters(file_to_open))
        file_open.close()

    def test_count_words(self):
        sys.argv.append("words")
        sys.argv.append("story")
        command = sys.argv[1]
        file_to_open = sys.argv[2]
        file_open = open(file_to_open, "r")
        contents = file_open.read().split(" ")
        expect = len(contents) + 2
        self.assertEqual(expect, solution.count_words(file_to_open))
        file_open.close()

    def test_count_lines(self):
        sys.argv.append("lines")
        sys.argv.append("story.txt")
        command = sys.argv[1]
        file_to_open = sys.argv[2]
        file_open = open(file_to_open, "r")
        contents = file_open.read().split("\n")
        expect = len(contents)
        self.assertEqual(expect, solution.count_lines(file_to_open))
        file_open.close()

if __name__ == '__main__':
    unittest.main()
