n=int(input("Enter number of row: "))
i=1
p=65
while i<=n:
    j=1
    while j<=i:
        if p>90:
            p=65
        print(chr(p),end="")
        j=j+1
        p=p+1
    print()
    i=i+1
