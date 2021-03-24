# Given a binary array, sort it in linear time and constant space by modifying
# the partitioning logic of the Quicksort algorithm.
# The output should print all zeroes, followed by all ones.
# Input:{1,0,1,0,1,0,0,1}
# Output :{0,0,0,0,1,1,1,1}

i = 0
binary = input(" Enter binary array using space between: ")
binary_list = [int(i) for i in (binary.split(" "))]
zeros = binary_list.count(0)   # Find all zeros from the input list

while zeros > 0:            # placing all zeros at first
    binary_list[i] = 0
    zeros = zeros - 1
    i = i + 1

for i in range(i, len(binary_list)):  # placing all ones after zeros
    binary_list[i] = 1

print(binary_list)
