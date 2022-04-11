# Combination Sum
 
from itertools import combinations
def combinationsum(array,x):
    b=[]
    for i in range(len(array)+1):
        for subset in combinations(array,i):
            if sum(subset)==x:
                
                a=list(subset)
                b.append(a)
    print(b)

array=[10,20,30,40,50,60,70,80,90]
x=80
combinationsum(array,x)

