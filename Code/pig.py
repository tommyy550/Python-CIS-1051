import random

def holdto20():
    score=0
    while(score<20):
        r=random.randint(1,6)
        #print("Roll: ",r)
        if r==1:
            score=0
            break
        score=score+r
    #print("Turn total: ",score)
    return score

def test():
    z=0
    tw=0
    tw1=0
    tw2=0
    tw3=0
    tw4=0
    tw5=0
    p=input("How many Hold-at-20 turn simulations?" )
    print("Score\tEstimated Probability")
    total=int(p)
    for x in range(total):
        n=holdto20()
        if n==0:
            z=z+1
        if n==20:
            tw=tw+1
        if n==21:
            tw1=tw1+1
        if n==22:
            tw2=tw2+1
        if n==23:
            tw3=tw3+1
        if n==24:
            tw4=tw4+1
        if n==25:
            tw5=tw5+1
    
    
            
    print("0\t",str(z/total))
          
    print("20\t",str(tw/total))
    print("21\t",str(tw1/total))
    print("22\t",str(tw2/total))
    print("23\t",str(tw3/total))
    print("24\t",str(tw4/total))
    print("25\t",str(tw5/total))

def checkWinner(one,two):
    if one>=100:
        print("Player one wins with "+str(one)+ " points.")
        return True
    if two>=100:
        print("Player two wins with "+str(two)+ " points.")
        return True
    return False
        
        
def holdatx():
    n=input("Enter a hold value" )
    hold=int(n)
    
    score=0
    z=0
    value=0
    for x in range(10000):
        while(score<=hold):
            r=random.randint(1,6)
            #print("Roll: ",r)
            if r==1:
                break
                z=z+1
            if r!=1:
                score=score+r
            if score>=hold:
                value=value+1
        #print("Turn total: ",score)
        score=0
    print("probability of getting hold value in one turn is ",str(value/10000))

def goal(currentScore):
    totalScore=currentScore
    score=0
    print("Score: ",str(totalScore))
    while score<20 and totalScore<100:
        r=random.randint(1,6)
        print("Roll: ",str(r))
        score=score+r
        if r==1:
            score=0
            break
    print("Turn total: ",str(score))
    print("New score: ",str(score+totalScore))
    return totalScore

def single():
    goal(0)
    
def play():
    player=random.randint(1,2)
    first=False
    if player==1:
        print("You will be player 1.")
        first=True
    if player==2:
        print("You will be player 2.")
        first=False

    print("Enter r to roll; enter h to hold.")
    p1=0
    p2=0
    endTurn=False
    score=0
    if first==True:
        while p1<100 and p2<100:
            print("Player 1 score: ",str(p1))
            print("Player 2 score: ",str(p2))
            print("It is player 1s turn.")
            while endTurn==False:
                
                
                text=input("r for roll and h for hold")
                if text=="r": #roll
                    r=random.randint(1,6)
                    if r==1:
                        print("Roll: ",str(r))
                        print("Turn total: ",str(0))
                        print("New score: ",str(p1))
                        endTurn=True
                        break
                        
                    else:
                        print("Roll: ",str(r))
                        score=score+r
                        
                if text=="h": #hold
                    p1=p1+score
                    print("Turn total: ",str(score))
                    print("New score: ",str(p1))
                    endTurn=True
                    break
            
            score2=0
            if checkWinner(p1,p2)== True:
                break
            #computer move
            score=0
            print("Player 1 score: ",str(p1))
            print("Player 2 score: ",str(p2))
            print("It is player 2s turn.")
            score2=0
            while score2<20 and p2<100:
                
                r=random.randint(1,6)
                print("Roll: ",str(r))
                if r==1:
                    print("Turn total: ",str(0))
                    print("New score: ",str(p2))
                    score2=0
                    endTurn=False
                    break
                else:
                    score2=score2+r
            p2=p2+score2      
            print("Turn total: ",str(score2))
            print("New score: ",str(p2))
            
            score2=0
            endTurn=False
            if checkWinner(p1,p2)== True:
                break




            
    else:#cpu goes first
        while p1<100 and p2<100:
            endTurn2=False
            #computer move           
            print("Player 1 score: ",str(p1))
            print("Player 2 score: ",str(p2))
            print("It is player 1s turn.")
            score2=0 
            while score2<20 and p1<100:
                
                r=random.randint(1,6)
                print("Roll: ",str(r))
                if r==1:
                    print("Turn total: ",str(0))
                    print("New score: ",str(p1))
                    score2=0
                    endTurn2=False
                    break
                else:
                    score2=score2+r
            p1=p1+score2      
            print("Turn total: ",str(score2))
            print("New score: ",str(p1))
            
            score2=0
            endTurn2=False
            if checkWinner(p1,p2)== True:
                break


        
        
            print("Player 1 score: ",str(p1))
            print("Player 2 score: ",str(p2))
            print("It is player 2s turn.")
            while endTurn2==False:
                
                
                text=input("r for roll and h for hold")
                if text=="r": #roll
                    r=random.randint(1,6)
                    if r==1:
                        print("Roll: ",str(r))
                        print("Turn total: ",str(0))
                        print("New score: ",str(p2))
                        endTurn2=True
                        break
                        
                    else:
                        print("Roll: ",str(r))
                        score=score+r
                        
                if text=="h": #hold
                    p2=p2+score
                    print("Turn total: ",str(score))
                    print("New score: ",str(p2))
                    endTurn2=True
                    break
            
            
            if checkWinner(p1,p2)== True:
                break
            score=0
        
#play()
test()           
            
        
        
            
                
                    
                    
                
                
                        
                
                
        
        




        
        
        
            


        
        

