li_all = []
li_positive = []
li_negative = []
li_odd = []
li_even = []
count_times = {}
i = 1
while i <= 10:
    n = int(input("Enter the " + str(i) + " number: "))
    li_all.append(n)
    if n > 0:
        li_positive.append(n)
    elif n < 0:
        li_negative.append(n)
    if n % 2 != 0:
        li_odd.append(n)
    elif n % 2 == 0:
        li_even.append(n)
    i = i + 1
    if n not in count_times:
        count_times[n] = 1
    else:
        count_times[n] = count_times[n] + 1

print("Positive Numbers are: ", li_positive)
print("Negative Numbers are: ", li_negative)
print("Odd Numbers are: ", li_odd)
print("Even Numbers are: ", li_even)
print("Number of times Number occur", count_times)
