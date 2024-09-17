# User function Template for Python3

class Solution:
    def maxLength(self, str):
        # code here
        open, close, ans = 0, 0, 0
        for e in str:
            if e == '(':
                open += 1
            else:
                close += 1
            if open < close:
                open, close = 0, 0
            if open == close:
                ans = max(ans, open+close)
        
        open, close = 0, 0
        for e in str[::-1]:
            if e == '(':
                open += 1
            else:
                close += 1
            if open > close:
                open, close = 0, 0
            if open == close:
                ans = max(ans, open+close)
        return ans