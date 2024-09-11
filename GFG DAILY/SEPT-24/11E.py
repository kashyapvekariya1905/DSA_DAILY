#User function Template for python3
from typing import List
import heapq

class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
    
        heapq.heapify(arr)
        total_cost = 0
        
        # Continue until there's only one rope left
        while len(arr) > 1:
            # Extract the two shortest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # Combine these ropes and calculate the cost
            combined_length = first + second
            total_cost += combined_length
            
            # Add the combined rope back to the heap
            heapq.heappush(arr, combined_length)
        
        return total_cost
