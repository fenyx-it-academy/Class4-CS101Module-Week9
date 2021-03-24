
# Without heap, just an conventional solution

def total_cost(n):
	total_cost = 0
	list2=[]
	while (len(n) > 1):
		x = (min(n))
		n.remove(min(n))
		y= (min(n))
		n.remove(min(n))
		cost = x+y
		list2.append(cost)
		total_cost += x+y
		n.append(cost)
		print (n)
	print ("Sums of 2 min. for each cycle", list2)
	return total_cost

n = [5,4,2,8]
print (n)
print (total_cost(n))