# Given n ropes of different lengths, connect them into a single rope with minimum cost.
# Assume that the cost to connect two ropes is the same as the sum of their lengths.

import heapq


def minimum_cost(cost):
    heapq.heapify(cost)                     # heapify the entered list
    total_cost = 0

    while len(cost) > 1:                    # continue if more than one node exists
        top = heapq.heappop(cost)           # delete the first
        next = heapq.heappop(cost)          # and the next node since they create a new joint node
        heapq.heappush(costs, top + next)   # sum of two deleted nodes place at the top as new node
        total_cost += top + next            # add these costs to the total cost
    print("Minimum Cost: ", total_cost)     # print the total cost when one node left


lengths = input("Enter the length of the ropes using spaces between:")
costs = [int(i) for i in (lengths.split(" "))]  # convert the string into integer in a list
minimum_cost(costs)                             # run the program with the given inputs
