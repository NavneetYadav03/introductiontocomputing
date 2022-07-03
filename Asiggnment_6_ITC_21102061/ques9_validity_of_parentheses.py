"""
9. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid
but "[)", "({[)]" and "{{{" are invalid.
"""
class sol:
    def validity(self,str1):
        ac=[]
        parentheses={"(":")","[":"]","{":"}"}
        for i in str1 :
            if i in parentheses:
                ac.append(i)
            elif len(ac)==0 or parentheses[ac.pop()]!=i:
                return False
        return len(ac) == 0
str=input("Write string for validity of parentheses: ")
print(sol().validity(str))
