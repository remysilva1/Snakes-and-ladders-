print("Welcome to players")
print("In this game you will have the opportunity to play this classical game called Snakes and ladder") #Explain them the rules of the game
print("The rules are simple:")
print("The number of players is two.") 
print("The first one who arrives at the 100 place, wins. The two players will throw the dice, the one who gets the biggest number, will start the game.")
print("If you find a snake, you will fall. On the other hand, you will go upstairs if you find a ladder.")

def dice():
    print("Throw the dice")

import random

def throw_dice():
    result = list(range(1,7))
    return random.choice(results)

def play():
    print ("Click enter to throw the dice")
    
player_1 = throw_dice()
player_2 = throw_dice()

print("Player 1 threw:", player_1)
print("Player 2 threw", player_2)

if player_1 > player_2:
    print("Player 1 starts the game!")
    
elif player_2 > player_1:
    print("Player 2 starts the game!")

else:
    print("There was a tie! Throw the dice again!")
    play()
    
play()

def place(player,position,board):
    board[position[0]][position[1]] = player 
    
def ladder_and_snake():
    print("LADDERS\n 5-17\n 38-71\n 40-53\n 67-80\n")
    print("SNAKES\n 96-10\n 70-50\n 45-36\n 21-19\n")

def climb(x):
    if(x==5):
        x=17
    if(x==38):
        x=71
    if(x==40):
        x=53
    if(x==67):
        x=80
    return(x)
def fall(y):
    if(y==96):
        y=10
    if(y==70):
        y=50
    if(y==45):
        y=36
    if(y==21):
        y=19
    return(y)


# Also we will use the functions if, elif & else to check if the player won or found a snake/ladder   
# Lists of tuples for the dice
#Data Science Galaxy. (2023, 4 junio). Snake and Ladder Game in Python | Game in Python | Data Science Galaxy [Vídeo]. YouTube. https://www.youtube.com/watch?v=A0HN2fn9x7E