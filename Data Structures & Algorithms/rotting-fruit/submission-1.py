class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        totalFresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    totalFresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
                    
        curTime = 0
        changeMade = 0
        while q:
            l = len(q)
            changeMade=0
            for i in range(l):
                row,col = q.popleft()
                for dr,dc in direction:
                    newRow = row+dr
                    newCol = col+dc
                    if 0<=newRow<m and 0<=newCol<n and grid[newRow][newCol]==1:
                        grid[newRow][newCol]=2
                        q.append([newRow,newCol])
                        changeMade+=1
                        totalFresh-=1
            if changeMade!=0:
                curTime+=1
        return curTime if totalFresh==0 else -1



