def solve(n,m,mat):
    if not mat:
        return 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    rst = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if mat[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                rst = max(rst, dp[i][j])
    return rst
n = 6
m = 5
mat = [[0, 1, 1, 0, 1], 
       [1, 1, 0, 1, 0],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]
print(solve(n,m,mat))

n = 2
m = 2
mat = [[1, 1], 
       [1, 1]]
print(solve(n,m,mat))

n = 2
m = 2
mat = [[0, 0], 
       [0, 0]]
print(solve(n,m,mat))
