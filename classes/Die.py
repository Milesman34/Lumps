import random

# Class that represents a die
class Die:
    def __init__(self, sides):
        self.sides = sides
        self.value = -1
        self.locked = False

        # Temporary locked value for GUI purposes
        self.temp_locked = False

    def __repr__(self):
        return f"die(sides={self.sides}, value={self.value})"

    # Rolls the die, returning the new value
    def roll(self) -> int:
        self.value = random.randint(1, self.sides)
        return self.value