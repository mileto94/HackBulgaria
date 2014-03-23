import solution
import unittest
import sys


class TestConcatFiles(unittest.TestCase):
    """docstring for TestConcatFiles"""
    def test_concat_two_files(self):
        sys.argv.append("file.txt")
        sys.argv.append("file2.txt")
        file_to_write = "MEGATRON.txt"
        arr_content = []
        file_write = open(file_to_write, "w")
        for index in range(1, len(sys.argv)):
            file_name = sys.argv[index]
            file_read = open(file_name, "r")
            content = file_read.read()
            arr_content.append(content)
            file_write.write(content)
            file_read.close()
            expect = "\n".join(arr_content)
        self.assertEqual(expect, solution.concat_files(file_read))
        file_write.close()

    def test_concat_three_files(self):
        sys.argv.append("file.txt")
        sys.argv.append("file2.txt")
        sys.argv.append("file3.txt")
        file_to_write = "MEGATRON.txt"
        arr_content = []
        file_write = open(file_to_write, "w")
        for index in range(1, len(sys.argv)):
            file_name = sys.argv[index]
            file_read = open(file_name, "r")
            content = file_read.read()
            arr_content.append(content)
            file_write.write(content)
            file_read.close()
            expect = "\n".join(arr_content)
        self.assertEqual(expect, solution.concat_files(file_read))
        file_write.close()


if __name__ == '__main__':
    unittest.main()
