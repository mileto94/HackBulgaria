import unittest
import solution
import sys


class TestReadFromFile(unittest.TestCase):
    """docstring for TestReadFromFile"""
    def test_read_from_file_Megatron(self):
        sys.argv.append("MEGATRON.txt")
        file_to_read = sys.argv[1]
        file_read = open(file_to_read, "r")
        content = file_read.read()
        self.assertEqual(content, solution.read_from_file(file_to_read))
        file_read.close()

    def test_read_from_file(self):
        sys.argv.append("file.txt")
        file_to_read = sys.argv[1]
        file_read = open(file_to_read, "r")
        content = file_read.read()
        file_read.close()
        self.assertEqual(content, solution.read_from_file(file_to_read))


if __name__ == '__main__':
    unittest.main()
