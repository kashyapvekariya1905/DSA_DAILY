def getSmallestString(s: str) -> str:
    char = list(s)
    n = len(char)
    for i in range(n-1):
        if int(char[i])%2 == int(char[i+1])%2:
            if char[i]>char[i+1]:
                char[i],char[i+1] = char[i+1],char[i]
                return ''.join(char)
    return s

s = "45320"
print(getSmallestString(s))
s = "001"
print(getSmallestString(s))
