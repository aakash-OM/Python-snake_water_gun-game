import random

def gamewin(computer,player):
    if computer==player:
        return None
    
    elif computer=='s':
        if player=='w':
            return False
        elif player=='g':
            return True

    elif computer=='w':
        if player=='g':
            return False
        elif player=='s':
            return True

    elif computer=='g':
        if player=='w':
            return False
        elif player=='s':
            return True        

n=int(input("enter how many times you want to play the game \n"))
for i in range(1,n+1):
    
    print("Computer's turn: Snake(s) Water(w) or gun(g) ")
    randno=random.randint(1,3)
        #print(randno)
    if randno==1:
        computer='s'
    elif randno==2:
        computer=='w'
    elif randno==3:
        computer=='g'
        

    player=input("Player's turn: Enter 's'(Snake), 'w'(Water) or 'g'(gun) \n")

    print(f"Computer choose: {computer}")
    print(f"Player choose: {player}")

    a=gamewin(computer,player)

    if a==None:
        print("Game is Tie \n :| \n \n ")
    elif a==True:
        print("Game Win \n  :) \n \n ")
    elif a== False:
        print("Game Loose \n :(  \n \n")


