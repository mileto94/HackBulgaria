from deal_with_file import DealWithFiles
import unittest
from time import time
from datetime import datetime
import glob


class TestDealWithFiles(unittest.TestCase):
    """docstring for TestDealWithFiles"""
    def setUp(self):
        self.order = DealWithFiles([("Alex", 4.56), ("Marty", 5.33), ("Gloria", 6.19), ("Melmon", 7.34)])

    def test_save_into_files(self):
        ts = time()
        filename = "orders_" + datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        content = self.order.save(filename)
        file_check = open(filename, "r")
        file_read = file_check.read()
        file_check.close()
        self.assertEqual(file_read, content)

    def test_show_lists_with_id(self):
        files = glob.glob("orders_*")
        expect = ""
        for index in range(len(files)):
            expect += "[" + str(index + 1) + "] - " + files[index]
            if index != len(files) - 1:
                expect += "\n"
        self.assertEqual(expect, self.order.show_lists_with_id())

    def test_load_content_from_file(self):
        files = glob.glob("orders_*")
        filename = files[2]
        file_read = open(filename, "r")
        file_content = file_read.read()
        file_read.close()
        self.assertEqual(file_content, self.order.print_status())

#True == True
    def test_load_data_from_file(self):
        files = glob.glob("orders_*")
        filename = files[1]
        file_read = open(filename, "r")
        file_content = file_read.read().split("\n")
        file_read.close()
        temp_expect = "\n".join(file_content)
        temp_expect = temp_expect.replace(" - ", " ")
        test = temp_expect.split("\n")
        expect = []
        for file in test:
            for item in range(len(file)):
                if file[item] == " ":
                    expect.append((file[:item], file[item + 1:]))
        self.assertEqual(expect, self.order.load_data(filename))


if __name__ == '__main__':
    unittest.main()
