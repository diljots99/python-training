# Count Servers that Communicate
class Solution:
    def countServers(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                var= grid[i][j]
                if var==1:
                    for m in range(len(grid)):
                        if m ==j and m==i:
                            continue
                        elif var==grid[i][m] or var==grid[m][j]:
                            count+=1
                            break
        return count

n = int(input())
grid = [list(map(int,input().split(" "))) for i in range(n)]
obj=Solution()
obj.countServers(grid)
