# Class and Objects
# 1.)

# class Car:
#     def __init__(self, model, company, year, speed):
#         self.model = model
#         self.company = company
#         self.year = year
#         self.speed = speed
    
# myCar = Car("Raj", "Raj1", 2020, 60)
# print(myCar.company)
# print(myCar.speed)
# print(myCar.year)
# print(myCar.model)



# class Car:
#     def __init__(self, model, company, year, speed, break2):
#         self.model = model
#         self.company = company
#         self.year = year
#         self.speed = speed
#         self.break2 = break2

#     def speed1(self):
#         print(self.model)

#     def break1(self):
#         print(self.break2)

#     def acc(self):
#         self.speed += 50
#         return self.speed
    
# myCar = Car("Raj", "Raj1", 2020, 60, -6)
# print(myCar.company)
# print(myCar.speed)
# print(myCar.year)
# print(myCar.model)
# myCar.speed1()
# myCar.break1()
# print(myCar.acc())




# class student:
#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks

# name = input()
# roll_no = int(input())
# marks = int(input())

# st = student(name, roll_no, marks)
# print(st.name)
# print(st.roll_no)
# print(st.marks)



# class BankAcc:
#     def __init__(self, dep, withdr):
#         self.dep = dep
#         self.withdr = withdr

#     def deposit(self):
#         if dep > 5000:
#             print("Deposit")
#         else:
#             print("Withdraw")

# dep = int(input())
# withdr = int(input())

# ba = BankAcc(dep, withdr)
# ba.deposit()




# class sal:
#     def __init__(self, salary, bonus):
#         self.salary = salary
#         self.bonus = bonus

#     def bal(self):
#         total = self.salary + self.bonus
#         return total

# salary = int(input())
# bonus = int(input())

# s = sal(salary, bonus)
# print(s.bal())



# class battery:
#     def __init__(self, battery_level):
#         self.battery_level = battery_level

#     def battery_status(self):
#         if self.battery_level > 50 and battery_level < 100:
#             print("High")
#         elif self.battery_level > 100:
#             print("Not valid")
#         else:
#             print("Low")

# battery_level = int(input())
# b = battery(battery_level)
# b.battery_status()




class aval:
    def __init__(self, booksCount):
        self.booksCount = booksCount
        print("Cont of aval")
    
    def avl(self):
        if self.booksCount < 1:
            print("Not aval")
        else:
            print("aval")

    def display(self):
        print("Hello Raju")

# booksCount = int(input())
# a = aval(booksCount)
# a.avl()





# Simple Inheritence
class interit(aval):
    def __init__(self, name):
        self.name = name
        
    
    def detailofsimple(self):
        print("Name: ", self.name)

mani  = interit("mani")
mani.display()



class mul_interit(aval, interit):
    def __init__(self, name1):
        self.name1 = name1
        
    def detailofmaul(self):
        print("Name: ", self.name1)

man  = mul_interit("mani")
man.display()