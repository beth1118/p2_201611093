import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def main():  
    print ("Let's play R S P game!!") 
    p1=input("hey first guy what's your choice?: ")
    p2=input("how about you,next guy: ") 
def subtool(p):  
    if(p=='r'):  
        return 2.0  
    elif(p=='s'):  
        return 4.0  
    elif(p=='p'):  
        return 8.0  
    else:  
        print ("Input Error")          
    alpha=subtool(p1)/subtool(p2)  
    if(alpha==0.5):  
        print ("p1 you win!!")  
    elif(alpha==1):  
        print ("draw :)")  
    elif(alpha==0.25):  
        print ("p2 you win!!")  
    elif(alpha==2):  
        print ("p2 you win!!")  
    elif(alpha==4):  
        print ("p1 you win!!")  
        
main()
 
