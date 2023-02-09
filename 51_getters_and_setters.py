PI = 3.14


class standard:
    def __init__(self):
        self._circumference = 0

    @property  # this makes a getter method
    def circumference(self):
        return self._circumference

    @circumference.setter  # this creates a setter method
    def circumference(self, new_value):
        if (new_value <= 0):
            raise ValueError("Invalid input")
        self._circumference = 2 * new_value * PI


new = standard()
new.circumference = 100
print(new.circumference)
