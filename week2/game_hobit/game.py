import random
from random import randint


class Entity():
    """docstring for Entity"""
    def __init__(self,name, health):
        self.name = name
        self.health = health

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def equip_weapon(self, weapon_for_entity):
        setattr(self, "weapon", weapon_for_entity)
        return True

    def has_weapon(self):
        return hasattr(self, "weapon")

    def take_damage(self, damage_points):
        self.health -= damage_points
        return self.health

    def take_healing(self, healing_points):
        if self.health > 0 and self.health < 100:
            self.health += healing_points
        return self.health

    def attack(self):
        if self.has_weapon():
            return self.weapon.damage
        else:
            return 10


class Hero(Entity):
    """docstring for Hero"""
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def get_nickname(self):
        return self.nickname

    def known_as(self):
        return self.name + " the " + self.nickname


class Orc(Entity):
    """docstring for Org"""
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor

    def attack(self):
        return self.berserk_factor*(super().attack())

class Weapon():
    """docstring for Weapon"""
    def __init__(self, Type, damage, critical_strike_percent):
        self.Type = Type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def getType(self):
        return self.Type

    def getCriticalStrikePercent(self):
        return self.critical_strike_percent

    def critical_hit(self):
        random_strike_percent = random.uniform(0,1)
        if self.critical_strike_percent > random_strike_percent:
            self.critical_strike_percent *= 2
            return self.critical_strike_percent
        else:
            return self.critical_strike_percent

class Fight():
    """docstring for Fight"""
    def __init__(self, new_hero, new_orc):
        self.hero = new_hero
        self.orc = new_orc

    def who_starts(self):
        random_who_starts = randint(1,100)
        if random_who_starts <= 50:
            first = self.hero
            return first
        else:
            return self.orc

    def get_opponent(self,first):
        if first == self.hero:
            return self.orc
        else:
            return self.hero

    def simulate_fight(self):
        first = self.who_starts()
        print("%s starts" % first.name)
        second = self.get_opponent(first)

        if first.has_weapon()==False:
            weapon_bare_hands = Weapon("his bare hands!", 5, 0.09)
            setattr(Entity, "weapon", weapon_bare_hands)

        if second.has_weapon()==False:
            weapon_bare_hands = Weapon("his bare hands!", 5, 0.09)
            setattr(Entity, "weapon", weapon_bare_hands)

        while True:
            damage = first.attack()
            print("%s attacks with %s" % (first.name, first.weapon.Type))
            second.take_damage(damage)
            print("%s is hurted" % (first.name))
            if second.is_alive() == False:
                print("%s died" % second.name)
                break
            damage = second.attack()
            print("%s attacks with %s" % (first.name, second.weapon.Type))
            first.take_damage(damage)
            print("%s is hurted" % (second.name))
            if first.is_alive() == False:
                print("%s died" % first.name)
                break
        if first.is_alive():
            return first
        return second

class Dungeon():
    """docstring for Dungein"""
    def __init__(self, file_to_read):
        file = open(file_to_read, "r")
        self.unparsed_map = file.read()
        file.close()


    def get_map(self):
        return self.unparsed_map

    def print_map(self):
        print(self.get_map())


