#takes 3 number inputs and sorts them in order
def sort():
    number1=input("enter number 1: \n")
    number2=input("enter number 2: \n")
    number3=input("enter number 3: \n")

    if number1>number2 and number1>number3:
        if number2>number3:
            print(number3,number2,number1)
        else: print(number2,number3,number1)
    if number2>number1 and number2>number3:
        if number1>number3:
            print(number3,number1,number2)
        else: print(number1,number3,number2)
    if number3>number2 and number3>number1:
        if number2>number1:
            print(number1,number2,number3)
        else: print(number2,number1,number3)

#converts celcius to F
def convert():
    text=input("Enter temp in celcius: ")
    f= float(text)*(9/5)+32
    print("that temp in F is ", f)

#converts seconds to hours,mins, and seconds
def time():
    text=input("Enter seconds to be converted: ")
    time=float(text)
    h=int(time/3600)
    m=int(time/60)%60
    s= int(time%60)
    print(h," hours ",m," minutes ",s," seconds") 
    


    
        
    
