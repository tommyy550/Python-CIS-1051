def isLeapYear(year):
    

date=input("Please enter a date")
day=int(input[0:2])
month=int(input[3:5])
year=int(input[6:10])

if month==4 or month==6 or month==9 or month==11:
    if 1<=day<=30:
        print("valid")
    else:
        print("invalid date due to day")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    if 1<=day<=31:
        print("valid")
    else:
        print("invalid date due to day")

elif month=2:
    if 1<=day<=28:
        print("true")
   elif day==29:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    print("valid")
                else:
                    print("invalid")
            else:
                print("valid")
        elif:
            print("invalid, not a leap year")
    else:
        print("invalid day")
else:
    print("invalid due to month")

    
           
