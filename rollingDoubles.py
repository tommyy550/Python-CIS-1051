import random

def db():
    first=random.randint(1,6)
    second=random.randint(1,6)
    if first==second:
        return True
    else:
        return False

def play():
    one=0
    two=0
    three=0
    none=0
    num=10000
    for i in range(10000):
        
        if db()==True:

            if db()==True:
                if db()==True:
                    three+=1
                else:
                    two+=1
            else:
                one+=1
                
        else:
            none+=1

    print(str(one/num))
    print(str(two/num))
    print(str(three/num))
    print(str(none/num))
        
            
