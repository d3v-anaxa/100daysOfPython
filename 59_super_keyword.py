import time
class Base:
    def __init__(self, arg):
        self.arg = arg

    def printdata(self):
        print(f"Base class : {self.arg}")

    def gettime(self):
        print( "TIME : ", time.asctime())

class Child(Base):
    def __init__(self, base):
        self.parent = base
        super().__init__(base.arg)

    def printdata(self):
        self.parent.printdata()
        print(f"Child class : {self.arg}")
        super().gettime()


n1 = Base("abcd")
n2 = Child(n1)
n1.printdata()
n2.printdata()
