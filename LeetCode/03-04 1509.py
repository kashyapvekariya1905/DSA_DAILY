from typing import List


def minDifference(nums: List[int]) -> int:
    return 0 if len(nums)<=4 else nums.sort() or min(nums[len(nums)-4+i]-nums[i] for i in range(4))

nums = [5,3,2,4]
print(minDifference(nums))
nums = [1,5,0,10,14]
print(minDifference(nums))
nums = [3,100,20]
print(minDifference(nums))
