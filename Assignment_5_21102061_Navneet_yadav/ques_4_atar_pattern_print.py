n=9
i1=1
while i1<=5:
    j1=1
    while j1<=i1:
        print("*",end=" ")
        j1= j1 + 1
    print()
    i1= i1 + 1
i2=1
while i2<=4:
    j2=1
    while j2<=(n-5-i2+1):
        print("*",end=" ")
        j2=j2+1
    print()
    i2=i2+1

