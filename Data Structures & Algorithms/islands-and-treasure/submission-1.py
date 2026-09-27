class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        visited = [[float('inf')]*n for _ in range(m)]
        q = deque()
        dir = [[0,-1],[0,1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited[i][j]=0
        curDist = 1
        while q:
            l=len(q)
            
            for i in range(l):
                row,col = q.popleft()
                for dr,dc in dir:
                    newRow = row+dr
                    newCol = col+dc
                    if 0<=newRow<m and 0<=newCol<n and visited[newRow][newCol]==float('inf') and grid[newRow][newCol]!=-1:
                        visited[newRow][newCol]=curDist
                        q.append([newRow,newCol])
            curDist+=1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2147483647 and visited[i][j]!=float('inf'):
                    grid[i][j]=visited[i][j]
        