#User function Template for python3

from typing import List

class Solution:
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        # Your implementation here
        from collections import defaultdict
        graph = defaultdict(set)
        in_degree = {chr(i + ord('a')): 0 for i in range(K)}
        
        # Build the graph
        for i in range(N - 1):
            word1, word2 = alien_dict[i], alien_dict[i + 1]
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_degree[c2] += 1
                    break
        
        # Perform topological sort
        queue = [c for c in in_degree if in_degree[c] == 0]
        order = []
        
        while queue:
            c = queue.pop(0)
            order.append(c)
            for neighbor in graph[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all characters are included
        if len(order) < K:
            return ""
        
        return ''.join(order)