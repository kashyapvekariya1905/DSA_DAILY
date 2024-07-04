from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next 
        ns = modify
        while ns:
            total = 0
            while ns.val != 0:
                total += ns.val
                ns = ns.next
            modify.val = total
            ns = ns.next
            modify.next = ns
            modify = modify.next
        return head.next
