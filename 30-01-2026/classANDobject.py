# class Vehicle:
#     def __init__(self, start):
#         self.start = start
    
#     def display(self):
#         print("Vehicle started at:", self.start)

# class Car(Vehicle):
#     def __init__(self, start, drive):   
#         super().__init__(start)
#         self.drive = drive
    
#     def display(self):
#         super().display()
#         print("Car is being driven:", self.drive)

# class ElectricCar(Car):
#     def __init__(self, start, drive, battery):
#         super().__init__(start, drive)
#         self.battery = battery
    
#     def display(self):
#         super().display()
#         print("Electric car battery level:", self.battery)
        
# v = Vehicle("8:00 AM")
# v.display()

# c = Car("9:00 AM", "Highway")
# c.display()

# e = ElectricCar("10:00 AM", "City", "80%")
# e.display()



# 2. Create a class Person that stores name, inherit it into Employee that stores salary, 
#    then inherit it into Manager that stores department and display all details.



class Person:
    def __init__(self, person_name):
        self.person_name = person_name
    
class Employee(Person):
    def __init__(self, person_name, emp_salary):
        super().__init__(person_name)
        self.salary = emp_salary

class Manager(Employee):
    def __init__(self, person_name, emp_salary, dept):
        super().__init__(person_name, emp_salary)
        self.department = dept
        
    def display(self):
        print("Name:", self.person_name)
        print("Salary:", self.salary)
        print("Department:", self.department) 

m = Manager("Charlie", 80000, "Sales")
m.display()
    