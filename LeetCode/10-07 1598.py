class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0
        for log in logs:
            if log == '../':
                if step > 0:
                    step -= 1
            elif log != './':
                step += 1
        return step
