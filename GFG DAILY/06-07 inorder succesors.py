class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None
        


class Solution:
    def __init__(self):
        self.prev = None
    def populateNext(self, root):
        if not root:
            return
        self.populateNext(root.left)
        if self.prev:
            self.prev.next = root
        self.prev = root
        self.populateNext(root.right)
