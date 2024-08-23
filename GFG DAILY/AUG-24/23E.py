#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    # code here
    if not root:
        return []
    
    result = []
    queue = deque([(root, 0)])
    
    while queue:
        node, level = queue.popleft()
        if len(result) == level:
            result.append(node.data)
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return result
