
import random
from entity import Entity

class ExpGoblin(Entity):
    '''One of the enemy classes that contains their info and attacks'''
    def __init__(self):
        """randomizing the hp"""
        hp = random.randint(12,15)
        super().__init__("Horrid Goblin",hp)

    def melee_attack(self, enemy):
        """randomizing the dmg"""
        dmg = random.randint(5,8)
        enemy.take_damage(dmg)
        return f"{self.name} slashes {enemy.name} for {dmg} damage."