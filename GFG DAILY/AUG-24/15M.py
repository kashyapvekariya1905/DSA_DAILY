
'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        number = 0
        while head:number, head = number * 10 + head.data, head.next
        return Node(number+1)
