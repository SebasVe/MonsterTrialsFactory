from abc import ABC, abstractmethod

class Entity(ABC):
    """Abstract base class for all entities in the game."""
    def __init__(self, name, hp):
        """Initialize entity with a name and hit points (HP)."""
        self._name = name
        self._hp = hp

    @property
    def name(self):
        """Get the entity's name."""
        return self._name

    @property
    def hp(self):
        """Get the entity's current HP."""
        return self._hp

    def take_damage(self, dmg):
        """Reduce HP by dmg, not dropping below zero."""
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        """String representation showing name and HP."""
        return f"{self.name} HP: {self.hp}"

    @abstractmethod
    def melee_attack(self, enemy):
        """Perform a melee attack on another entity."""
        pass