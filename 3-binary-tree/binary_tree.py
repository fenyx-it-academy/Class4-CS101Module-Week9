class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# A function to insert a new node with the given key value


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def even_odd_level_difference(root):
    if (not root):
        return 0

    q = []
    q.append(root)

    level = 0
    evenSum = 0
    oddSum = 0

    # traverse until the queue is empty
    while (len(q)):

        size = len(q)
        level += 1

        # traverse for complete level
        while(size > 0):

            temp = q[0]  # .front()
            q.pop(0)

            # check if level no. is even or
            # odd and accordingly update
            # the evenSum or oddSum
            if(level % 2 == 0):
                evenSum += temp.value
            else:
                oddSum += temp.value

            # check for left child
            if (temp.left):

                q.append(temp.left)

            # check for right child
            if (temp.right):

                q.append(temp.right)

            size -= 1

    return (oddSum - evenSum)


root = Node(1)
insert(root, Node(2))
insert(root, Node(3))
insert(root, Node(4))
insert(root, Node(5))
insert(root, Node(6))
insert(root, Node(7))
insert(root, Node(8))
# insert(root, Node(9))
# insert(root, Node(10))
# insert(root, Node(11))
# insert(root, Node(12))
# insert(root, Node(13))


result = even_odd_level_difference(root)
print(result)
