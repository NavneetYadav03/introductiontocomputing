"""
4.Write a python program to enter marks of 5 students into a list and display
them in sorted manner.
"""

a=float(input("Enter marks of First student ",))
b=float(input("Enter marks of Second student ",))
c=float(input("Enter marks of Third student ",))
d=float(input("Enter marks of Fourth student ",))
e=float(input("Enter marks of Fivth student ",))
marks=[a,b,c,d,e]
marks.sort()
print(marks)
