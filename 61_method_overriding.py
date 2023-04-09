class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __area__(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__( radius, radius)

    def __area__(self):
        return 3.14 * self.radius * self.radius

s1 = Shape( 22, 7)
s2 = Circle(7)

print( "Area of shape : ", s1.__area__())
print( "Area of circle : ", s2.__area__())
