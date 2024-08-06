
class Solution:
    def kthElement(self, k, arr1, arr2):
        
        arr = arr1+arr2
        return sorted(arr)[k-1]
        