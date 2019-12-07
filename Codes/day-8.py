class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def countUnivalRec(root, count):
    if root is None:
        return True
    
    left = countUnivalRec(root.left, count)
    right = countUnivalRec(root.right, count)

    if left == False or right == False:
        return False
    
    if root.left and root.data != root.left.data:
        return False
    
    if root.right and root.data != root.right.data:
        return False

    count[0] += 1
    return True

def countUnival(root):
    count = [0]
    countUnivalRec(root, count)
    return count[0]

tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(countUnival(tree))