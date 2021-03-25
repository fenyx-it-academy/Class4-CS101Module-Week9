import heapq
from heapq import heappush, heappop

def theCheapestCost(quantities):
    heapq.heapify(quantities)

    prices = 0
    while len(quantities) > 1:
        q1 = heappop(quantities)
        q2 = heappop(quantities)

        sum = q1 + q2
        print("""Binary Sum is : {}""".format(sum))
        heappush(quantities,sum)
        prices += sum

    return prices

if __name__ == '__main__':
    quantities = [5, 4, 2, 8]

    print(quantities)
    print("The Cheapest Cost is :",theCheapestCost(quantities))