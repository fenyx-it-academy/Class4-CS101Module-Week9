# calculate the difference between the sum of all nodes present at odd levels and
# the sum of all nodes present at even level. You should get the required difference as output is:
# (1+4+5+6) - (2+3+7+8) = -4

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def calculate(root, diff=0, level=1):

    if root is None:
        return diff

    if level % 2 == 1:
        diff = diff + root.data

    else:
        diff = diff - root.data

    diff = calculate(root.left, diff, level + 1)
    diff = calculate(root.right, diff, level + 1)

    return diff


print("\n\nEnter the value for all nodes in the given order uing spaces between, "
      "enter 0 if no value is given: ")
print("For the given question you can enter  1 2 3 4 0 5 6 0 0 0 0 7 8 0 0 ")
print("           1"
      "\n       /       \\"
      "\n      2          3"
      "\n    /  \        /  \\"
      "\n   4    5      6    7"
      "\n  /\    /\    /\    /\\"
      "\n 8  9  10 11 12 13 14 15"
       )

nodes = input()
node_values = [int(i) for i in (nodes.split(" "))]


root = Node(node_values[0])
root.left = Node(node_values[1])
root.right = Node(node_values[2])

root.left.left = Node(node_values[3])
root.left.right = Node(node_values[4])
root.right.left = Node(node_values[5])
root.right.right = Node(node_values[6])

root.left.left.left = Node(node_values[7])
root.left.left.right = Node(node_values[8])
root.left.right.left = Node(node_values[9])
root.left.right.right = Node(node_values[10])

root.right.left.left = Node(node_values[11])
root.right.left.right = Node(node_values[12])
root.right.right.left = Node(node_values[13])
root.right.right.right = Node(node_values[14])

print(calculate(root))

