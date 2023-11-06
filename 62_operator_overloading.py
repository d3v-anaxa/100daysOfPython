class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, n):
        return f"{self.i + n.i}i + {self.j + n.j}j + {self.k + n.k}k"

    def __sub__(self, n):
        return f"{self.i - n.i}i + {self.j - n.j}j + {self.k - n.k}k"


v1 = Vector(10, 12, 15)
print(v1)

v2 = Vector(1, 2, 5)
print(v2)

print(v1 + v2)
print(v1 - v2)
