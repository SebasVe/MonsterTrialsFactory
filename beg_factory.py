"""Defines the BeginnerFactory interface for creating random enemies names."""
import random
from enemy_factory import EnemyFactory
from beg_goblin import BegGoblin
from beg_troll import BegTroll

class BeginnerFactory(EnemyFactory):
    """ Randomly reuturns beginner enemies into the program """
    def create_random_enemy(self):
        return random.choice([BegGoblin(), BegTroll()])