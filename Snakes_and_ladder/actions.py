def create_new_board():
    board = [[" "]*10]*10
    return board

def print_board(board):
    print(
        f"""
 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} | {board[0][5]} | {board[0][6]} | {board[0][7]} | {board[0][8]} | {board[0][9]}
--------------------------------------
 {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]} | {board[1][5]} | {board[1][6]} | {board[1][7]} | {board[1][8]} | {board[1][9]}
--------------------------------------
 {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]} | {board[2][5]} | {board[2][6]} | {board[2][7]} | {board[2][8]} | {board[2][9]}
--------------------------------------
 {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} | {board[3][5]} | {board[3][6]} | {board[3][7]} | {board[3][8]} | {board[3][9]}
--------------------------------------
 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} | {board[4][5]} | {board[4][6]} | {board[4][7]} | {board[4][8]} | {board[4][9]}
--------------------------------------
 {board[5][0]} | {board[5][1]} | {board[5][2]} | {board[5][3]} | {board[5][4]} | {board[5][5]} | {board[5][6]} | {board[5][7]} | {board[5][8]} | {board[5][9]}
--------------------------------------
 {board[6][0]} | {board[6][1]} | {board[6][2]} | {board[6][3]} | {board[6][4]} | {board[6][5]} | {board[6][6]} | {board[6][7]} | {board[6][8]} | {board[6][9]}
--------------------------------------
 {board[7][0]} | {board[7][1]} | {board[7][2]} | {board[7][3]} | {board[7][4]} | {board[7][5]} | {board[7][6]} | {board[7][7]} | {board[7][8]} | {board[7][9]}
--------------------------------------
 {board[8][0]} | {board[8][1]} | {board[8][2]} | {board[8][3]} | {board[8][4]} | {board[8][5]} | {board[8][6]} | {board[8][7]} | {board[8][8]} | {board[8][9]}
--------------------------------------
 {board[9][0]} | {board[9][1]} | {board[9][2]} | {board[9][3]} | {board[9][4]} | {board[9][5]} | {board[9][6]} | {board[9][7]} | {board[9][8]} | {board[9][9]}
"""
    ) 
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

def play():
    print ("Click enter to throw the dice")
    input()
    
#play_again = play*2 
    
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

place(player_1,0,mi_tablero)
print_board(mi_tablero)


#play_again()

def throw_again_dice():
  print("Throw again the dice to advance")
if throw_again_dice. lower() == 's':
    play()

# Function to move the player on the board based on the dice roll
def move_player(player_position, throw_again_dice):
    new_position = player_position + throw_again_dice
    if new_position <= 100:
        return new_position
    else:
        return player_position

# Main function to play the game

def update_board(board, pos_player_1, pos_player_2):
    if pos_player_1[0], pos_player_1[1] == pos_player_2[0], pos_player_2[1]:
        board[pos_player_1[0]][pos_player_1[1]] = "&"
    else: 
        board[pos_player_1[0]][pos_player_1[1]] = "X"
        board[pos_player_2[0]][pos_player_2[1]] = "O"
    return board

def move_player():
      pos_player_1  


while pos_player_1 < 100:  
        input("Click again to roll the dice...")
        
        print("You rolled a", throw_again_dice)
        pos_player_1 = move_player(pos_player_1, throw_again_dice)  
        print("Your new position is:", pos_player_1)
        str(print(update_board))
print("Congratulations player 1! You reached position 100 and won the game.")

while pos_player_2 < 100:  
        input("Click again to roll the dice...")
        
        print("You rolled a", throw_again_dice)
        pos_player_2 = move_player(pos_player_2, throw_again_dice)  
        print("Your new position is:", pos_player_2)
        str(print(update_board))
print("Congratulations player 2! You reached position 100 and won the game.")
play()


#Data Science Galaxy. (2023, 4 junio). Snake and Ladder Game in Python | Game in Python | Data Science Galaxy [Vídeo]. YouTube. https://www.youtube.com/watch?v=A0HN2fn9x7E
