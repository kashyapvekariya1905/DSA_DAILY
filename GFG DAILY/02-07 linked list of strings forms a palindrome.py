'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

def check(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
    
def compute(head): 
    #return True/False
    rst = ""
    current = head
    while current:
        rst += current.data
        current = current.next
    return check(rst)

