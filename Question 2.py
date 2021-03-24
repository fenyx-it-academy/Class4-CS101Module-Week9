def QuickSort(array, lowestVal, length):
  if lowestVal < length:
    q = partition(array, lowestVal, length)
    QuickSort(array, lowestVal, q-1)
    QuickSort(array, q+1, length)
  return array 

def partition(array, lowestVal, length):
  pivot = array[length]
  i = lowestVal - 1
  temp = 0
  for j in range(lowestVal, length):
    if array[j] <= pivot:
      i += 1
      temp = array[j]
      array[j] = array[i]
      array[i] = temp
  temp = array[i + 1]
  array[i + 1] = array[length]
  array[length] = temp
  return(i+1)


li = [1,0,1,0,1,0,0,1]

print(QuickSort(li, 0, len(li)-1))
