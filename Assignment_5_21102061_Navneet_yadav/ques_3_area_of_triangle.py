import math
side1=float(input("side 1: "))
side2=float(input("side 2: "))
side3=float(input("side 3: "))
if side1<0 or side2<0 or side3<0:
    print("Triangle not Valid")

if side3<side1+side2 and side2<side1+side3 and side1<side3+side2:
    semi_perimeter = (side1 + side2 + side3) / 2
    area = math.sqrt((semi_perimeter) * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    print("Area of Triangle by Heron's Formula: ", area)
else :
    print("Triangle not Valid")
