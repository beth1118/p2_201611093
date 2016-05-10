import collections
def CountData():
    allData= [
      ["Coffee","Water","Milk","Icecream"],
      ["Espresso","No","No","No"],
      ["Long Black","Yes","No","No"],
      ["Flat White","No","Yes","No"],
      ["Cappuccino","No","Yes - Frothy","No"],
      ["Affogato","No","No","Yes"],
    ]

    data = allData[1:]

    count = 0
    for i in data:
        if i[2]=="No":
            count= count + 1

    for i in data:
        print i[0], i[2]

    print "MilkRatio",(float(len(data))-float(count))/(len(data))

def score():
    score = [
["English", 100],
["Math", 200],
["English", 200],
["Math", 200],
["English", 100],
["Math", 300]
]
    EnSum = 0
    MaSum = 0
    for i in range(0,len(score)):
        if score[i][0]=="English":
            EnSum=EnSum+score[i][1]
    for i in range(0,len(score)):
        if score[i][0]=="Math":
            MaSum=MaSum+score[i][1]

    print "EnglishSum:", EnSum,"MathSum :", MaSum
    print "EnglishAverage:",EnSum/3,"MathAverage:",MaSum/3

def CountLetItBe():
    LetItBe="When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness She is standing right in front of me Speaking words of wisdom let it be Let it be let it be Let it be let it be Whisper words of wisdom let it be And when the broken-hearted people Living in the world agree There will be an answer let it be For though they may be parted There is still a chance that they will see There will be an answer let it be Let it be let it be Let it be let it be Yeah there will be an answer let it be Let it be let it be Let it be let it be Whisper words of wisdom let it be Let it be let it be Ah let it be yeah let it be Whisper words of wisdom let it be And when the night is cloudy There is still a light that shines on me Shine on until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be Let it be yeah let it be Oh there will be an answer let it be Let it be let it be Let it be yeah let it be Whisper words of wisdom let it be"

    SplitLet=LetItBe.split()
    CountList=dict()
    LetItBe_Com=[]
    rank=[5]
    for i in range(0,len(SplitLet)):
        LetItBe_Com.append(SplitLet[i].lower())

    for i in LetItBe_Com:
        if i not in CountList:
            CountList[i]=1
        else:
            CountList[i]=CountList[i]+1

    print CountList
    print max(CountList.values())




    
def lab10_2():
    CountData()
    score()

    CountLetItBe()
   

def main():
    lab10_2()
    
if __name__=="__main__":
    main()

wn.exitonclick()