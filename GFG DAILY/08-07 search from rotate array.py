class Solution:
    def search(self,arr,key):
        # Complete this function
        if key in arr:
            rst = arr.index(key)
            return rst
        else:
            return -1

def search_in_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == key:
            return mid
        
        if arr[start] <= arr[mid]:
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1

# Test cases
arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key1 = 10
print(search_in_rotated_array(arr1, key1))  # Output: 5

arr2 = [3, 5, 1, 2]
key2 = 6
print(search_in_rotated_array(arr2, key2))  # Output: -1
