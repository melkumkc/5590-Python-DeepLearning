class Employee(): # base class
    number_employee = 0 # public member

    def __init__(self, name, family, total_salary, department): # constructor
        self.name = name  # string
        self.family = family  # string
        self.total_salary = total_salary
        self.department = department
        Employee.number_employee += 1 # increamens number_emplyee when ever a new employee object is created


    def average_salary(self): # class method
        self.average = self.total_salary / 12
        return self.average



class FulltimeEmployee(Employee): # derived class
    full_time = True




E1 = Employee("abe", "getachew", 140000, "soft")



print(E1.name)
print(E1.average_salary())
print(E1.family)
print (Employee.number_employee)
E2 = FulltimeEmployee("mmmeee", "getachew", 240000, "soft")

print (Employee.number_employee)