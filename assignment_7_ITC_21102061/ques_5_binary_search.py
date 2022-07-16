def binarySearch(array, x, low, high):
    low = 0;

    mid = low
    index = -1
    while low < high:
        mid = low + (high - low) // 2
        if array[mid] > x:
            high = mid
        elif array[mid] < x:
            low = mid + 1
        else:
            index = mid
            high = mid
    return index


array  = [int(x) for x in input("Enter array: ").split()]
x=int(input("Enter the number for occuurences: "))
new = sorted(array)
result = binarySearch(array, x, 0, len(array) - 1)
print("Sorted Array is,", new)
if result != -1:  # If element is found
    print("Number of occurences of element", x, "is:", array.count(x))
else:  # If element is not found
    print("Not found")
