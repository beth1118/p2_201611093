import turtle
import time
wn=turtle.Screen()
t1=turtle.Turtle()
import math
def square(size,pos,color):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.begin_fill()
    for i in range(4):
        t1.fd(size)
        t1.right(90)
    t1.fillcolor(color)
    t1.end_fill()
def Circle(size,pos,color):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.begin_fill()
    t1.circle(size)
    t1.fillcolor(color)
    t1.end_fill()
    t1.penup()

def makeSwirlSquare(size,bigger,turns,angle,pos):
    nBigger=2
    t1.goto(pos)
    t1.pendown()
    t1.pencolor("skyblue")
    for i in range(0,turns):
        if not i%nBigger:
            size+=bigger
        t1.forward(size)
        t1.right(angle)


        
            

t1.shape("turtle")
wn.bgcolor("Pink")
t1.pencolor("skyblue")
t1.fillcolor("White")
t1.penup()
t1.goto(-200,0)
t1.write("START!")
square(40,(250,0),"skyblue")
square(35,(100,150),"skyblue")
square(50,(50,-200),"skyblue")
square(75,(-50,100),"skyblue")
square(45,(-250,60),"skyblue")
square(40,(-150,-170),"skyblue")
Circle(30,(0,-140),"skyblue")
Circle(40,(200,50),"skyblue")
Circle(45,(-200,100),"skyblue")
Circle(50,(-230,-150),"skyblue")
square(25,(210,-140),"skyblue")
makeSwirlSquare(20,30,11,90,(200,-130))
print "your score is 0"
t1.penup()
t1.goto(-200,0)
x=float()
y=float()
score=0
def SCORE():
    played=open('gamescore.txt','a')
    if score>=100:
        name = raw_input("Put in your name: ")
        msg='played {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print("End Game"+'\n'+'Score' + '\t'+ str(score) +'\t' + msg)
        played.write('\n' + 'Score' + '\t'+ str(score) +'\t' + msg)
        played.close()
    if score<=-50:
        name = raw_input("Put in your name: ")
        msg='played {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print("End Game"+'\n'+'Score' + '\t'+ str(score) +'\t' + msg)
        played.write('\n' + 'Score' + '\t'+ str(score) +'\t' + msg)
        played.close()
def k1():
    global score
    (x,y)=t1.pos()
    curpos=t1.pos()
    x1=curpos[0]
    y1=curpos[1]
    t1.fd(10)
    if (210<=x<=235 and -165<=y<=-140):
        score+=200
        print "Score= %d " % score
        t1.goto(-200,0)
    if (250<=x<=290 and -40<=y<=0):
        score-=22
        print "Score= %d " % score
        t1.goto(-200,0)
    if (-150<=x<=-110 and -210<=y<=-170):
        score+=11
        print "Score= %d " % score
        t1.goto(-200,0)
    if (100<=x<=135 and 15<=y<=60):
        score+=27
        print "Score= %d " % score
        t1.goto(-200,0)
    if (-250<=x<=-205 and 15<=y<=60):
        score+=25
        print "Score= %d " % score
        t1.goto(-200,0)
    if (50<=x<=100 and -250<=y<=-200):
        score+=15
        print "Score= %d " % score
	t1.goto(-200,0)
    if (-50<=x<=25 and 25<=y<=100):
        score+=30
	print "Score= %d" % score
        t1.goto(-200,0)
    if (math.sqrt(math.pow(0-x1,2)+math.pow(-110-y1,2))<=30):
	score+=18
	print "Score= %d" % score
        t1.goto(-200,0)
    if (math.sqrt(math.pow(200-x1,2)+math.pow(90-y1,2))<=40):
 	score-=14
	print "Score= %d" % score
        t1.goto(-200,0)
    if (math.sqrt(math.pow(-200-x1,2)+math.pow(145-y1,2))<=45):
 	score+=23
	print "Score= %d" % score
        t1.goto(-200,0)
    if (math.sqrt(math.pow(-230-x1,2)+math.pow(-100-y1,2))<=50):
 	score-=17
	print "Score= %d" % score
        t1.goto(-200,0)

    if (135<=x<=145 and -210<=y<=-40):
        t1.goto(-200,0)
    if (165<=x<=175 and -180<=y<=-100):
        t1.goto(-200,0)
    if (245<=x<=255 and -180<=y<=-130):
        t1.goto(-200,0)
    if (275<=x<=285 and -210<=y<=-100):
        t1.goto(-200,0)
    if (305<=x<=315 and -240<=y<=-40):
        t1.goto(-200,0)
    if (140<=x<=310 and -45<=y<=-35):
        t1.goto(-200,0)
    if (170<=x<=280 and -105<=y<=-95):
        t1.goto(-200,0)
    if (200<=x<=250 and -135<=y<=-125):
        t1.goto(-200,0)
    if (170<=x<=250 and -185<=y<=-175):
        t1.goto(-200,0)
    if (140<=x<=280 and -215<=y<=-205):
        t1.goto(-200,0)
    if (110<=x<=310 and -245<=y<=-235):
        t1.goto(-200,0)
    SCORE()

def k2():
    t1.left(90)
def k3():
    t1.right(90)
def k4():
    t1.bk(50)
wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")

wn.listen()
turtle.mainloop()
wn.exitonclick()