# Roman number to Integers def romanInt(s):
def romanInt(s):
    """
    :type s:str
    :rtype:int
    """
    r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    
    n=0
    j=9999
    for i in range(len(s)):
        p=r[s[i]]
        if j<p:
            n=n-j+p-j
        else:
            n=n+p
        j=p
    return n
s=input()
print(romanInt(s))
        


