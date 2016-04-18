import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquareAtSave(size, pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks 

def drawSquareFrom(xtracks,ytracks):
   x=((xtracks,ytracks),(xtracks+100,ytracks),(xtracks+100,ytracks-100),(xtracks,ytracks-100),(xtracks,ytracks))
   t1.penup()
   t1.goto(x[0])
   t1.pendown()
   for i in range(0,5):
       t1.goto(x[i])

def lab7a():
   size=100
   pos=(0,0)
   mytracks=drawSquareAtSave(size,pos)
   print mytracks

def lab7b():
   xtracks=input("input x pos:")
   ytracks=input("input y pos:")
   mytracks=drawSquareFrom(xtracks,ytracks)

def main():
    lab7a(), lab7b()
    input()

if __name__=="__main__":
    main()