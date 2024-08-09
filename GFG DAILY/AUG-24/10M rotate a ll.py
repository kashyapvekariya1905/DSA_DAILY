
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        dummy = w = Node(-1)
        dummy.next = head
        
        while k > 0:
            w = w.next
            k -= 1
        
        if not w.next:
            return head
            
        ret = w.next
        w.next = None
        t = ret
        while t.next:
            t = t.next
        t.next = dummy.next
        return ret