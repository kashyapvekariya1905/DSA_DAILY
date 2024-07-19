class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def RemoveHalfNodes(self, root):
        # Base case: if the root is None, return None
        if root is None:
            return None
        
        # Recursively process left and right subtrees
        root.left = self.RemoveHalfNodes(root.left)
        root.right = self.RemoveHalfNodes(root.right)
        
        # If the current node is a half node
        if root.left is None and root.right is not None:
            return root.right
        if root.left is not None and root.right is None:
            return root.left
        
        # If it's not a half node, return the root
        return root
