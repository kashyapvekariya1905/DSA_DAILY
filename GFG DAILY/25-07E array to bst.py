#User function Template for python3
class Solution:
    def sortedArrayToBST(self, nums):
        # code here
        n=len(nums)
        temp=[Node(nums[i]) for i in range(0,n)]
        mid=n//2
        i=1
        while i<n:
            temp[i].left=temp[i-1]
            if i+1<n:
                temp[i].right=temp[i+1]
            i+=2
        return temp[mid]
