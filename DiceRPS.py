import random 
import os
os.system('cls' if os.name=='nt' else 'clear')
while True:

    print("Rock,Paper,Scissors - Shoot!")
    userChoice = input("Choose your weapon [Rock], [Paper] , [Scissor]:")
    print(" you chose: " + userChoice)
    choices = ['Rock','Paper','Scissor']
    PhooChoice = random.choice(choices)
    print( " I chose:" +  PhooChoice )
    if PhooChoice == userChoice:
        print("same!")
    elif PhooChoice =='Rock' and userChoice=='Scissor':
        print("Rock beats Scissor, I win!")
    elif PhooChoice =='Scissor' and userChoice=='Paper':
        print("Scissor beats Paper , I win!")
    elif PhooChoice =='Paper' and userChoice=='Rock':
        print("Paper beats Rock  , I win!")
    else:
        print("You win!")
        exit()
            

       