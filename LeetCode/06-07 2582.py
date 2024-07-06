def passThePillow(n: int, time: int) -> int:
    ct = 2*(n-1)
    rt = time%ct
    if rt<n:
        return rt+1
    return n-rt+n-1

n = 4
time = 5
n = 3
time = 2
print(passThePillow(n,time))
