from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        def solve(prev, curr, next):
            return (prev.val < curr.val > next.val) or (prev.val > curr.val < next.val)
        lst = []
        prev = head
        curr = head.next
        index = 1
        while curr and curr.next:
            if solve(prev, curr, curr.next):
                lst.append(index)
            prev = curr
            curr = curr.next
            index += 1
        if len(lst) < 2:
            return [-1, -1]
        mindst = float('inf')
        for i in range(1, len(lst)):
            mindst = min(mindst, lst[i] - lst[i-1])
        maxdst = lst[-1] - lst[0]
        return [mindst, maxdst]
