def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

def selectionSort(arr, size):
    for step in range(size):
        minimum = step
        for i in range(step + 1, size):
            if arr[i] < arr[minimum]:
                minimum = i
        # Swap
        (arr[step], arr[minimum]) = (arr[minimum], arr[step])


duplicate = [int(x) for x in input("Enter array: ").split()]
x = Remove(duplicate)
size = len(x)
selectionSort(x, size)
print('Sorted Array in Ascending Order: ')
print(x)
