from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        se = set(nums)
        d = ListNode(0)
        d.next = head
        prev = d
        cur = head
        while cur:
            if cur.val in se:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return d.next

s = Solution()
nums = [1,2,3]
head = [1,2,3,4,5]

print(s.modifiedList(nums,head))
nums = [1]
head = [1,2,1,2,1,2]
print(s.modifiedList(nums,head))

nums = [5]
head = [1,2,3,4]
print(s.modifiedList(nums,head))
