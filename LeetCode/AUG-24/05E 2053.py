from typing import List


def kthDistinct(arr: List[str], k: int) -> str:
    occ = {}
    for i in arr:
        if i in occ:
            occ[i] += 1
        else:
            occ[i] = 1
    lst = []
    for f,v in occ.items():
        if v == 1:
            lst.append(f)
    if len(lst)<k:
        return ""
    print(lst[k-1])

arr = ["d","b","c","b","c","a"]
k = 2
print(kthDistinct(arr,k))
arr = ["aaa","aa","a"]
k = 1
print(kthDistinct(arr,k))

arr = ["a","b","a"]
k = 3
print(kthDistinct(arr,k))
