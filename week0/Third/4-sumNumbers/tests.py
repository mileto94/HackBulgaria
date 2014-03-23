import unittest
import solution
import sys


class TestSumNumbersFromFile(unittest.TestCase):
    """docstring for TestSumNumbersFromFile"""
    def test_sum_numbers_1(self):
        sys.argv.append("FMI.txt")
        file_to_read = sys.argv[1]
        file_read = open(file_to_read, "r")
        content = file_read.read().split(" ")
        numbers = map(int, content)
        file_read.close()
        self.assertEqual(sum(numbers), solution.sum_numbers(file_to_read))

    def test_sum_numbers_2(self):
        sys.argv.append("number.txt")
        file_to_read = sys.argv[1]
        file_read = open(file_to_read, "r")
        content = file_read.read().split(" ")
        numbers = map(int, content)
        file_read.close()
        self.assertEqual(sum(numbers), solution.sum_numbers(file_to_read))

if __name__ == '__main__':
    unittest.main()
