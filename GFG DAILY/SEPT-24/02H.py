import heapq

class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        # Direction vectors for moving left, right, up, and down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Distance matrix initialized with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        
        # Min-heap to store (cost, x, y)
        pq = [(grid[0][0], 0, 0)]
        
        while pq:
            current_cost, x, y = heapq.heappop(pq)
            
            # If we reached the bottom-right cell
            if x == n - 1 and y == n - 1:
                return current_cost
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # If the neighbor is within bounds
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = current_cost + grid[nx][ny]
                    
                    # If a cheaper path to (nx, ny) is found
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        
        return dist[n - 1][n - 1]

# Example usage:
# grid1 = [[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]]
# grid2 = [[4, 4], [3, 7]]
# sol = Solution()
# print(sol.minimumCostPath(grid1))  # Output: 43
# print(sol.minimumCostPath(grid2))  # Output: 14
