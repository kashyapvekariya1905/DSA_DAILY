class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and not visited[x][y]
        
        def dfs(x, y, path):
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return
            
            visited[x][y] = True
            
            for move, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if is_safe(nx, ny):
                    dfs(nx, ny, path + move)
            
            visited[x][y] = False
        
        if not m or m[0][0] == 0 or m[-1][-1] == 0:
            return []
        
        n = len(m)
        paths = []
        visited = [[False] * n for _ in range(n)]
        directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        
        dfs(0, 0, "")
        return sorted(paths)
