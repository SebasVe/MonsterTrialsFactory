
import random
from entity import Entity

class ExpTroll(Entity):
    '''One of the enemy classes that contains their info and attacks'''
    def __init__(self):
        """randomizing the hp"""
        hp = random.randint(15,18)
        super().__init__("Angry Troll",hp)

    def melee_attack(self, enemy):
        """randomizing the dmg"""
        dmg = random.randint(8,12)
        enemy.take_damage(dmg)
        return f"{self.name} crushes {enemy.name} for {dmg} damage."