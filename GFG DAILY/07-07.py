class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def Ancestors(self, root, target):
        def dfs(node, path):
            if node is None:
                return None
            if node.data == target:
                return path[::-1]  
            path.append(node.data)
            left_result = dfs(node.left, path)
            if left_result:
                return left_result
            right_result = dfs(node.right, path)
            if right_result:
                return right_result
            
            path.pop()
            return None
        result = dfs(root, [])
        if result:
            print(*result, end="")
        return result or [] 

# Function to build the tree
def buildTree(s):
    if not s or s[0] == 'N':
        return None
    
    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    size = 0
    q = []
    q.append(root)

    size += 1
    i = 1
    while size > 0 and i < len(ip):
        currNode = q[0]
        q.pop(0)
        size -= 1
        
        currVal = ip[i]
        
        if currVal != "N":
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size += 1
        
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        if currVal != "N":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size += 1
        i += 1
    
    return root

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        target = int(input())
        ob = Solution()
        ob.Ancestors(root, target)
        print()  # Print newline after each test case
