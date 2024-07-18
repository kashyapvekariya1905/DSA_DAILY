def constructLowerArray(arr):
    def ms(enum):
        if len(enum) <= 1:
            return enum
        mid = len(enum) // 2
        left = ms(enum[:mid])
        right = ms(enum[mid:])
        return merge(left, right)
    def merge(left, right):
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    merged.append(left[i])
                    count[left[i][0]] += j
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            while i < len(left):
                merged.append(left[i])
                count[left[i][0]] += j
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged
    count = [0]*len(arr)
    enum = list(enumerate(arr))
    ms(enum)
    return count

arr = [12, 1, 2, 3, 0, 11, 4]
arr = [1,2,3,4,5]
print(constructLowerArray(arr))
