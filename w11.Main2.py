import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("Maze.gif")
t1.penup()
t1.goto(-300,300)

def k1():
    t1.fd(50)
def k2():
    t1.left(45)
def k3():
    t1.right(45)
def k4():
    t1.bk(50)
wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")
wn.listen()

def mousegoto(x,y):
    msg="mouse clicked {0} {1}".format(x,y)
    wn.title(msg)
    t1.setpos(x,y)

def addMouse():
    wn.onclick(mousegoto) 

wn.exitonclick()