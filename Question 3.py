class Node:
    def __init__(self, data, leftNode=None, rightNode=None):
        self.data = data
        self.left = leftNode
        self.right = rightNode


def levelDiff(tree, diff, level):
    # Best Case
    if tree is None:
        return diff

    # Odd Levels
    if level % 2 == 1:
        diff = diff + tree.data
    else:   # Even levels
        diff = diff - tree.data

    # Check Left Node
    diff = levelDiff(tree.left, diff, level + 1)
    # Check Right Node
    diff = levelDiff(tree.right, diff, level + 1)

    return diff


tree = Node(1, Node(2, Node(4)), Node(3, Node(5, Node(7), Node(8)), Node(6)))
print(levelDiff(tree, 0, 1))