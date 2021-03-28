# Represent a node of binary tree
class Node:
    def __init__(self, data):
        # Assign data to the new node, set left and right children to None
        self.data = data;
        self.left = None;
        self.right = None;


class DiffOddEven:
    def __init__(self):
        # Represent the root of binary tree
        self.root = None;

        # difference() will calculate the difference between sum of odd and even levels of binary tree

    def difference(self):
        oddLevel = 0;
        evenLevel = 0;
        diffOddEven = 0;

        # Variable nodesInLevel keep tracks of number of nodes in each level
        nodesInLevel = 0;

        # Variable currentLevel keep track of level in binary tree
        currentLevel = 0;

        # queue will be used to keep track of nodes of tree level-wise
        queue = [];

        # Check if root is None
        if (self.root == None):
            print("Tree is empty");
            return 0;
        else:
            # Add root node to queue as it represents the first level
            queue.append(self.root);
            currentLevel = currentLevel + 1;

            while (len(queue) != 0):
                # Variable nodesInLevel will hold the size of queue i.e. number of elements in queue
                nodesInLevel = len(queue);

                while (nodesInLevel > 0):
                    current = queue.pop(0);

                    # Checks if currentLevel is even or not.
                    if (currentLevel % 2 == 0):
                        # If level is even, add nodes's to variable evenLevel
                        evenLevel = evenLevel + current.data;
                    else:
                        # If level is odd, add nodes's to variable oddLevel
                        oddLevel = oddLevel + current.data;

                        # Adds left child to queue
                    if (current.left != None):
                        queue.append(current.left);
                        # Adds right child to queue
                    if (current.right != None):
                        queue.append(current.right);
                    nodesInLevel = nodesInLevel - 1;
                currentLevel = currentLevel + 1;
                # Calculates difference between oddLevel and evenLevel
            diffOddEven = abs(oddLevel-evenLevel);
        return diffOddEven;


bt = DiffOddEven();
# Add nodes to the binary tree
bt.root = Node(1);
bt.root.left = Node(2);
bt.root.right = Node(3);
bt.root.left.left = Node(4);
bt.root.right.left = Node(5);
bt.root.right.right = Node(6);
bt.root.right.right.left = Node(7);
bt.root.right.right.right = Node(8);

# Display the difference between sum of odd level and even level nodes
print("Difference between sum of odd level and even level nodes: " , str(bt.difference()));