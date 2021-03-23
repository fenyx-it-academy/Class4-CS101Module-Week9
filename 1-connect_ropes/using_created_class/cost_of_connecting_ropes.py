from BHeap import BHeap


def connect_ropes(arr):
    binary_heap = BHeap()
    for i in arr:
        binary_heap.add(i)

    result = 0

    while binary_heap.size() > 1:
        first_rope = binary_heap.poll()
        second_rope = binary_heap.poll()

        result += first_rope + second_rope

        binary_heap.add(first_rope+second_rope)

    return result


lst = [5, 4, 2, 8]
lst1 = [11, 22, 3, 4, 5, 6, 7, ]
lst2 = [11, 23, 1, 43, 6, 78, 5]
lst3 = [8, 2, 4, 56, 23, 1]

print(connect_ropes(lst))
print(connect_ropes(lst1))
print(connect_ropes(lst2))
print(connect_ropes(lst3))
