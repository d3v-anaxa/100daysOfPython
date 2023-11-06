class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __str__(self):
        return f"{self.name} ({self.sound})"

class Dog(Animal):
    def __init__(self, breed):
        Animal.__init__(self, name="Dog", sound="Bark")
        self.breed = breed
    
    def __str__(self):
        return f"{self.name}[{self.breed}] -> {self.sound}"

class Cat(Animal):
    def __init__(self, breed):
        Animal.__init__(self, name="Cat", sound="Meow")
        self.breed = breed
    
    def __str__(self):
        return f"{self.name}[{self.breed}] -> {self.sound}"

print(f"""
{ Dog('Doverman') }
{ Dog('Rotweiller') }
{ Cat('Persian') }
      """) 
