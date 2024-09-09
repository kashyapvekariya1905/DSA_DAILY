#User function Template for python3

class Solution:
    def isCircle(self, arr):
        # code here
        from collections import defaultdict
        graph = defaultdict(list)
        mark = [0] * 26
        indegree = [0] * 26
        outdegree = [0] * 26
        vis = [0] * 26
        for i in range(N):
            s = A[i]
            u = ord(s[0]) - 97
            v = ord(s[len(s) - 1]) - 97
            indegree[u] += 1
            outdegree[v] += 1
            mark[u] = 1
            mark[v] = 1
            graph[u].append(v)
        def dfs(root):
            vis[root] = 1
            for node in graph[root]:
                if vis[node] == 0:
                    dfs(node)
        def safe(s):
            dfs(s)
            for i in range(26):
                if vis[i] == 0 and mark[i] == 1 : return False
            return True
        for i in range(26) :
            if indegree[i] != outdegree[i] : return 0
        if safe(ord(A[0][0]) - 97) == True : return 1
        return 0