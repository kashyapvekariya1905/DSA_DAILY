class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        # code here
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum
