"""
5. Write a Python function that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
"""
def seperate_and_sort(string):
    list_1 = string.split("-")
    list_1.sort()
    print("-".join(list_1))

string = input("Enter string: ")
seperate_and_sort(string)
