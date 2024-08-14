class Solution:
    def longest_common_substring(self, str1: str, str2: str) -> int:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(max_length, dp[i][j])

        return max_length

# Test cases
solution = Solution()
print(solution.longest_common_substring("ABCDGH", "ACDGHR"))  # Output: 4
print(solution.longest_common_substring("ABC", "ACB"))  # Output: 1