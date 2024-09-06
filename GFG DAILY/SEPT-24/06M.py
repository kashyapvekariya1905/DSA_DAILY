#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        running, s = 0, float('-inf')
        for e in arr:
            running += e
            s = max(s, running)
            running = max(running, 0)
            
        return s
