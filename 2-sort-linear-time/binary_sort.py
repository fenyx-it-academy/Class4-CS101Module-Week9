def sort(arr):
    """
    Sort a binary Array
    """
    index = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[index] = 0
            index += 1

    for i in range(inx, len(arr)):
        arr[index] = 1
        index += 1


arr = [1, 0, 1, 0, 1, 0, 0, 1]
arr2 = [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
arr3 = [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1]
arr4 = [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1]

sort(arr)
print(arr)

sort(arr2)
print(arr2)

sort(arr3)
print(arr3)

sort(arr4)
print(arr4)
