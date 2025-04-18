
import entity
import random
class Hero(entity.Entity):
    '''Main player entity used by the user only'''
    def __init__(self, name):
        """passing the name and hp in a superclass"""
        super().__init__(name,25)

    def melee_attack(self, enemy):
        """damage to the enemey and returning the description"""
        damage1 = random.randint(1,6)
        damage2 = random.randint(1,6)
        dmg = damage1 + damage2
        enemy.take_damage(dmg)
        return f"{self.name} slashes a {enemy.name} with a sword for {dmg} damage."

    def ranged_attack(self, enemy):
        """Arrow attack: deal 1D12 damage."""
        dmg = random.randint(1, 12)
        enemy.take_damage(dmg)
        return f"{self.name} pierces a {enemy.name} with an arrow for {dmg} damage."