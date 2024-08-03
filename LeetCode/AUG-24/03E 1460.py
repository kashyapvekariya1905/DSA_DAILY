class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        
        count = Counter(target)
        for num in arr:
            count[num] -= 1
        
        return all(count[num] == 0 for num in count)
