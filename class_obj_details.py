class Student():
    def __init__(self, Name, roll, english, maths, physics, python, java):
        self.name = Name
        self.rollnum = roll
        self.s1 = english
        self.s2 = maths
        self.s3 = physics
        self.s4 = python
        self.s5 = java
    def printalldetails(self):
        print(self.name)
        print(self.rollnum)
        print(self.s1)
        print(self.s2)
        print(self.s3)
        print(self.s4)
        print(self.s5)
obj1 = Student("sai","r6",78,57,98,58,56)
obj1.printalldetails()

obj2 = Student("pravalli","s2",79,60,89,67,56)
obj2.printalldetails()

obj3 = Student("priya",425,78,97,59,70,89)
obj3.printalldetails()