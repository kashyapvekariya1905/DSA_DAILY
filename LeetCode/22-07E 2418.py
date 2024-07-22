from typing import List
def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    hn = {heights[i]: names[i] for i in range(len(names))}
    heights.sort()
    result = []
    for height in reversed(heights):
        result.append(hn[height])
    return result

names = ["Mary","John","Emma"]
heights = [180,165,170]
names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(sortPeople(names,heights))
