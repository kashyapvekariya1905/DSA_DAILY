class Solution:
    def kPangram(self,string, k):
    # code here
        s = set()
        charCount =0
        for each in string:
            if each!=' ':
                s.add(each)
                charCount +=1
        unique = len(s)
        duplicate = charCount-unique
        required = 26-unique
        if duplicate>=required and required<=k:
            return True
        return False
