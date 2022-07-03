"""
Write a Python function to check whether a number is perfect or not. According to
Wikipedia : In number theory, a perfect number is a positive integer that is equal to the
sum of its proper positive divisors, that is, the sum of its positive divisors excluding the
number itself (also known as its aliquot sum). Equivalently, a perfect number is a
number that is half the sum of all of its positive divisors (including itself).
"""
def check_perfect(n):
    sum=0
    sum_2=n
    for i in range (1,n):
        if n%i==0:
            sum=sum+i
            sum_2=sum_2+i
    if sum==n:
        print("perfect number")
    else:
        print("number not perfect ")
    if sum_2/2==n:
        print("perfect number from 2nd method")
    else:
        print("number not perfect from 2nd method")

n=int(input("Enter number to check perfect: "))
check_perfect(n)
