#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        dummy = prev_copy = Node(-1)
        node = head
        while node:
            copy_node = Node(node.data)
            copy_node.random = node.random
            node._copy = copy_node
            prev_copy.next, prev_copy = copy_node, copy_node
            node = node.next
        copy_node = dummy.next
        while copy_node:
            if copy_node.random:
                copy_node.random = copy_node.random._copy
            copy_node = copy_node.next
        return dummy.next
    