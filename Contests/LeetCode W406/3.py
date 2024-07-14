from typing import List


def minimumCost(m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
    mod = 10**9+7
    horizontalCut.sort(reverse=True)
    verticalCut.sort(reverse=True)
    a = 0
    b = 0
    hp = 1
    vp = 1
    rst = 0
    while a<len(horizontalCut) and b<len(verticalCut):
        if horizontalCut[a]>verticalCut[b]:
            rst+=horizontalCut[a]*vp
            hp+=1
            a+=1

        else:
            rst+=verticalCut[b]*hp
            vp+=1
            b+=1

    while b<len(verticalCut):
        rst+=verticalCut[b]*hp
        b+=1

    while a<len(horizontalCut):
        rst+=horizontalCut[a]*vp
        a+=1

    return rst%mod


m = 3
n = 2
horizontalCut = [1,3]
verticalCut = [5]
print(minimumCost(m, n, horizontalCut, verticalCut))
m = 2
n = 2
horizontalCut = [7]
verticalCut = [4]
print(minimumCost(m, n, horizontalCut, verticalCut))
