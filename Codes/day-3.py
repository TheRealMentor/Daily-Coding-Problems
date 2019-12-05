# In the question it is not mentioned that tree is complete or not, here I have taken the tree to be complete.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def serialize(root):
    queue = []
    res = []
    queue.append(root)
    res.append(root.val)

    while(len(queue)!=0):
        tmp = queue.pop(0)
        if tmp.left:
            queue.append(tmp.left)
            res.append(tmp.left.val)

        if tmp.right:
            queue.append(tmp.right)
            res.append(tmp.right.val)

    return res

def deserialize(arr, root, i):

    if i < len(arr):
        temp = Node(arr[i])
        root = temp

        root.left = deserialize(arr, root.left, 2*i+1)
        root.right = deserialize(arr, root.right, 2*i+2)
    
    return root

node = Node('root', Node('left', Node('left.left')), Node('right'))

print(deserialize(serialize(node), None, 0).left.left.val)
