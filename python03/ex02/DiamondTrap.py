from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    (
        "Class representing King Joffrey, "
        "inheriting from Baratheon and Lannister."
    )

    def __init__(self, first_name, is_alive=True):
        """Initialize the King character."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes_color):
        """Set the eyes color."""
        self.eyes = eyes_color

    def set_hairs(self, hairs_color):
        """Set the hairs color."""
        self.hairs = hairs_color

    def get_eyes(self):
        """Get the eyes color."""
        return self.eyes

    def get_hairs(self):
        """Get the hairs color."""
        return self.hairs
