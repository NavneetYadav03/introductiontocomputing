"""
6. Given two numbers ‘a’ and b’. Write a program to count number of bits
needed to be flipped to convert ‘a’ to ‘b’.
"""
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
num = a ^ b
Count_flipped_bit = 0
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)
