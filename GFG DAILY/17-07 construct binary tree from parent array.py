'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        # your code here
        m = {}
        for c, p in enumerate(parent):
            if c not in m:
                m[c] = Node(c)
            if p not in m:
                m[p] = Node(p)
            
            if not m[p].left:
                m[p].left = m[c]
            else:
                m[p].right = m[c]
        return m[-1].left
    
