class Solution:
    def is_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False
        return self.is_bst(node.left, min_val, node.data) and self.is_bst(node.right, node.data, max_val)

    def get_tree_size(self, node):
        if node is None:
            return 0
        return 1 + self.get_tree_size(node.left) + self.get_tree_size(node.right)

    def get_bst_size(self, node):
        if node is None:
            return 0
        if self.is_bst(node, float('-inf'), float('inf')):
            return self.get_tree_size(node)
        return max(self.get_bst_size(node.left), self.get_bst_size(node.right))
    def largestBst(self, root):
        # Your code here
        return self.get_bst_size(root)
