class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        clst = nums[0]
        mind = abs(nums[0])
        for i in nums:
            dst = abs(i)
            if dst<mind or (dst==mind and i>clst):
                clst = i
                mind = dst
        return clst
