"""
Given n ropes of different lengths, connect them into a single rope with minimum cost.
Assume that the cost to connect two ropes is the same as the sum of their lengths.
(Hint: Use a priority queue implemented using min-heap)
Input: [5,4,2,8]
Output : The minimum cost is 36
For example,
[5, 4, 2, 8] –> First, connect ropes of lengths 4 and 2 that will cost 6.
[5, 6, 8]    –> Next, connect ropes of lengths 5 and 6 that will cost 11.
[11, 8]      –> Finally, connect the remaining two ropes that will cost 19.
Therefore, the total cost for connecting all ropes is 6 + 11 + 19 = 36.
"""
import heapq
from heapq import heappush, heappop


def mincost(ropelenght):
    heapq.heapify(ropelenght)

    cost = 0
    while len(ropelenght) > 1:
        p1 = heappop(ropelenght)
        p2 = heappop(ropelenght)
        sum = p1 + p2
        print(p1, '+', p2, '\t=', sum)
        heappush(ropelenght, sum)
        cost += sum
    return cost


ropelenght = [5, 4, 2, 8]

print('Ropes Lenghts:', ropelenght)
print("The minimum cost is :", mincost(ropelenght))
