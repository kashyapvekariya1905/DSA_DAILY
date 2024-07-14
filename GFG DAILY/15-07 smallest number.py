class Solution:
    def smallestNumber(self, s, d):
        # code here
        if s>9*d:
            return "-1"
        rst = ['0']*d
        for i in range(d-1,0,-1):
            if s>9:
                rst[i] = '9'
                s-=9
            else:
                rst[i] = str(s-1)
                s=1
        rst[0] = str(s)
        return ''.join(rst)
