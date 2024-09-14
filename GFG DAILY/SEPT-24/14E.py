#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        l = r = 0
        
        ln = len(arr)
        
        flag = True
        
        
        while r <ln:
            
            if flag:
                
                if arr[r] >=0:
                    
                    
                    temp = arr[r]
                    
                    for i in range(r,l-1, -1):
                        
                        arr[i] = arr[i-1]
                        
                        
                    arr[l] = temp
                    
                    l+=1
                    
                    r=l
                    
                    flag = False
                    
                    
                   
                    
                    
                    
                else:
                    
                    r+=1
                    
            else:
                
                if arr[r] < 0:
                    
                   
                    temp = arr[r]
                    
                    for i in range(r,l-1, -1):
                        
                        arr[i] = arr[i-1]
                        
                        
                    arr[l] = temp
                    
                    l+=1
                    
                    r=l
                    
                    flag = True
                    
                else:
                    
                    r+=1
                    
                    
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends