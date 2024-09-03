#User function Template for python3

class Solution:
	def nthStair(self,n):
	    steps=[1,2]
        dp=[0]*(n+1)
        dp[0]=1
        
        for step in steps:
            for target in range(1,n+1):
                if step<=target:
                    dp[target]+=dp[target-step]
                
        
        return dp[n]
        
        # Recursive approach
        
        dp={}
        def solve(i,j):
            if i>n:
                return 0
            
            if i==n or j==len(steps):
                return i==n
            
            if (i,j) in dp:
                return dp[(i,j)]
                
            dp[(i,j)]=solve(i+steps[j],j)+solve(i,j+1)
            
            return dp[(i,j)]
            
        
        return solve(0,0)