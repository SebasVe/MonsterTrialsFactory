"""Defines the ExpertFactory interface for creating enemies."""
import random
from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll

class ExpertFactory(EnemyFactory):
    """ Randomly reutrns expert enemies name """
    def create_random_enemy(self):
       return random.choice([ExpGoblin(), ExpTroll()])