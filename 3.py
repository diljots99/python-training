# Roman number to Integers 
def romantoint(s):
    
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ls=[]
    sum=0
    for i in roman:
        for j in s:
            if j==i:
                A=roman[j]
                ls.append(A)
            
    for k in range(0,len(ls)):
        sum=sum+ls[k]
    return sum
        
romantoint('VI')       
        
