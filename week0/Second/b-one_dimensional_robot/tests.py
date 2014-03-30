import unittest
import solution


class TestOneDimensionalRobot(unittest.TestCase):
    """docstring for TestOneDimensionalRobot"""
    def test_final_position_1(self):
        self.assertEqual(2, solution.final_position("RRLRRLLR", 10, 10))

    def test_final_position_2(self):
        self.assertEqual(4, solution.final_position("RRRRR", 3, 4))

    def test_final_position_3(self):
        self.assertEqual(-1, solution.final_position("LLLLLLLLLLR", 2, 6))

    def test_final_position_4(self):
        self.assertEqual(20, solution.final_position(
            "RRRRRRRLRRLRRRRRRRRRRRRLRLRRRRRRRRLRRRRRLRRRRRRRRR", 5, 20))

    def test_final_position_5(self):
        self.assertEqual(-30, solution.final_position("RLRLLLLLLLRLLLRLLLLLLLLRLLLLLRLLLRRLLLLLRLLLLLRLLL", 34, 15))

    def test_final_position_6(self):
        self.assertEqual(6, solution.final_position("RRRLLLRLRLRLLLRRRRRRRR", 32, 21))

if __name__ == '__main__':
    unittest.main()
