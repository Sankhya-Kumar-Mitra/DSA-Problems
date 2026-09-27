class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curArea = 0
        result = 0
        def dfs(i,j):
            nonlocal grid
            nonlocal curArea
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return
            grid[i][j]=0
            curArea+=1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curArea=0
                if grid[i][j]==1:
                    dfs(i,j)
                    result = max(result,curArea)
        return result
        