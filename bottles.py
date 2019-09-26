
def beer(n):   
    for x in range(n):
        print(str(n-x) + " bottles of bear on the wall, "+ str(n-x) + " bottles of beer")
        print("Take one down, pass it around " + str(n-x-1) + " bottles of beer on the wall.")

def math(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(str(i*j), end=" ")
        print()

def square(n):
    num=0
    for x in range(1,n+1):
        num+= x*x
    print(str(num))

def slash(n):
    for x in range(n):
        for i in range(x*2):
            print("\\",end=" ")
        for i in range(2+4*(n-(x+1))):
            print("!", end=" ")
        for i in range(x*2):
            print("/",end=" ")
        print("")

def glass():
    print("|", end = "")
    for x in range(10):
        print('"',end="")
    print("|")
    f=8
    for x in range(1,5):
        #put spaces
        print(" "*x,end="")
        for i in range(1):
            #print \\
            print("\\",end="")
        for j in range(f):
            #print :
            print(":",end="")
            
        for y in range(1):
            #print /
            print("/")
        # increment
        f=f-2
    print("     ||  ")

    f=2
    for x in range(4,-1,-1):
        print(" "*x,end="")
        for i in range(1):
            print("/",end="")
        for j in range(f):
            print(":",end="")
        for y in range(1):
            print("\\")
        f=f+2
    print("|", end = "")
    for x in range(10):
        print('"',end="")
    print("|")

    
    
                  

