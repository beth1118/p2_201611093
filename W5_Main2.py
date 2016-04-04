def BMI():
    height=raw_input("input user height(m):")
    weight=raw_input("input user weight(kg):")
    BMI=weight/(height*height)
       print BMI
    if BMI <= 18.5:
        res="low weight"
    elif 18.5<BMI<25:
        res="normal weight"
    elif 25<=BMI<30:
        res="overweight"
    elif 30<=BMI:
        res="obesity"
    return res

print BMI()
        