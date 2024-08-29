n = int(input("number of students : "))
for i in range(n):
    a=input("name :")
    b=input("class : ")
    c=int(input("height in cm : "))
    d=int(input("weight in kg : "))
    e=input("prefered sport : ")
    f=int(input("calorie intake : "))
    dic = {"name":a,"class":b,"height":c,"weight":d,"prefered sport":e,"calorie intake":f}
    if c < 150:
        if d < 45:
            print("red:underweight")
        elif d > 65:
            print("red:overweight")
        elif d <65 and d>50:
            print("green:suffient nutrition")
        else :
            print("needs more nutrition")
    elif c < 170 and c >= 150:
        if d < 65:
            print("red:underweight")
        elif d > 80:
            print("red:overweight")
        elif d <75 and d>70:
            print("green:suffient nutrition")
        else :
            print("needs more nutrition")
    elif c >= 170:
        if d < 75:
            print("red:underweight")
        elif d > 100:
            print("red:overweight")
        elif d <80 and d>90:
            print("green:suffient nutrition")
        else :
            print("needs more nutrition")
