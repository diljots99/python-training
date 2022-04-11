# Combination Sum
def combinationSum(n, t):
    r = []
    u={}
    n = list(set(n))
    solve(n,t,r,u)
    return r
def solve(n,t,r,u,i = 0,c=[]):
    if t == 0:
        temp = [i for i in c]
        temp1 = temp
        temp.sort()
        temp = tuple(temp)
        if temp not in u:
            u[temp] = 1
            r.append(temp1)
        return
    if t <0:
        return
    for x in range(i,len(n)):
        c.append(n[x])
        solve(n,t-n[x],r,u,i,c)
        c.pop(len(c)-1)
n=list(map(int,input().split()))
t=int(input())
print(combinationSum(n,t))