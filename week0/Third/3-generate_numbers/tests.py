import solution
import unittest
import sys


class TestGenerateFileWithRandomNumbers(unittest.TestCase):
    """docstring for TestGenerateFileWithNumbers"""
    def test_generate_file_with_random_numbers(self):
        sys.argv.append("FMI.txt")
        sys.argv.append(100)
        file_to_write = sys.argv[1]
        number = int(sys.argv[2])
        file_write = open(file_to_write, "w")
        expect = str(solution.generate_numbers(file_to_write, number))
        file_write.write(expect)
        file_write.close()
        file_read = file_to_write
        file_read = open(file_to_write, "r")
        content = file_read.read()
        file_read.close()
        self.assertEqual(content, expect)

if __name__ == '__main__':
    unittest.main()
