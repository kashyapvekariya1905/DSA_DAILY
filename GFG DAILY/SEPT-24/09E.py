class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        n = len(arr)
        
        #p1 is the start index of 1s and p2 is the start index 2s
        i, j = 0, n-1
        k = 0
        
        while k <= j:
            # have to use if else. can't use 3 if because after 1 if, the arr[k] change.
            if arr[k] == 0:
                arr[k], arr[i] = arr[i], arr[k]
                i += 1
                k += 1
            elif arr[k] == 2:
                arr[k], arr[j] = arr[j], arr[k]
                j -= 1
            else:
                k += 1