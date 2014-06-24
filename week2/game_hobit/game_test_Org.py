import unittest
import game

class TestOrc(unittest.TestCase):
    """docstring for TestOrc"""
    def test__init__(self):
        new_orc = game.Orc("Bron", 45, 0.2)
        new_weapon = game.Weapon("gun", 34, 67)
        self.assertEqual(0, new_orc.attack())



if __name__ == '__main__':
    unittest.main()
