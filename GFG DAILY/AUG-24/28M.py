#User function Template for python3
 
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        #code here
        temp = {}
        for i in arr: temp[i] = temp.get(i, 0)+1
        temp2 = [[i, temp[i]] for i in temp]
        temp2.sort(key = lambda i:(-i[1], i[0]))
        temp3 = []
        for x, y in temp2: temp3.extend([x]*y)
        return temp3