#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        max_element = max(arr)
    
    # Create a counting array to store the frequency of each element
        count = [0] * (max_element + 1)
    
    # Count the frequency of each element
        for num in arr:
            count[num] += 1
    
    # Find the kth smallest element
        current_count = 0
        for i in range(len(count)):
            current_count += count[i]
            if current_count >= k:
                    return i
    
    # If k is out of range, return -1 or raise an exception
        return -1