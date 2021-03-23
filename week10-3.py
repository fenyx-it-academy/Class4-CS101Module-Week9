class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def evenOddLevelDifference(root):
    if (not root):
        return 0

    q = []
    q.append(root)

    level = 0
    evenSum = 0
    oddSum = 0

    while (len(q)):

        size = len(q)
        level += 1

        while (size > 0):

            temp = q[0]
            q.pop(0)

            if (level % 2 == 0):
                evenSum += temp.data
            else:
                oddSum += temp.data

            if (temp.left):
                q.append(temp.left)

            if (temp.right):
                q.append(temp.right)

            size -= 1

    return (oddSum - evenSum)


if __name__ == '__main__':
    """
    Let us create Binary Tree shown
    in above example """
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.left = newNode(5)
    root.right.right = newNode(6)
    root.right.left.left = newNode(7)
    root.right.left.right = newNode(8)

    result = evenOddLevelDifference(root)
    print( "\nDiffence between sums is", result)

