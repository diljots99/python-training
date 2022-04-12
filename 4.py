# Count Servers that Communice
def countserver(grid:list[list[int]]):
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
