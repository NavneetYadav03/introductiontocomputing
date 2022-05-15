"""[2]. Store your name, SID, department name and CGPA into different variables.
With the help of String formatting print the following output:
Hey, ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is 9.9
"""

Name='ABC'
SID=21105039
Department='XYZ'
CGPA=9.9
print("Hey, {} Here! \nMy SID is {} \nI am from {} department and my CGPA is {}." .format(Name, SID, Department, CGPA), end='\n')
