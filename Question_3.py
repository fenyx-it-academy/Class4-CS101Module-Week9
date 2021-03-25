
class BSTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def TreeChild(branch, diff=0, level=1):
    # base case
    if branch is None:
        return diff

    # if the current level is odd
    if level % 2 == 1:
        diff = diff + branch.data

    else:
        diff = diff - branch.data

    diff = TreeChild(branch.left, diff, level + 1)
    diff = TreeChild(branch.right, diff, level + 1)

    return diff


if __name__ == '__main__':
    ''' Construct the following tree
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
    '''

    branch                  = BSTree(1)
    branch.left             = BSTree(2)
    branch.right            = BSTree(3)
    branch.left.left        = BSTree(4)
    branch.right.left       = BSTree(5)
    branch.right.right      = BSTree(6)
    branch.right.left.left  = BSTree(7)
    branch.right.left.right = BSTree(8)

    print("(Level1+Level3<=>[1+4+5+6])-(Level2+Level4<=>[2+3+7+8]) = ",TreeChild(branch))

