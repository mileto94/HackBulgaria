import game
import unittest

class TestEntity(unittest.TestCase):
    """docstring for TestEntity"""
    def test__init__(self):
        new_entity = game.Entity("Bron", 100)
        self.assertEqual("Bron", new_entity.get_name())
        self.assertEqual(True, new_entity.is_alive())

    def test_health(self):
        new_entity = game.Entity("Bron", 45)
        self.assertEqual(True, new_entity.is_alive())

    def test_health(self):
        new_entity = game.Entity("Bron", 45)
        self.assertEqual(True, new_entity.is_alive())

    def  test_take_damage(self):
        new_entity = game.Entity("Bron", 100)
        self.assertEqual(79, new_entity.take_damage(21))

    def test_take_healing(self):
        new_entity = game.Entity("Bron", 100)
        new_entity.take_healing(23)
        self.assertEqual(True, new_entity.is_alive())

    def test_take_healing_unsuccessful(self):
        new_entity = game.Entity("Bron", 0)
        new_entity.take_healing(34)
        self.assertEqual(False, new_entity.is_alive())

    def test_take_healing_successful(self):
        new_entity = game.Entity("Bron", 34)
        new_entity.take_healing(26)
        self.assertEqual(True, new_entity.is_alive())

    def test_take_healing_unsuccessful_minus(self):
        new_entity = game.Entity("Bron", -4)
        new_entity.take_healing( 34)
        self.assertEqual(False, new_entity.is_alive())

    def test_equip_weapon(self):
        new_entity = game.Entity("Hobit", 34)
        weapon = game.Weapon("Axe", 34, 56)
        new_entity.equip_weapon(weapon)
        self.assertEqual(True, new_entity.has_weapon())


    def test_attack(self):
        new_entity = game.Entity("Hobit", 56)
        self.assertEqual(0, new_entity.attack())



if __name__ == '__main__':
    unittest.main()

