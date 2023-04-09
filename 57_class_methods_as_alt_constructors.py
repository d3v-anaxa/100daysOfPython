class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def parsestr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

e1 = Employee("Harry", "12000")
e2 = Employee.parsestr("Larry-24000")
print(f"{e1.name} {e1.salary}")
print(f"{e2.name} {e2.salary}")
