class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def isBSTUtil(root, min1, max1):
            if root is None:
                return True

            if root.data<=min1 or root.data>=max1:
                return False

            return isBSTUtil(root.left, min1, root.data) and isBSTUtil(root.right, root.data, max1)

        return isBSTUtil(root, float("-inf"), float("inf"))
