from Snakes_and_ladder.board import print_board
from Snakes_and_ladder.actions import throw_dice 

def test_throw_dice():
    board = create_new_board
    assert result in [1, 2, 3, 4, 5, 6]

def create_new_board():
    board = [[" "]*10]*10
    return board
 
def welcome ():
    print("Welcome to players")
    print("In this game you will have the opportunity to play this classical game called Snakes and ladder") #Explain them the rules of the game
    print("The rules are simple:")
    print("The number of players is two.") 
    print("The first one who arrives at the 100 place, wins. The two players will throw the dice, the one who gets the biggest number, will start the game.")
    print("If you find a snake, you will fall. On the other hand, you will go upstairs if you find a ladder.")

def play():
    print ("Click enter to throw the dice")
    input()

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

def throw_again_dice():
  print("Throw again the dice to advance")
if throw_again_dice. lower() == 's':
    play()

throw_again_dice()
