"""
Given a binary array,sort it in linear time and constant space by modifying the partitioning logic of the Quicksort algorithm.
The output should print all zeroes, followed by all ones. For example,
Input:      {1,0,1,0,1,0,0,1}
Output :    {0,0,0,0,1,1,1,1}
"""
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

arr = [1,0,1,0,1,0,0,1]
print("Binary array given is  : {}".format(arr))
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted binary array is : {}".format(arr))
