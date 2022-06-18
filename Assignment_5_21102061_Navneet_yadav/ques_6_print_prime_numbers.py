x=int(input("Enter Startng number: "))
n=int(input("Enter number for Range: "))
if x<=1:
    x=2
if n<=1 or n<x:
    print("Enter Range correctly")
while x<=n:
    i = 2
    flag = False
    while i < x:
        if x % i == 0:
            flag = True
            break
        i = i + 1
    if flag:
        pass
    else:
        print(x)
    x=x+1
