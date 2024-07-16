class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: TreeNode, origin: int, destination: int) -> str:
        self.path_array = [''] * 100001
        self.start_ptr = 0
        self.end_ptr = 100000
        self.origin = origin
        self.destination = destination
        
        self.traverse_tree(root)
        
        if self.start_ptr > 0:
            return ''.join(self.path_array[:self.start_ptr])
        else:
            return ''.join(self.path_array[self.end_ptr + 1:])
    
    def traverse_tree(self, node):
        if not node:
            return 0
        
        if node.val == self.destination:
            return -1 if self.search_origin_in_subtree(node.left) or self.search_origin_in_subtree(node.right) else self.destination
        
        if node.val == self.origin:
            return -1 if self.search_destination_in_subtree(node.left, 'L') or self.search_destination_in_subtree(node.right, 'R') else self.origin
        
        left_result = self.traverse_tree(node.left)
        if left_result != 0:
            if left_result == -1:
                return -1
            if left_result == self.destination:
                self.path_array[self.end_ptr] = 'L'
                self.end_ptr -= 1
                return -1 if self.search_origin_in_subtree(node.right) else left_result
            else:
                self.path_array[self.start_ptr] = 'U'
                self.start_ptr += 1
                return -1 if self.search_destination_in_subtree(node.right, 'R') else left_result
        
        right_result = self.traverse_tree(node.right)
        if right_result != 0:
            if right_result == -1:
                return -1
            if right_result == self.destination:
                self.path_array[self.end_ptr] = 'R'
                self.end_ptr -= 1
            else:
                self.path_array[self.start_ptr] = 'U'
                self.start_ptr += 1
            return right_result
        
        return 0
    
    def search_origin_in_subtree(self, node):
        if not node:
            return False
        self.path_array[self.end_ptr] = 'U'
        self.end_ptr -= 1
        if node.val == self.origin:
            return True
        if self.search_origin_in_subtree(node.left) or self.search_origin_in_subtree(node.right):
            return True
        self.end_ptr += 1
        return False
    
    def search_destination_in_subtree(self, node, direction):
        if not node:
            return False
        self.path_array[self.start_ptr] = direction
        self.start_ptr += 1
        if node.val == self.destination:
            return True
        if self.search_destination_in_subtree(node.left, 'L') or self.search_destination_in_subtree(node.right, 'R'):
            return True
        self.start_ptr -= 1
        return False
