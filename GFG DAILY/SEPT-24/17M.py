#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        n =len(arr)
        
        # Initialize the result with the difference between the highest and lowest value in the sorted array
        res = arr[-1] - arr[0]
        
        # Step 2: Calculate possible minimum difference after modifying the array
        for i in range(1, n):
            if arr[i] >= k:
                # Maximum and minimum possible values after modifying the array
                max_val = max(arr[i-1] + k, arr[-1] - k)
                min_val = min(arr[0] + k, arr[i] - k)
                res = min(res, max_val - min_val)
        
        return res