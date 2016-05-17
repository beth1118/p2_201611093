import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()

def background():
    t1.shape("turtle")
    t1.speed(2)
    t1.penup()
    t1.goto(-320,300)
    t1.clear()

def drawSquare():
    t1.penup()
    t1.goto(100,100)
    t1.pendown()
    for i in range(0,4):
        t1.fd(100)
        t1.left(90)
    t1.penup()

def drawLine1():
    t1.setheading(0)
    t1.penup()
    t1.goto(50,300)
    t1.pendown()
    t1.fd(100)
    t1.penup()

def drawLine2():
    t1.goto(200,350)
    t1.pendown()
    t1.setheading(270)
    t1.fd(100)
    t1.penup()
 
def drawCircle():
    t1.penup()
    t1.home()
    t1.pendown()
    t1.circle(100)
    t1.penup()

def cl(curpos):
    if 330<curpos[0]<390 and -250<curpos[1]<-150:
        t1.goto(-320,300)
        print "Good"

coord = [(100,100),(200,200)]
xs=coord[0][0]
ys=coord[0][1]
xe=coord[1][0]
ye=coord[1][1]

def isinRectangle(coord,curpos):
    if xs<=curpos[0]<=xe and ys<=curpos[1]<=ye:
        t1.color("pink")
        drawSquare()

line1=[(50,300),(150,300)]
x1=line1[0][0]-5
y1=line1[0][1]-5
x2=line1[1][0]+5
y2=line1[1][1]+5
pos1=(x1,y1)
pos2=(x2,y2)

def isOnLine1(curpos,pos1,pos2):
    if x1<=curpos[0]<=x2 and y1<=curpos[1]<=y2:
        t1.color("pink")
        drawLine1()

line2=[(200,300),(200,400)]
x3=line2[0][0]-5
y3=line2[0][1]-5
x4=line2[1][0]+5
y4=line2[1][1]+5
pos3=(x3,y3)
pos4=(x4,y4)

def isOnLine2(curpos,pos3,pos4):
    if x3<=curpos[0]<=x4 and y3<=curpos[1]<=y4:
        t1.color("pink")
        drawLine2()


circlepos=(0,100)
radious=100


def isinCircle(curpos,radious,circlepos):
    if math.sqrt(math.pow(curpos[0]-circlepos[0],2) + math.pow(curpos[1]-circlepos[1],2))<=100:
        t1.color("pink")
        drawCircle()

def Draw():
    background()
    drawSquare()
    drawLine1()
    drawLine2()
    drawCircle()

def keyup():
    t1.fd(50)
    curpos=t1.pos()
    cl(curpos)
    isinRectangle(coord,curpos)
    isOnLine1(curpos,pos1,pos2)
    isOnLine2(curpos,pos3,pos4)
    isinCircle(curpos,radious,circlepos)

Draw()
def keydown():
    t1.back(50)
def turnr():
    t1.right(90)
def turnl():
    t1.left(90)

def mousegoto(x,y):
    t1.setpos(x,y)
    curpos=t1.pos()
    cl(curpos)
    isinRectangle(coord,curpos)
    isOnLine1(curpos,pos1,pos2)
    isOnLine2(curpos,pos3,pos4)
    isinCircle(curpos,radious,circlepos)

def addkeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keydown, "Down")
    wn.onkey(turnr, "Right")
    wn.onkey(turnl, "Left")
def addmouse():
    wn.onclick(mousegoto)
addkeys()
addmouse()
wn.listen()
turtle.mainloop()