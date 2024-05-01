from .board import *
def welcome ():
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
    return random.choice(result)  
    
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

def play():
    print("hola")


welcome()

play()
player_1 = throw_dice()
player_2 = throw_dice()

print("Player 1 threw:", player_1)
print("Player 2 threw:", player_2)

if player_1 > player_2:
    print("Player 1 starts the game!")
    
elif player_2 > player_1:
    print("Player 2 starts the game!")

else:
    print("There was a tie! Throw the dice again!")
    player_1 = throw_dice()
    player_2 = throw_dice()

    print("Player 1 threw:", player_1)
    print("Player 2 threw:", player_2)
    

mi_tablero = create_new_board() 
print_board(mi_tablero)

# place(player_1,0,mi_tablero) 
print_board(mi_tablero)


#play_again()

def throw_again_dice():
  print("Throw again the dice to advance")
# if throw_again_dice. lower() == 's':
 #   play()

# Function to move the player on the board based on the dice roll
def move_player(player_position, throw_again_dice):
    new_position = player_position + throw_again_dice
    if new_position <= 100:
        return new_position
    else:
        return player_position

# Main function to play the game

def update_board(board, pos_player_1, pos_player_2):
    if [pos_player_1[0], pos_player_1[1]] == [pos_player_2[0], pos_player_2[1]]:
        board[pos_player_1[0]][pos_player_1[1]] = "&"
    else: 
        board[pos_player_1[0]][pos_player_1[1]] = "X"
        board[pos_player_2[0]][pos_player_2[1]] = "O"
    return board

# def move_player():
#      pos_player_1  
pos_player_1 = 99
pos_player_2 = 99


while pos_player_1 < 100:  
        input("Click again to roll the dice...")
        pos_player_1 = pos_player_1 + 1
        print("You rolled a", throw_again_dice)
       # pos_player_1 = move_player(pos_player_1, throw_again_dice)  
        print("Your new position is:", pos_player_1)
        str(print(update_board))
print("Congratulations player 1! You reached position 100 and won the game.")

while pos_player_2 < 100:  
        input("Click again to roll the dice...")
        pos_player_2 = pos_player_2 + 1
        print("You rolled a", throw_again_dice)
       # pos_player_2 = move_player(pos_player_2, throw_again_dice)  
        print("Your new position is:", pos_player_2)
        str(print(update_board))
print("Congratulations player 2! You reached position 100 and won the game.")
play()


#Data Science Galaxy. (2023, 4 junio). Snake and Ladder Game in Python | Game in Python | Data Science Galaxy [Vídeo]. YouTube. https://www.youtube.com/watch?v=A0HN2fn9x7E

