"""
Translate each of the following mathematical expressions into an equivalent Python expression. You may assume that the math library has been imported (via import math).
a) 
(3 + 4)(5)
b)
n(n-1)
c)
4(pie)(r^2)
d)
(r(cos alpha)^2 +r(sin beta)^2)^1/2
e)
(y2-y1)/(x2-x1)
"""
import math
# a)
print("Value of (3+4)(5): ",(3+4)*(5))

# b)
n=int(input("value of n: ",))
print("Value of n(n-1)/2 :",(n*(n-1)/2))

# c)
r=int(input("value of r: ",))
print("Value of 4(pie)(r)^2",4*(math.pi)*(r**2))

# d)
r=int(input("Value of r: ",))
alpha=float(input("Value of Alpha in Degrees: "))
beta=float(input("Value of Beta in Degrees: "))
print("Value of ((r)(cos(alpha)^2 +(r)(sin(beta)^2)^1/2: ",math.sqrt(((r)*(math.cos(math.radians(alpha)))**2) + ((r)*(math.sin(math.radians(beta)))**2)))

# e)
x1=float(input("Value of x1: "))
x2=float(input("Value of x2: "))
y1=float(input("Value of y1: "))
y2=float(input("Value of y2: "))
print("Value of (y2-y1)/(x2-x1): ",(y2-y1)/(x2-x1))


