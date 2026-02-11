# # Abstraction: Abstraction (in Object-Oriented Programming) means showing only what the user needs to know and hiding the internal implementation details.
# ABC means "Abstract based class"
# NOTE:
# a.) Abstract class must have atleast one method
# b.) We can not create object of abstract class
# c.) We have to use @abstractmethod decorator to define abstract method



# 🔹 What is an Abstract Class?
# An abstract class is a class that:
# ❌ Cannot be instantiated directly
# ✅ Is meant to be inherited
# ✅ Defines abstract methods that child classes must implement
# Think of it as a blueprint / contract:
# It says what methods must exist, but not how they work.

# 🔹 Why Abstract Classes Exist
# They help you:
# Enforce a common structure across subclasses
# Hide implementation details
# Achieve abstraction (focus on what, not how)
# Reduce bugs by forcing required methods
# Enable polymorphism
# Make large systems easier to maintain
# In real projects, abstract classes prevent incomplete or inconsistent subclasses.





# # ABSTRACTION OOPS PRACTICE QUESTIONS IN PYTHON

# # 1. Create an abstract class Animal with abstract method sound() and implement it in Dog class.
from abc import ABC, abstractmethod
# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass
    
# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")

# d = Dog()
# d.sound()



# # 2. Create an abstract class Shape with abstract method area() and implement it in Rectangle class.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print("Area of Rectangle:", self.length * self.width)
        
r = Rectangle(5, 3)
r.area()


# # 3. Create an abstract class Bank with abstract method interest_rate() and implement it in SBI class.

# class Bank(ABC):
#     @abstractmethod
#     def interest_rate(self):
#         pass
    
# class SBI(Bank):
    
#     def __init__(self, rate):
#         self.rate = rate
        
#     def interest_rate(self):
#         print("SBI Interest Rate:", self.rate)
        
# s = SBI(34)
# s.interest_rate()
        

# # 4. Create an abstract class Vehicle with abstract method speed() and implement it in Car class.
# class Vehicle(ABC):
#     @abstractmethod
#     def speed(self):
#         pass
    
# class Car(Vehicle):
#     def __init__(self, speed):
#         self.speed = speed
        
#     def speed(self):
#         print("Car speed:", self.speed)
# c = Car(120)
# c.speed()



# # 5. Create an abstract class Employee with abstract method salary() and implement it in Developer class.
# class Employee(ABC):
#     @abstractmethod
#     def salary(self):
#         pass
    
# class Developer(Employee):
#     def __init__(self, salary):
#         self.salary = salary
        
#     def salary(self):
#         print("Developer salary:", self.salary)
        
# d = Developer(500000)
# d.salary()


# # 6. Create an abstract class Payment with abstract method pay(amount) and implement it in UPI class.
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
    
# class UPI(Payment):
        
#     def pay(self, amount):
#         print("Paid amount:", amount)
        
# u = UPI(10000)
# u.pay()


# # 7. Create an abstract class Mobile with abstract method features() and implement it in Samsung class.
from abc import ABC, abstractmethod

class Mobile(ABC):
    @abstractmethod
    def features(self):
        pass
    

class Samsung(Mobile):
    def __init__(self, features):
        self.feature_list = features   # renamed variable
        
    def features(self):
        print("Samsung features:", self.feature_list)


s = Samsung("Camera, Battery, Display")
s.features()


# # 8. Create an abstract class Course with abstract method duration() and implement it in PythonCourse class.
from abc import ABC, abstractmethod
class Course(ABC):
    @abstractmethod
    def duration(self):
        pass
    
class PythonCourse(Course):
    def __init__(self, duration):
        self.duration_a = duration  # renamed variable
        
    def duration(self):
        print("Python course duration:", self.duration_a)
        
p = PythonCourse("3 Months")
p.duration()

# # 9. Create an abstract class Food with abstract method price() and implement it in Pizza class.
class Food(ABC):
    @abstractmethod
    def price(self):
        pass

class Pizza(Food):
    def __init__(self, price):
        self.price_a = price 
    
    def price(self):
        print("Pizza price:", self.price_a)
        
p = Pizza(250)
p.price()

# # 10. Create an abstract class Electronics with abstract method warranty() and implement it in Laptop class.
class Electronics(ABC):
    @abstractmethod
    def warranty(self):
        pass
    
class Laptop(Electronics):
    def __init__(self, warrantly):
        self.warranty_a = warrantly
        
    def warranty(self):
        print("Laptop warranty:", self.warranty_a)
        
l = Laptop("2 Years")
l.warranty()