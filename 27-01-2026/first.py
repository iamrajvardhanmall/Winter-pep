# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
# myCar = Car("Toyota", "Corolla", 2020)
# print(myCar.make)
# print(myCar.model)
# print(myCar.year)



# class Car1:
#     def __init__(self, manikant, aniket):
#         self.manikant = manikant
#         self.aniket = aniket

# myCar1 = Car1("BMW", "X5")
# print(myCar1.manikant)
# print(myCar1.aniket)


# Add method to class to increase speed and to decrease speed
# class Car2:
#     def __init__ (self, speed):
#         self.speed = speed
    
#     def incr(self):
#         self.speed += 10
#         return self.speed
    
#     def decr(self):
#         self.speed -= 100
#         return self.speed
    
# myCar2 = Car2(50)
# print(myCar2.incr())
# print(myCar2.decr())



# Add a methos to display car information
class Car3:
    def __init__ (self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
        
    def display(self):
        print("Car Make:", self.make)
        print("Car Model:", self.model)
        print("Car Price:", self.price)

myCar3 = Car3("Honda", "Civic", 22000)
myCar3.display()