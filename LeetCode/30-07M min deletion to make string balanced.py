class Solution:
    def minimumDeletions(self, s: str) -> int:
        c = 0
        min_del = 0
        for char in s:
            if char == 'a':
                min_del = min(min_del + 1, c)
            else:
                c += 1   
        return min_del