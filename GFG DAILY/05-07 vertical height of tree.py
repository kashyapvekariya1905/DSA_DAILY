class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def verticalWidth(self, root):
        if not root:
            return 0
        minh = float('inf')
        maxh = float('-inf')
        def inorder(node, hd):
            nonlocal minh, maxh
            if not node:
                return
            minh = min(minh, hd)
            maxh = max(maxh, hd)
            inorder(node.left, hd - 1)
            inorder(node.right, hd + 1)
        inorder(root, 0)
        return maxh - minh + 1
def build_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = Node(nodes[index])
    root.left = build_tree(nodes, 2 * index + 1)
    root.right = build_tree(nodes, 2 * index + 2)
    return root

# Test the solution
if __name__ == "__main__":
    # Test case 1
    nodes1 = [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, None, 9]
    root1 = build_tree(nodes1)
    sol = Solution()
    print("Vertical width of tree 1:", sol.verticalWidth(root1))  # Expected output: 6

    # Test case 2
    nodes2 = [1, 2, 3]
    root2 = build_tree(nodes2)
    print("Vertical width of tree 2:", sol.verticalWidth(root2))  # Expected output: 3
