import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def square(size,pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    for i in range(4):
        t1.fd(size)
        t1.right(90)
t1.shape("turtle")
wn.bgcolor("Pink")
t1.pencolor("black")
t1.fillcolor("White")
t1.penup()
t1.goto(-200,0)
t1.write("START!")
square(30,(250,0))
square(25,(100,150))
square(50,(50,-200))
square(75,(-50,100))
print "your score is 0"
t1.penup()
t1.goto(-200,0)
x=float()
y=float()
score=0
def k1():
    global score
    (x,y)=t1.pos()
    t1.fd(10)
    if (250<x<280 and -30<y<0):
        score+=20
        print "Score=> %d " % score
        t1.goto(-200,0)
    if (100<x<125 and 125<y<150):
        score+=40
        print "Score=> %d " % score
        t1.goto(-200,0)
    if (50<x<100 and -250<y<-200):
        score+=10
        print "Score=> %d " % score
        t1.goto(-200,0)
    if (-50<x<25 and 25<y<100):
        score+=40
	print "Score=> %d" % score
        t1.goto(-200,0)
    if (score>100):
        print "game finished"
        wn.bye()
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
wn.exitonclick()