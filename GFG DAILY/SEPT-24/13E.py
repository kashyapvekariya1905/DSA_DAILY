#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        def f(root):
            
            if not root:
                return
            root.left,root.right = root.right,root.left
            f(root.left)
            f(root.right)
        
        return f(root)