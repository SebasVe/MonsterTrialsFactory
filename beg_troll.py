import random
from entity import Entity

class BegTroll(Entity):
    '''One of the enemy classes that contains their info and attacks'''
    def __init__(self):
        hp = random.randint(8,10)
        super().__init__("Troll",hp)

    def melee_attack(self, enemy):
        dmg = random.randint(5,9)
        enemy.take_damage(dmg)
        return f"{self.name} smacks {enemy.name} for {dmg} damage."