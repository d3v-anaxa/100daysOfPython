class MyClass:
    company_name = "Tesla" # class_variable
    number_employee = 0

    def __init__(self, name):
        self.name = name
        self.number_employee += 1
        self.raise_amount = 0.2 # instance variable

    def show_details(self):
        print(f"""name : {self.name} raise_amount in {self.company_name} with {self.number_employee} employee : {self.raise_amount}""")

emp_1 = MyClass("Ayanaksha")
emp_2 = MyClass("Ranit")
MyClass.show_details(emp_1)
MyClass.show_details(emp_2)

emp_1.company_name = "Microsoft"
emp_1.raise_amount = 0.6

MyClass.show_details(emp_1)
MyClass.show_details(emp_2)

print(MyClass.company_name)
MyClass.company_name = "Google"

MyClass.show_details(emp_1)
MyClass.show_details(emp_2)
