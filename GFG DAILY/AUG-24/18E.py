class Solution:
    def canSplit(self, arr):
        #code here
        su = sum(arr)
        k = 0
        for i in arr:
            k += i
            su -= i
            if k == su:
                return True
        return False