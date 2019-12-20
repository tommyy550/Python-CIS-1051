data=open("xxx",'r')

text=data.readlines()
count={}
count["luck"]=0

for line in text:
    words = line.split(" ")
    for word in words:
        word=word.lower()
        word.word.strip()
        if word in count:
            count[word]=count[word]+1

//seeing frequency of characters
for line in text:
    for char in line:
        if char not in count:
            count[char]=1
        else:
            count[char]=count[char]+1

//turtle moving ex: l 90
commands=open("trutle boss.commands",'r')
bob=trutle.Turtle()

for line in commands:
    parts=line.split()
    command=parts[0]
    amount=int(parts[1])

    if command=='f':
        bob.right(amount)
    ---
    ---

//writing filter            w=writec a=append(adds onto a file)
target=open("myFirstFile.txt","w")
target.write("hello")

//graphs
import altair

x_vals=[]
y_vals=[]

for x in range(-10,11):
    x_vals.append(x)
    y_vals.append(x**2)
    print(x,x**2)
data=altair.Data(X=x_vals,Y=y_vals)
print(data)
    
    
    
