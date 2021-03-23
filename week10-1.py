import heapq

def minCost(arr, n):
    heapq.heapify(arr)
    res = 0
    while (len(arr) > 1):

        first = heapq.heappop(arr)
        second = heapq.heappop(arr)


        res += first + second
        heapq.heappush(arr, first + second)
    return res

if __name__ == '__main__':
    lengths = [5, 4, 2, 8]
    size = len(lengths)

    print("The minimum cost is " +
          str(minCost(lengths, size)))


