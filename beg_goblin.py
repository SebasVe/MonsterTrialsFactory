
import random
from entity import Entity
class BegGoblin(Entity):
    '''One of the enemy classes that contains their info and attacks'''
    def __init__(self):
       """randomizing goblin hp"""
       hp = random.randint(7,9)
       super().__init__("Goblin", hp)

    def melee_attack(self,enemy):
        """randomizing goblin dmg """
        dmg = random.randint(4,6)
        enemy.take_damage(dmg)
        return f"{self.name} bites {enemy.name} for {dmg} damage."