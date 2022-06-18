string=input("Enter String: ")
count_word={}
string=string.split()
print(string)
for word in string:
    if word not in count_word:
        count_word[word]=1
    else:
        count_word[word]=count_word[word]+1
print(count_word)
