#User function Template for python3

class Solution:
    def minTime(self, root,target):
        # code here
        parent={}
        res=[root]
        while res:
            a=res.pop(0)
            if a.left:
                parent[a.left]=a
                res.append(a.left)
            if a.right:
                parent[a.right]=a
                res.append(a.right)
        queue=[]
        def inorder(root):
            if root and root.data==target:
               queue.append([root,0])
            else:
                if root:
                    inorder(root.left)
                    inorder(root.right)
        inorder(root)
        vis={queue[0][0]:1}
        maxi=0
        while queue:
            for i in range((len(queue))):
                a=queue.pop(0)
                node=a[0]
                count=a[1]
                maxi=max(maxi,count)
                if node in parent and parent[node] not in vis:
                    vis[parent[node]]=1
                    queue.append([parent[node],count+1])
                if node.left and node.left not in vis:
                    vis[node.left]=1
                    queue.append([node.left,count+1])
                if node.right and node.right not in vis:
                    vis[node.right]=1
                    queue.append([node.right,count+1])
        return maxi
