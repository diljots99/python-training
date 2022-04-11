# Count Servers that Communicate
class solution:
    
    def countserver(self,grid:list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        rows=[0]*m
        cols=[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rows[i]=rows[i]+1
                    cols[j]=cols[j]+1

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (rows[i]>1 or cols[j]>1):
                    ans=ans+1
            return ans
