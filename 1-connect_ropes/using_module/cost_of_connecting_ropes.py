import heapq


def connect_ropes(arr):
    heapq.heapify(arr)
    result = 0

    while len(arr) > 1:
        first_rope = heapq.heappop(arr)
        second_rope = heapq.heappop(arr)

        result += first_rope + second_rope

        heapq.heappush(arr, first_rope+second_rope)

    return result


lst = [5, 4, 2, 8]
lst1 = [11, 22, 3, 4, 5, 6, 7, ]
lst2 = [11, 23, 1, 43, 6, 78, 5]
lst3 = [8, 2, 4, 56, 23, 1]
print(connect_ropes(lst))
print(connect_ropes(lst1))
print(connect_ropes(lst2))
print(connect_ropes(lst3))
