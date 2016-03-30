marks=input("User input grade (0~100) : ")
print "%d" %marks,"marks"
if 90<=marks<=100:
    print "%s" %"A"
elif 80<=marks<90:
    print "%s" %"B"
elif 70<=marks<80:
    print "%s" %"C"
elif 60<=marks<50:
    print "%s" %"D"
else:
    print "%s" %"F" 