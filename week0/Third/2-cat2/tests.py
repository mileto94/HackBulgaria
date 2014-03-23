import solution
import unittest
import sys


class TestReadFile(unittest.TestCase):
    """docstring for TestReadFile"""
    def test_with_two_files(self):
        sys.argv.append("file.txt")
        sys.argv.append("file2.txt")
        for index in range(1, len(sys.argv)):
            file_to_read = sys.argv[index]
            file_text = open(file_to_read, "r")
            content = file_text.read() + "\n"
            file_text.close()
            self.assertEqual(content, solution.cat2(file_to_read))

    def test_with_three_files(self):
        sys.argv.append("file.txt")
        sys.argv.append("file2.txt")
        sys.argv.append("file3.txt")
        for index in range(1, len(sys.argv)):
            file_to_read = sys.argv[index]
            file_text = open(file_to_read, "r")
            content = file_text.read() + "\n"
            file_text.close()
            self.assertEqual(content, solution.cat2(file_to_read))

if __name__ == '__main__':
    unittest.main()
