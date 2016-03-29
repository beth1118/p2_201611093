import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.home()
t1.clear()
def makeswirlsSquare(size,bigger,sides,angle):
    for i in range(0,sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)
makeswirlsSquare(10,10,30,90)
wn.exitonclick()