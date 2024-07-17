class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, nums):
       #code here
        positives=0
        negatives=0
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>ans:
                positives=negatives+1
                ans=nums[i]
            elif nums[i]<ans:
                negatives=positives+1
                ans=nums[i]
        return max(positives,negatives)+1
