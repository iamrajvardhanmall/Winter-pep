# ENCAPSULATION OOP PRACTICE QUESTIONS
# 1. Create a Student class where marks are private and accessed using getter method.
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks   # Private attribute
        
#     def get_marks(self):
#         return self.__marks  
    
# s = Student("Alice", 85)
# print(s.get_marks()) # Output: 85




# 2. Create a BankAccount class with private balance and methods to deposit and check balance.
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.__balance = balance  # Private Attribute
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Deposit amount must be positive")
    
#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount("123456", 1000)
# account.deposit(500)
# print(account.get_balance()) # Output: 1500

# 3. Create a Person class where age is private and cannot be negative.
# class Person:
#     def __init__(self, age):
#         if age < 0:
#             raise ValueError("Age can not be negative")
#         self.__age = age
    
#     def display(self):
#         return self.__age

# p = Person(5788)
# print(p.display())
            
        

# 4. Create a User class that hides password and verifies it using a method.
# class passw:
#     def __init__(self, password):
#         self.__password = password
        
#     def checkpassword(self, enterpassword):
#         if self.__password == enterpassword:
#             return True
#         else:
#             return False
# p = passw("Raj")
# print(p.checkpassword("rbjfbrh"))
# print(p.checkpassword("Raj"))

    
    

# 5. Create an Employee class where salary is private and can be increased.
class Employee:
    def __init__(self, sal):
        self.__sal = sal
    
    def display(self, inc):
        self.__sal += inc
        return self.__sal

e = Employee(50000)
print(e.display(5000)) # Output: 55000
        

# 6. Create a Car class with private speed and methods accelerate and brake.

# 7. Create a Mobile class where battery percentage is private and decreases when used.

# 8. Create an ATM class with hidden PIN and verification method.

# 9. Create a Book class where price is private and cannot be negative.

# 10. Create a Result class where marks list is private and modified using methods.