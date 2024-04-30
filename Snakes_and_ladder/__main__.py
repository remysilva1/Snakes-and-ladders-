from board import create_new_board, print_board
from actions import dice

with open("README.md","r") as f:
   print(f.read())
   
def place():
    place

board = create_new_board() #Set up phase 
while True:   #Per turn
    print_board(board)
    # input("Click enter to throw the dice")
    command = input("Enter a command:")   #Per command
    if command == "place":
        position = input("Position")
        position = [int(p) for p in position]
        place("x",position, board)
        print_board(board)
        
    elif command == "throw dice":
        dice()
    else:
        print("I did not understand this command.")