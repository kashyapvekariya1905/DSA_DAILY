# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        # code here 
        v=str.split('.')
        v=v[::-1]
        return '.'.join(v)