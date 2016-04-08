def Leaf():
    year=input("User input year : ")
    if (year%4==0) and (year%100!=0 or year%400==0):
        print "leap year"
    else:
        print "no leap year"
Leaf()


@startuml

title leapyear or not

start 
 :user input year;
 
 if(tear%4==0)and year(%100 !=0 or year%400==0) then (yes)
 
 :print leapyear!;
 else (no)
 :print no leapyear;
 endi


def Game():
   import random
   guessesTaken = 0
   print("Hi!, what's your name?") 
   myName = input()
   number = random.randint(1,100)
   print('well, '+ myName + ', I am thinking of a number 1 and 100.')
   while guessesTaken < 10:
        print ('Taken a guess')
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
   if guess < number:
        print ('Your guess is too low')
   if guess > number:
        print ('Your guess is too high')
   if guess == number:
        break
   if guess == number:
        guessesTaken = str(guessesTaken)
        print ('Great, ' + myName + '! You guessed my number in ' + guesses-Taken + '         guesses!')
   if guess != number:
        number = str(number)
        print ('Nope. The number I was thinking of was ' + number)
   wn.exitonclick() 
Game()

@startuml 
title UpDownGame 
start  
:Select random one number in range; 
:Try to guess the number; 
:Player input one number;  
while(Play) 
if (Compare Player number & answer) then (Player number < answer) 
:Up; 
else (Player number > answer) 
:Down; 
endif 
endwhile 
:Player number = answer; 
:You win; 
:End Game; 
stop 
@enduml


def lab6():
    Game()
    Leaf()

def main():
   lab6()

if __name__=="__main__":
   main()