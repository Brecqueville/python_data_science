class calculator:
    """Class for performing scalar mathematical operations on vectors."""
    def __init__(self, vector):
        """Initialize the calculator with a vector."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar to all elements of the vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply all elements of the vector by a scalar."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from all elements of the vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide all elements of the vector by a scalar."""
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError:
            print("Error: Division by zero.")
