class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        def solve(i, j, temp_grid):
            if i < 0 or i >= m or j < 0 or j >= n or temp_grid[i][j] == 0:
                return
            temp_grid[i][j] = 0
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                solve(i + di, j + dj, temp_grid)
        
        def count():
            temp_grid = [row[:] for row in grid]  
            c = 0
            for i in range(m):
                for j in range(n):
                    if temp_grid[i][j] == 1:
                        solve(i, j, temp_grid)
                        c += 1
            return c
        
        isLand = count()
        if isLand != 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    isLand = count()
                    if isLand != 1:
                        return 1
                    grid[i][j] = 1
        
        return 2