"""
7. Write a Python program to create two empty classes, Student and Marks. Now create
some instances and check whether they are instances of the said classes or not. Also,
check whether the said classes are subclasses of the built-in object class or not.
"""
class Student:
    pass
class Marks:
    pass
Navneet=Student()
Jatin=Student()
a_grade=Marks()
b_grade=Marks
print("To check whether they are instances of said classes or not:")
print(isinstance(Navneet,Student))
print(isinstance(Navneet,Marks))
print(isinstance(Jatin,Student))
print(isinstance(Jatin,Marks))
print(isinstance(a_grade,Marks))
print(isinstance(a_grade,Student))
print("\nTo check whether the said classes are subclasses of the built-in object class or not:")
print(issubclass(Student,object))
print(issubclass(Marks,object))
