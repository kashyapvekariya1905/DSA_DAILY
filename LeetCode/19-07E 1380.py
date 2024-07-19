from typing import List
def luckyNumbers (matrix: List[List[int]]) -> List[int]:
    n = len(matrix)
    m = len(matrix[0])
    rmin = []
    for i in range(n):
        temp = float('inf')
        for j in range(m):
            temp = min(temp, matrix[i][j])
        rmin.append(temp)

    cmax = []
    for i in range(m):
        temp = float('-inf')
        for j in range(n):
            temp = max(temp, matrix[j][i])
        cmax.append(temp)
    rst = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == rmin[i] and matrix[i][j] == cmax[j]:
                rst.append(matrix[i][j])
    return rst

matrix = [[3,7,8],
          [9,11,13],
          [15,16,17]]
print(luckyNumbers(matrix))

matrix = [[1,10,4,2],
          [9,3,8,7],
          [15,16,17,12]]
print(luckyNumbers(matrix))

matrix = [[7,8],
          [1,2]]
print(luckyNumbers(matrix))
