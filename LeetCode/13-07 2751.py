class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        lst = list(range(n))
        rst = []
        s = deque()
        lst.sort(key=lambda x: positions[x])
        for i in lst:
            if directions[i] == "R":
                s.append(i)
            else:
                while s and healths[i] > 0:
                    top = s.pop()
                    if healths[top] > healths[i]:
                        healths[top] -= 1
                        healths[i] = 0
                        s.append(top)
                    elif healths[top] < healths[i]:
                        healths[i] -= 1
                        healths[top] = 0
                    else:
                        healths[i] = 0
                        healths[top] = 0
        for i in range(n):
            if healths[i] > 0:
                rst.append(healths[i])
        return rst
