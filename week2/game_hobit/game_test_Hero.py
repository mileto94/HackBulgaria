import unittest
import game

class TestHero(unittest.TestCase):
    """docstring fo TestHero"""
    def test__init__hero(self):
        new_hero = game.Hero("Bron", 56, "DragonSlayer")
        self.assertEqual("Bron", new_hero.get_name())
        self.assertEqual(True, new_hero.is_alive())
        self.assertEqual("Bron the DragonSlayer", new_hero.known_as())

    def test_known_as_hero(self):
        new_hero = game.Hero("Bron", 100, "DragonSlayer")
        self.assertEqual("Bron the DragonSlayer", new_hero.known_as())

    def test_nickname_hero(self):
        new_hero = game.Hero("Bron", 14, "DragonSlayer")
        self.assertEqual("DragonSlayer", new_hero.get_nickname())

if __name__ == '__main__':
    unittest.main()
