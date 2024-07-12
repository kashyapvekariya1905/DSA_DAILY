def maximumGain(s: str, x: int, y: int) -> int:
    a = 0
    b = 0
    less = min(x,y)
    rst = 0
    for i in s:
        if i>'b':
            rst+=min(a,b)*less
            a = 0
            b = 0
        elif i=='a':
            if x<y and b>0:
                b-=1
                rst+=y
            else:
                a+=1
        elif i == 'b':
            if y<x and a>0:
                a-=1
                rst+=x
            else:
                b+=1
    rst += min(a,b)*less
    return rst


s = "cdbcbbaaabab"
x = 4
y = 5
print(maximumGain(s, x, y))
s = "aabbaaxybbaabb"
x = 5
y = 4
print(maximumGain(s, x, y))
