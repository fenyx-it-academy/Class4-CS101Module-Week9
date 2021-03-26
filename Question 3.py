"""
Construct a following tree.

              1
            /   \
           /     \
          2       3
         /      /  \
        /      /    \
       4      5      6
             / \
            /   \
           7     8
Take this binary tree, calculate the difference between the sum of all nodes present at odd levels and
the sum of all nodes present at even level. You should get the required difference as output is:
(1+4+5+6) - (2+3+7+8) = -4
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def calc_sum_diff(root, diff=0, level=1):
    if root is None:
        return diff

    if level % 2 == 1:
        diff = diff + root.data

    else:
        diff = diff - root.data

    diff = calc_sum_diff(root.left, diff, level + 1)
    diff = calc_sum_diff(root.right, diff, level + 1)
    return diff

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
print("(1+4+5+6) - (2+3+7+8) =",calc_sum_diff(root))

