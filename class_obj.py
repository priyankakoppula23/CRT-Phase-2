class Student():
    def __init__(self, Name, roll, english, maths, physics, python, java):
        self.name = Name
        self.rollnum = roll
        self.s1 = english
        self.s2 = maths
        self.s3 = physics
        self.s4 = python
        self.s5 = java

obj1 = Student("sai","r6",78,57,98,58,56)
print(obj1.name)
print(obj1.rollnum)
print(obj1.s1)
print(obj1.s2)
print(obj1.s3)
print(obj1.s4)
print(obj1.s5)

obj2 = Student("pravalli","s2",79,60,89,67,56)
print(obj2.name)
print(obj2.rollnum)
print(obj2.s1)
print(obj2.s2)
print(obj2.s3)
print(obj2.s4)
print(obj2.s5)

obj3 = Student("priya",425,78,97,59,70,89)
print(obj3.name)
print(obj3.rollnum)
print(obj3.s1)
print(obj3.s2)
print(obj3.s3)
print(obj3.s4)
print(obj3.s5)