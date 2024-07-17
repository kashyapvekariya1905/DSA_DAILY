# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        tds = set(to_delete)
        res = []
        def solve(root, is_root):
            if not root:
                return None
            rd = root.val in tds
            if is_root and not rd:
                res.append(root)
            root.left = solve(root.left, rd)
            root.right = solve(root.right, rd)
            return None if rd else root
        solve(root, True)
        return res
