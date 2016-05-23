import os
mydir=os.getcwd()
filename='python.txt'
myfilename=os.path.join(mydir,filename)
myfile=open(myfilename)
line=myfile.readline()
myfile.close()

def One():
    myfile=open(myfilename,'r')
    for line in myfile:
        if line.find('Python') >=0:
            print line

    myfile.close()

def Two():
    filetwo=open('output.txt', 'w')
    line1='first line\n'
    filetwo.write(line1)
    line2='second line\n'
    filetwo.write(line2)
    line3='third line'
    filetwo.write(line3)
    filetwo.close()
    myfiletwo=open('output.txt', 'r')
    contentstwo=myfiletwo.readlines()
    for a in range(0,len(contentstwo)):
        if contentstwo[a].find('l') >= 0:
            result = contentstwo[a].split()
        for b in range(0,len(result)):
            if result[b].find('l') >= 0:
                print result[b].upper()
    myfiletwo.close()
    
def lab12():
    print "One"
    One()
    print "Two"
    Two()

def main():
    lab12()
    raw_input()

if __name__=="__main__":
    main()