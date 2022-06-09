"""
1. Write a program to take a number as input and convert it into its binary equivalent.
"""

number=int(input("Enter a number: "))
b=[]
while(number > 0):
    digit= number % 2
    b.append(digit)
    number= number // 2
b.reverse()
print("Binary Equivalent is: ")
for i in b:
    print(i,end=" ")
