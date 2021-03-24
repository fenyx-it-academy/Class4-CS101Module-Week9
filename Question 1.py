import heapq

def minimum_cost(array):
    heapq.heapify(array)
    cost = 0

    while len(array) > 1:
        print(array)
        print("Current cost: ", cost)
        root = heapq.heappop(array)
        next = heapq.heappop(array)
        sum = root + next
        heapq.heappush(array, sum)
        cost += sum
        
    print("###############################")
    print("Total Cost: ", cost)

print("Enter the comma seperated values (e.g. 1,2,45,5): ")
input_vals = input()
array = [int(i) for i in (input_vals.split(","))]
minimum_cost(array)

