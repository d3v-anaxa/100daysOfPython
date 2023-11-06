class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __str__(self):
        return f"Type -> {self.name} \nSound -> {self.sound}"

class Dog(Animal):
    def __init__(self, breed):
        Animal.__init__(self, name="Dog", sound="Bark")
        self.breed = breed
    
    def __str__(self):
        return f"{Animal.__str__(self)}\nBreed -> {self.breed}"

class GermanShepard(Dog):
    def __init__(self, color):
        Dog.__init__(self, breed="German Shepard")
        self.color = color

    def __str__(self):
        return f"{Dog.__str__(self)}\nColor -> {self.color}"

n1 = GermanShepard('Black & Golden')
print(n1)
