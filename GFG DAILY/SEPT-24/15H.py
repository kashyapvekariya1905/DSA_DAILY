#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        # do Code here
        if not root:
            
            return None
        
        stupid_head=head = Node(-1)
        
        stack = []
        
        
        node = root
        
        
        while stack or node:
            
            
            if node:
                
                
                stack.append(node)
                
                
                node = node.left
                
                
            else:
                
                node = stack.pop()
                
                head.right = node
                
                node.left = head
                head = head.right
                
                node = node.right
                
                
        head.right = None
        
        
        stupid_head = stupid_head.right
        
        stupid_head.left = None
        
        
        return stupid_head