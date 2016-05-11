import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def line(size,pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.fd(size)

t1.penup()
t1.goto(-200,0)

line(50,(200,0))


t1.penup()
t1.goto(-200,0)
x=float()
y=float()
score=0
def k1():
    global score
    (x,y)=t1.pos()
    t1.fd(40)
    if (150<x<200 and y==0):
        print "good"
        t1.goto(-200,0)

        wn.bye()
def k2():
    t1.left(45)
def k3():
    t1.right(45)
def k4():
    t1.bk(40)
wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")
wn.listen()
wn.exitonclick()