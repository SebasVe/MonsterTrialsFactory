"""Defines the EnemyFactory interface for creating enemies."""
from abc import ABC, abstractmethod
import entity

class EnemyFactory(ABC):
    """Interface for enemy factory classes."""
    @abstractmethod
    def create_random_enemy(self):
        """Create and return a random enemy instance."""
        pass