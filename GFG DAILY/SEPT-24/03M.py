#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		# code here
		dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
		
		for i in range(len(s1)):
		    for j in range(len(s2)):
		        dp[i][j] = max(dp[i][j - 1] if j - 1 >= 0 else 0, dp[i-1][j] if i - 1 >= 0 else 0)
		        if s1[i] == s2[j]:
		            dp[i][j] = (dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0) + 1
        
        return len(s1) + len(s2) - 2 * dp[-1][-1]