class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        mp={}
        mmax=0
        directions=((0,1),(1,0),(0,-1),(-1,0))
        def solve(i,j):
            ans=1
            seen=set()
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]>1:
                    id=grid[ni][nj]
                    if id not in seen:
                        ans+=mp[id]
                        seen.add(id)
            return ans
        def dfs(i,j,id):
            nonlocal cnt
            cnt+=1
            grid[i][j]=id
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                    dfs(ni,nj,id)
        id=2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    cnt=0
                    dfs(i,j,id)
                    mp[id]=cnt
                    id+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    mmax=max(mmax,solve(i,j))
        return mmax if mmax>0 else m*n

