import unittest
import solution


class TestMagicString(unittest.TestCase):
    """docstring for TestMagicString"""
    def test_magic_string_1(self):
        self.assertEqual(2, solution.magic_string(">><<><"))

    def test_magic_string_2(self):
        self.assertEqual(0, solution.magic_string(">>>><<<<"))

    def test_magic_string_3(self):
        self.assertEqual(4, solution.magic_string("<<>>"))

    def test_magic_string_4(self):
        self.assertEqual(20, solution.magic_string("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))

if __name__ == '__main__':
    unittest.main()
