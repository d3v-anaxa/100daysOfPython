class Person:
    name = str("Harry")
    occupation = str("Software dev")
    net_worth_in_dollar = int(1024)
    def info(self):
        print(f"{type(self)}{self.name} is a {self.occupation}. He earns {self.net_worth_in_dollar} dollars annually")
        # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

dev1 = Person()
dev1.info()
