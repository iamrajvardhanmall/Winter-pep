# class Person():
#     def __init__(self, name):
#         self.name = name
    
#     def display(self):
#         print("Name: ", self.name)

# class student(Person):
#     def __init__(self, rollno, name):
#         super().__init__(name)
#         self.rollno = rollno
        
#     def display(self):
#         print("Roll NO: ", self.rollno)
#         super().display()

# # p = Person("Amit")
# # p.display()       
# s = student(38, "Raj")
# s.display()





class School():
    def __init__(self, school_name):
        self.school_name = school_name
        
class Student(School):
    def __init__(self, school_name, grade):
        super().__init__(school_name)
        self.grade = grade
    
    def display(self):
        print(self.school_name, self.grade)

s = Student("ABC School", "10th Grade")
s.display()
