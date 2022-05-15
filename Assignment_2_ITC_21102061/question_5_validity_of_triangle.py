"""
5. For any three lengths, there is a simple test to see if it is possible to form a
triangle. If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
converts them to integers, and to check whether the given input lengths can
form a triangle or not (Print : “Yes” or “No”).[Don’t use if else here].
"""
side1=int(input("Enter 1st side of triangle :"))
side2=int(input("Enter 2nd side of traingle :"))
side3=int(input("Enter 3rd side of triangle :"))
while (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
    print("Yes,triangle is valid")
    break
else:
    print("No,triangle not valid")
