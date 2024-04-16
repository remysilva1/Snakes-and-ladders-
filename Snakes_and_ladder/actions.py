print("Welcome to players")
print("In this game you will have the opportunity to play this classical game called Snakes and ladder") #Explain them the rules of the game
print("The rules are simple:")
print("The number of players is two.") 
print("The first one who arrives at the 100 place, wins. The two players will throw the dice, the one who gets the biggest number, will start the game.")
print("If you find a snake, you will fall. On the other hand, you will go upstairs if you find a ladder.")

def dice():
    print("Throw the dice")

def place(player,position,board):
    board[position[0]][position[1]] = player 
# Also we will use the functions if, elif & else to check if the player won or found a snake/ladder   
# Lists of tuples for the dice