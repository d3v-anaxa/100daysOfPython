class Person:
    def info(self):
        print(f"{self.name} is a {self.occupation}.")
#       The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    def __init__(self, name, occupation):
        print("created new instance", end="\t")
        self.name = str(name)
        self.occupation = str(occupation)
        self.info()
#    name = str("Harry")
#    occupation = str("Software dev")
#    net_worth_in_dollar = int(1024)
try:
    dev1 = Person("Harry", "dev")
    dev2 = Person("Harry", "dev")
    dev3 = Person("Harry", "dev")
    dev4 = Person("Harry", "dev")
    dev5 = Person("Harry", "dev")
    dev6 = Person("Harry", "dev")
except Exception as e:
    print(e)
