class Base:
    def method(self):
        print("Base method")

new = {"lst" :[-19, 18, 0, 11, -23]}
print(f"{dir(new)}") # prints every method available on the given argument
print(f"{help(Base)}") # print man page of the given argument
print(f"{Base.__dict__}") # prints data members and methods of argument class
