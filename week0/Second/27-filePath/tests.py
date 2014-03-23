import solution
import unittest

class TestSolution_for_file_path(unittest.TestCase):
    """docstring for TestSolution_for_file_path"""
    def test_1(self):
        new_path = "/"
        self.assertEqual("/", solution.reduce_file_path(new_path))

    def test_2(self):
        new_path = "/srv/../"
        self.assertEqual("/", solution.reduce_file_path(new_path))

    def test_3(self):
        new_path = "/srv/www/htdocs/wtf/"
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path(new_path))

    def test_4(self):
        new_path = "/srv/www/htdocs/wtf"
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path(new_path))

    def test_5(self):
        new_path = "/srv/./././././"
        self.assertEqual("/srv", solution.reduce_file_path(new_path))

    def test_6(self):
        new_path = "/etc//wtf/"
        self.assertEqual("/etc/wtf", solution.reduce_file_path(new_path))

    def test_7(self):
        new_path = "/etc/../etc/../etc/../"
        self.assertEqual("/", solution.reduce_file_path(new_path))

    def test_8(self):
        new_path = "//////////////"
        self.assertEqual("/", solution.reduce_file_path(new_path))

    def test_9(self):
        new_path = "/../"
        self.assertEqual("/", solution.reduce_file_path(new_path))

    def test_10(self):
        new_path = "/home//radorado/code/./hackbulgaria/week0/../"
        self.assertEqual("/home/radorado/code/hackbulgaria", solution.reduce_file_path(new_path))

if __name__ == '__main__':
    unittest.main()
