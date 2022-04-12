# Combination Sum
from itertools import combinations
def combinationsum(candidate,target):
    ls1=[]
    for i in range(len(candidate)+1):
        for j in combinations(candidate,i):
            if sum(j)==target:
                ls1.append(j)
    print(ls1) 
    
    
combinationsum([1,2,3,5],5)     