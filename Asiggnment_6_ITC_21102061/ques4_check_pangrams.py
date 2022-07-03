"""
Write a Python function to check whether a string is a pangram or not. Note: Pangrams
are words or sentences containing every letter of the alphabet at least once. For
example: "The quick brown fox jumps over the lazy dog"
"""
def check_pangrams(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    flag = False
    for ele in alphabet:
        if ele not in string.lower():
            flag = False
            break
        else:
            flag = True
    if flag:
        print("pangram")
    else:
        print("not pangram")
string=input("Enter string to check pangrams: ")
check_pangrams(string)


