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



def combinationSum(arr, sum):
	ans = []
	temp = []

	
	arr = sorted(list(set(arr)))
	findNumbers(ans, arr, temp, sum, 0)
	return ans

def findNumbers(ans, arr, temp, sum, index):
	
	if(sum == 0):
		
		
		ans.append(list(temp))  
		return
	
	
	for i in range(index, len(arr)):

		
		if(sum - arr[i]) >= 0:          # check for negativity

			# adding element which can equal to sum
			# sum
			temp.append(arr[i])
			findNumbers(ans, arr, temp, sum-arr[i], i)

			
			temp.remove(arr[i])



arr = [2, 3, 5]
sum = 8
ans = combinationSum(arr, sum)


if len(ans) <= 0:
	print("no combination find")
	

print(ans)

	


