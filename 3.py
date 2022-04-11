# Roman number to Integers 
def romantoint(A):
    d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    previous='I'
    result=0
    for current in A[::-1]:
        if(d[current]<d[previous]):
            result=result-d[current]

        else:
            result=result+d[current]

        previous=current
    return result


romantoint("LVIII")