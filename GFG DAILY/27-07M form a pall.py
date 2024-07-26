class Solution:
    def countMin(self, str):
        # code here
        from functools import lru_cache
        import sys
        sys.setrecursionlimit(10**6)
        
        
        @lru_cache(None)
        def count(i, j):
            if i >= j:
                return 0
            if str[i] == str[j]:
                return count(i+1, j-1)
            return min(count(i+1, j), count(i, j-1)) + 1
        return count(0, len(str)-1)
