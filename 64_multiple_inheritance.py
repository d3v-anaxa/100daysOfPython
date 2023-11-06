class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"Name : {self.name}\nRole : {self.role}"

class Developer:
    def __init__(self, TechStack):
        self.TechStack = TechStack

    def __str__(self):
        return f"Tech Stack : {self.TechStack}"

class Manager(Employee, Developer):
    def __init__(self, name, TechStack, Experience):
        Employee.__init__(self, name, role="Manager")
        Developer.__init__(self, TechStack)
        self.exp = Experience

    def __str__(self):
        return f"""{Employee.__str__(self)}\n{Developer.__str__(self)}\nExperience : {self.exp}"""

n1 = Manager("Ben", "MERN", 5)
print(n1)
