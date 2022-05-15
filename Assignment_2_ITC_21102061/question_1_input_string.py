#[a].Find the length of the input string.

string=str(input("Enter the string: ",))
print("length of input string: ",len(string))

#[b]. Reverse the order of the string in one line code.
r=string[::-1]
print("reverse of input string: ",r)

#[c]. Using Slice function store “a case sensitive” in new string.

S=slice(10, 26)
print("String slicing: ", string[S])

#[d]. Replace “a case sensitive” with “object oriented”.

f=string.replace('a case sensitive', 'object oriented')
print("Replacing substring: ", f)

#[e]. Find index of substring “a” in the given input string.

x=string.index('a')
print("Index of 'a' is: ", x)

#[f]. Remove the white spaces from the given input string.

m=string.replace(' ','')
print("string after removing white spaces: ", m, end="\n")
