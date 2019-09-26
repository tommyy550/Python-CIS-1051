def vowel(s):
    r=0
    for i in range(len(s)):
        if s[0]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            r=r+1
    return r

def evenNum(n):
    r=0
    x=str(n)
    for i in range(1,len(x)+1):
        #if (n%(10**i))%2==0:
        if n//10**i%10:
            r=r+1
    return r

def armstrong(n):
    x=0
    s=str(n)
    for i in range(len(s)):
        x=x+(int(s[i])**3)
    if n==x:
        return True
    else:
        return False


def batman():
    for i in range(1000,10000):
        ones=i%10
        tens=(i//10)%10
        huns=(i//100)%10
        thos=i//1000
        if ones!=tens and ones!=huns and ones!=thos and tens!=huns and tens!=thos and huns!=thos:
            if thos==3*tens:
                if ones%2==1:
                    if 27==ones+tens+huns+thos:
                        return i
    return -1
        
    
    
