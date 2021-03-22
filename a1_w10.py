'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2021 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210322]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# Question 1:
# Given n ropes of different lengths, connect them into a single rope with minimum cost. 
# Assume that the cost to connect two ropes is the same as the sum of their lengths.(Hint: Use a priority queue implemented using min-heap)
# Input:    [5,4,2,8]
# Output :  The minimum cost is 36
# For example,
# [5, 4, 2, 8] –> First, connect ropes of lengths 4 and 2 that will cost 6.
# [5, 6, 8]    –> Next, connect ropes of lengths 5 and 6 that will cost 11.
# [11, 8]      –> Finally, connect the remaining two ropes that will cost 19.
# Therefore, the total cost for connecting all ropes is 6 + 11 + 19 = 36.

import heapq
from heapq import heappush, heappop

"""
         2      min-heap
       /   \
      4     5
           /
          8
"""
# Function to calculate the minimum cost to join `n` ropes into a single rope
def findMinCost(prices):
 
    # In-place transform list `prices` into a min-heap in linear time
    heapq.heapify(prices)
 
    # keep track of the minimum cost so far
    cost = 0
 
    # repeat till heap size is reduced to one
    while len(prices) > 1:
 
        # Extract the top two elements from the min-heap
        x = heappop(prices)
        y = heappop(prices)
 
        # calculate the cost of the extracted values
        sum = x + y
 
        # insert the cost back to the min-heap
        heappush(prices, sum)
 
        # update the minimum cost
        cost += sum
 
    return cost
 
 
if __name__ == '__main__':
 
    prices = [5, 4, 2, 8]
    print("The minimum cost is:", findMinCost(prices))
 