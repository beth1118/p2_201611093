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
    a = 0
    for i in data:
        if i[2]=="No":
            a=a + 1

    for i in data:
        print i[0], i[2]

    print "MilkRatio",(float(len(data))-float(a))/(len(data))

def scoreSum():
    score = [
	    ["English", 100],
	    ["Math", 200],
 	    ["English", 200],
	    ["Math", 200],
 	    ["English", 100],
	    ["Math", 300]
	    ]
    EnglishSum = 0
    MathSum = 0
    for i in range(0,len(score)):
        if score[i][0]=="English":
            EnglishSum=EnglishSum+score[i][1]
    for i in range(0,len(score)):
        if score[i][0]=="Math":
            MathSum=MathSum+score[i][1]

    print "EnglishSum:", EnglishSum,"MathSum :", MathSum
    print "EnglishAverage:",EnglishSum/3,"MathAverage:",MathSum/3

def LetItBe():
    lyrics=list()
    lyrics=[
        "When I find myself in times of trouble",	
	"Mother Mary comes to me",
	"Speaking words of wisdom let it be",
	"And in my hour of darkness",
	"She is standing right in front of me",
	"Speaking words of wisdom let it be",

	"Let it be let it be",
	"Let it be let it be",
	"Whisper words of wisdom let it be",

	"And when the broken-hearted people",
	"Living in the world agree",
	"There will be an answer let it be",
	"For though they may be parted",
	"There is still a chance that they will see",
	"There will be an answer let it be",

	"Let it be let it be",
	"Let it be let it be",
	"Yeah there will be an answer let it be",
	"Let it be let it be",
	"Let it be let it be",
	"Whisper words of wisdom let it be",

	"Let it be let it be",
	"Ah let it be yeah let it be",
	"Whisper words of wisdom let it be",

	"And when the night is cloudy",
	"There is still a light that shines on me",
	"Shine on until tomorrow let it be",
	"I wake up to the sound of music",
	"Mother Mary comes to me",
	"Speaking words of wisdom let it be",

	"Let it be let it be",
	"Let it be yeah let it be",
	"Oh there will be an answer let it be",
	"Let it be let it be",
	"Let it be yeah let it be",
	"Whisper words of wisdom let it be"
 	]
    doc=lyrics
    d=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d:
                d[c]=1
            else :
                d[c]=d[c]+1

    print d
    for v in range(len(d)):
        if d.values()[v]>=20:
            print d.keys()[v], d.values()[v]





def lap10():
    CountData()
    scoreSum()
    LetItBe()

def main():
    lap10()

if __name__=="__main__":
    main()

wn=raw_input()