#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        a = str.split(".")
        b = []
        t = "true"
        f = "false"
        if len(a)==4:
            for i in a:
                a = i
                a = int(a)
                b.append(a)
            if (b[0]<=255 and b[1]<=255) and (b[2]<=255 and b[3]<=255):
                return t
        else:
            return f