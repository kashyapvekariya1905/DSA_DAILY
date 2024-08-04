from typing import List


def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    mod = 10**9+7
    lst = [0] * (n*(n+1)//2)
    ind = 0
    for i in range(n):
        csum = 0
        for j in range(i,n):
            csum+=nums[j]
            lst[ind] = csum
            ind+=1
    s = 0
    lst.sort()
    for i in range(left-1,right):
        s+=lst[i]
    return (s%mod)
nums = [1,2,3,4]
n = 4
left = 1
right = 5
print(rangeSum(nums, n, left, right))
