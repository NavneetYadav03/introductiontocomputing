"""
2. Write a Python function that checks whether a passed string is palindrome or not. Note:
A palindrome is a word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run.
"""
def check_palidrome(string):
    string_remove_space = string.replace(" ", "")
    reversed_string = string_remove_space[::-1]
    if string_remove_space == reversed_string:
        print("palindrome")
    else:
        print("not palindrome")


string=input("Enter string for palindrome check: ")
check_palidrome(string)
