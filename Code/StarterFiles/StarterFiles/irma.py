import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    file=open("irma.csv",'r')

    for line in file:
        line=line.strip()
        line=line.split(",")
        if line[0]=="Date":
            continue
        if int(line[4])>157:
            t.pencolor("red")
            t.width(30)
            t.write("5", font=("Times New Roman",25))
        elif int(line[4])>130:
            t.pencolor("orange")
            t.width(25)
            t.write("4", font=("Times New Roman",25))
        elif int(line[4])>111:
            t.pencolor("yellow")
            t.width(20)
            t.write("3", font=("Times New Roman",25))
        elif int(line[4])>96:
            t.pencolor("green")
            t.width(15)
            t.write("2", font=("Times New Roman",25))
        elif int(line[4])>74:
            t.pencolor("blue")
            t.width(10)
            t.write("1", font=("Times New Roman",25))
        else:
            t.pencolor("white")
            t.width(5)
            t.write("", font=("Times New Roman",25))
        
        t.goto(float(line[3]),float(line[2]))
        
        
        

if __name__ == "__main__":
    irma()
