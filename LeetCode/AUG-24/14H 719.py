from typing import List


def smallestDistancePair(nums: List[int], k: int) -> int:
    def solve(dist):
        count = left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > dist:
                left += 1
            count += right - left
        return count
    nums.sort()
    lo, hi = 0, nums[-1] - nums[0]
    while lo < hi:
        mid = (lo + hi) // 2
        if solve(mid) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo

nums = [1,3,1]
k = 1
print(smallestDistancePair(nums,k))

nums = [1,1,1]
k = 2
print(smallestDistancePair(nums,k))

nums = [1,6,1]
k = 3
print(smallestDistancePair(nums,k))
