def threeSumClosest(arr, target):
    n = len(arr)
    if n < 3:
        return sum(arr) if arr else 0 
    arr.sort()
    cl = sum(arr[:3]) 
    for i in range(n-2):
        l = i + 1
        r = n - 1
        while l < r:
            cr = arr[i] + arr[l] + arr[r]
            if cr == target:
                return cr
            if abs(cr - target) < abs(cl - target):
                cl = cr
            elif abs(cr - target) == abs(cl - target):
                cl = max(cr, cl)
            if cr < target:
                l += 1
            else:
                r -= 1
    return cl

arr = [-7, 9, 8, 3, 1, 1]
target = 2
print(threeSumClosest(arr, target))
arr = [5, 2, 7, 5]
target = 13
print(threeSumClosest(arr, target))
