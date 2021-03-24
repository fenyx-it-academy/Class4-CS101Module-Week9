

def sort(A):
	# Count Zero's
	zeros = A.count(0)

	# Restructure to locate O's from beginning
	k = 0
	while zeros:
		A[k] = 0
		zeros = zeros - 1
		k = k + 1

	# fill the  rest with 1
	for k in range(k, len(A)):
		A[k] = 1


if __name__ == '__main__':
	A = [1,0,1,0,1,0,0,1]

	sort(A)

	# print the restructured list
	print(A)




