"""
Write a Python function that prints out the first n rows of Pascal's triangle. Note:
Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
Sample Pascal's triangle:
"""

from math import factorial


def print_pascal_triangle(numRows):
    for i in range(numRows):
        for j in range(numRows - i + 1): #for spaces
            print(end=" ")
        for j in range(i + 1): #for elements in row
            # nCr = n!/((n-r)!*r!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print("\n")# print each row in a new line

number_of_rows=int(input("Number of rows (always positive): "))
print_pascal_triangle(number_of_rows)
