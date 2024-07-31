class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        lo = 0
        hi = min(len(s) for s in arr)
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            common = True
            for s in arr[1:]:
                if s[:mid] != arr[0][:mid]:
                    common = False
                    break
            if common:
                lo = mid
            else:
                hi = mid - 1
        return "-1" if lo == 0 else arr[0][:lo]
