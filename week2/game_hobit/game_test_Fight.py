import game
import unittest

class TestFight(unittest.TestCase):
    """docstring for Fight"""
    def test_who_starts(self):
        new_hero = game.Hero("Brus Wayne", 100, "Batman")
        new_orc = game.Orc("The Jocker", 100, 0.9)
        new_fight = game.Fight(new_hero, new_orc)

        who_start = new_fight.who_starts()

        self.assertTrue(isinstance(who_start, game.Hero) or isinstance(who_start, game.Orc))

    def test_simulate_fight(self):
        new_hero = game.Hero("Brus Wayne", 100, "Batman")
        new_orc = game.Orc("The Jocker", 100, 0.9)
        new_weapon = game.Weapon("Mighty Axe", 25, 0.2)
        rifle = game.Weapon("rifle", 56, 0.7)
        new_hero.equip_weapon(new_weapon)
        new_orc.equip_weapon(rifle)
        new_fight = game.Fight(new_hero, new_orc)
        who_start = new_fight.who_starts()
        opponent = new_fight.get_opponent(who_start)
        self.assertTrue(isinstance(opponent, game.Hero) or isinstance(opponent, game.Orc))
        survived = new_fight.simulate_fight()
        self.assertTrue(isinstance(survived, game.Hero) or isinstance(survived, game.Orc))

    def test_simulate_one_weapon_fight(self):
        new_hero = game.Hero("Brus Wayne", 100, "Batman")
        new_orc = game.Orc("The Jocker", 100, 0.9)
        new_weapon = game.Weapon("Mighty Axe", 25, 0.2)
        new_hero.equip_weapon(new_weapon)
        new_fight = game.Fight(new_hero, new_orc)
        who_start = new_fight.who_starts()
        opponent = new_fight.get_opponent(who_start)
        self.assertTrue(isinstance(opponent, game.Hero) or isinstance(opponent, game.Orc))
        survived = new_fight.simulate_fight()
        self.assertTrue(isinstance(survived, game.Hero) or isinstance(survived, game.Orc))

    def test_simulate_no_weapon_fight(self):
        new_hero = game.Hero("Oliver ", 100, "Stone Cold")
        new_orc = game.Orc("Harry Finn", 100, 0.9)
        new_fight = game.Fight(new_hero, new_orc)
        who_start = new_fight.who_starts()
        opponent = new_fight.get_opponent(who_start)
        self.assertTrue(isinstance(opponent, game.Hero) or isinstance(opponent, game.Orc))
        survived = new_fight.simulate_fight()
        self.assertTrue(isinstance(survived, game.Hero) or isinstance(survived, game.Orc))

if __name__ == '__main__':
    unittest.main()

