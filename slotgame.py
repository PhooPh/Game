import random
while True:
    coin=input("enter your amount")
    coin2=input("enter your money")
    print("coin")
    print("coin2")
    randomdata=[]
    for i in range(3):
        fruit=["apple","orange","mango"]
        number= random.choice(fruit)
        print(number)  
        randomdata.append(number)
    print(randomdata)
    if randomdata[0]==randomdata[1]==randomdata[2]:
        print("win")
        winnermoney=int(coin)*10
        print(winnermoney)
    userinfo=input("Do you want to play this again?")
    if userinfo=="yes":
        pass
    else:
        exit()  

    