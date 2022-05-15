
"""
3.Write a python program to store different data type values into a list. (For an
example: Student [SID, Name, Gender, Course Name, CGPA]).
Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).
CGPA should have floating type values (example: 7.5).
"""

Sid=int(input("Enter your SID ",))
Name=str(input("Enter your Name ", ))
GEN=str(input("Enter your gender enter M for male,enter F for female,enter U for other ",))
CN=str(input("Enter course Name ", ))
CGPA=float(input("Enter your CGPA ", ))
List2=["SID","NAME","GENDER","COURSE_NAME","CGPA"]
List=[Sid,Name,GEN,CN,CGPA]
print(List2)
print(List)

