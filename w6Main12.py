"""
@author LYJ
@since 160411
"""

x=list()

def sumList(aList):
    sum=0
    for i in range(0,1001):
        if(i%4==0 and i%5>0):
            x.append(i)
    for t in range(0,len(x)):
        sum=sum+x[t]    
    return sum

def lab6():
    """programming is really hahaha fun"""
    aList=[x]
    labsum=sumList(aList)
    print labsum

def main():
    lab6()

def main():
	lab6()

if __name__=="__main__":
	main()

wn=raw_input("Do you want finish? Input yes and press Enter  ")
