import unittest
import game

class Weapon(unittest.TestCase):
    """docstring for Weapon"""
    def test__init__(self):
        axe = game.Weapon("Mighty Axe", 25, 0.2)
        self.assertEqual("Mighty Axe", axe.getType())
        #self.assertEqual(25, axe.attack(25))
        self.assertEqual(0.2, axe.getCriticalStrikePercent())

    def test_critical_hit(self):
        axe = game.Weapon("Mighty Axe", 25, 0.2)
        temporary = axe.critical_hit()
        self.assertTrue(temporary > 0 and temporary<2)


if __name__ == '__main__':
    unittest.main()
