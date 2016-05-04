import math
Locations=tuple()
myList=list()
(x1,y1)=(37.575807,126.973358)
Locations=[(37.571656,126.976576),(37.570122,126.982885),(37.574595,126.957621),(37.576479,126.985297),(37.570409,126.992111)]
for i in Locations:
    myList.append (math.sqrt((x1-i[0])**2+(y1-i[1])**2))
    

print min(myList)