from board import create_new_board, print_board
from actions import dice

with open("README.md","r") as f:
   print(f.read())

board = create_new_board()
while True: 
    print_board(board)
    command = input("Enter a command:")
    if command == "hello":
        hello() # type: ignore
    elif command == "q":
        exit()
    elif command == "throw dice":
        dice()
    else:
        print("I did not understand this command.")
    
print(board([]))

#Add shift omnivox 
#Do relations between every file with main
