import turtle

t=turtle.Turtle()
t.shape("turtle")

def olympics(bob):
    bob.reset()
    t.width(10)
    
    bob.color("blue")
    bob.up()
    bob.goto(-120,0)
    bob.down()
    bob.circle(50)

    bob.color("black")
    bob.up()
    bob.goto(0,0)
    bob.down()
    bob.circle(50)

    bob.color("red")
    bob.up()
    bob.goto(120,0)
    bob.down()
    bob.circle(50)

    bob.color("yellow")
    bob.up()
    bob.goto(-60,-60)
    bob.down()
    bob.circle(50)

    bob.color("green")
    bob.up()
    bob.goto(60,-60)
    bob.down()
    bob.circle(50)

def nshape(bob):
    bob.reset()
    text=input("Enter number of sides: ")
    number=int(text)  
    for x in range(number):
        bob.fd(50)
        bob.left(360/number)

def clock(bob):
    bob.reset()
    bob.left(90)
    for x in range(12):
        bob.up()
        bob.forward(50)
        bob.down()
        bob.forward(50)
        bob.stamp()
        bob.up()
        bob.backward(100)
        bob.right(30)

def initials(bob):
    #draws "T"
    bob.reset()
    bob.forward(100)
    bob.backward(50)
    bob.right(90)
    bob.forward(100)
    #draws "H"
    bob.up()
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.down()
    bob.forward(100)
    bob.backward(50)
    bob.right(90)
    bob.forward(50)
    bob.left(90)
    bob.forward(50)
    bob.backward(100)

