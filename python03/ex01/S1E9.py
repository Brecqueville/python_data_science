from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a first name and an alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to change the character's health state to dead."""
        pass


class Stark(Character):
    """Class representing Stark, inheriting from Character."""

    def die(self):
        """Change the Stark character's alive status to False."""
        self.is_alive = False
