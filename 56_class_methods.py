class Employee:
    company = "Twitter"
    def show(self):
        print(f"The name of the company is {self.company} ")
    
    @classmethod # decorator to manipulate class member values
    def manip(self, newCompany):
        self.company = newCompany

e1 = Employee()
e1.show()
print(Employee.company)
e1.manip("SpaceX")
e1.show()
print(Employee.company)
