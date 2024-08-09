
class Solution:
    def Maximize(self, a): 
        # Complete the function
        a.sort()
        return sum([a[i] * i for i in range(len(a))]) % (10 ** 9 + 7)
      
