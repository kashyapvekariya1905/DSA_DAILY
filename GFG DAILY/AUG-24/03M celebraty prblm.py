class Solution:
    def celebrity(self, mat):
        # code here 
        n = len(mat)
        degree = [[0,0] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    degree[i][0] += 1
                    degree[j][1] += 1 
        for i, deg in enumerate(degree):
            if deg == [0, n-1]:
                return i
        return -1
