# Two Sums
def twosum(num,target):

    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            if target-num[i]==num[j]:
                return([i,j])

               
num=[1,3,4,2,5,3,2]
target=4
print(twosum(num,target))