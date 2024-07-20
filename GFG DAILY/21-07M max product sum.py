import sys

class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        mod = 10**9 + 7
        zc = 0
        nc = 0
        product = 1
        mn = -sys.maxsize - 1
        n = len(arr)
        if n == 1:
            return arr[0]
        for i in range(n):
            if arr[i] == 0:
                zc += 1
                continue
            if arr[i] < 0:
                nc += 1
                mn = max(mn, arr[i])
            product = (product * arr[i]) % mod
        if zc == n or (zc == n - 1 and nc == 1):
            return 0
        if nc % 2 != 0:
            product = (product * pow(mn, mod - 2, mod)) % mod
        return product
    
