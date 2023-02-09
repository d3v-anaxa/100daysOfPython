class Employee:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def showDetails(self):
        print(f"Name : {self._name} && ID : {self._id}")


class Programmer(Employee):
    def showLang(self):
        print("C is the only language i'll ever use")


emp_1 = Employee("Baburao Aapte", "star garage")
emp_1.showDetails()

emp_2 = Programmer("Linus Torvald", "Linux")
emp_2.showDetails()
emp_2.showLang()
