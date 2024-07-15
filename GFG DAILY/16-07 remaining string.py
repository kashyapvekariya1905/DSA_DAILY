from typing import Counter


def printString(s, ch, count):
    occ = 0
    for i in range(len(s)):
        if s[i] == ch:
            occ+=1
            if occ == count:
                return s[i+1:]
    return ""

s = "Thisisdemostring"
ch = 'i'
count = 3
print(printString(s,ch,count))

s = "Thisisdemostri"
ch = 'i'
count = 3
