class LockingBinaryTreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self._is_locked = False
        self.locked_descendents = 0

    def _can_lock_or_unlock(self):
        if self.locked_descendents > 0:
            return False
        
        curr = self.parent
        while curr:
            if curr._is_locked:
                return False
            curr = curr.parent
        
        return True
    
    def is_locked(self):
        return self._is_locked
    
    def lock(self):
        if self._can_lock_or_unlock():
            self._is_locked = True

            curr = self.parent
            while curr:
                curr.locked_descendents += 1
                curr = curr.parent
            
            return True
        else:
            return False
    
    def unlock(self):
        if self._can_lock_or_unlock():
            self._is_locked = False

            curr = self.parent
            while curr:
                curr.locked_descendents -= 1
                curr = curr.parent
            
            return True
        else:
            return False

root = LockingBinaryTreeNode(4)
root.left = LockingBinaryTreeNode(3, LockingBinaryTreeNode(2, parent=root.left), LockingBinaryTreeNode(1, parent=root.left), parent=root)
root.right = LockingBinaryTreeNode(5, LockingBinaryTreeNode(6, parent=root.right), LockingBinaryTreeNode(7, parent=root.right), parent=root)

print("Before locking: " + str(root.left.left.is_locked()))
root.left.left.lock()
print("After locking: " + str(root.left.left.is_locked()))