number=int(input("Enter number: ",))
n1=int(input("Start number for range: "))
n2=int(input("End number for range: "))
for i in range(n1,n2+1):
    if i%number==0:
        print(i)
