def partition(arr, low, high):
    """
     This function takes last element as pivot, places
     the pivot element at its correct position in sorted
     array, and places all smaller (smaller than pivot)
     to left of pivot and all greater elements to right
     of pivot
    """
    i = (low-1)           # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    """
    The main function that implements QuickSort
    arr[] - -> Array to be sorted,
    low - -> Starting index,
    high - -> Ending index
    """
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = [1, 0, 1, 0, 1, 0, 0, 1]

quickSort(arr, 0, len(arr) - 1)
print(arr)
