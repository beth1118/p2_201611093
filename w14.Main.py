class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is ",self.name
mydog=Dog('lucky')
mydog.getName()
class Dog(Dog):
    def __init__(self,name):
        self.name=name
    def getname(self):
        print "my dog name is ", self.name
    def talk(self):
        print "mung mung"

class ShinTzuDog(Dog):
    def talk(self):
        print "si si"

class Maltese(Dog):
    def talk(self):
        print "mal mal"

        
def mung():
    t3=Dog('poppy')
    t3.talk()
    t4=ShinTzuDog('poppy')
    t4.talk()
    t5=Maltese('poppy')
    t5.talk()

def lab14():
    mung()


def main():
    lab14()
    
if __name__=="__main__":
    main()

raw_input()