def board(positions):
    turn = 2
    for x in range (0,100):
        positions.insert(x, x+1)
    for y in range(99, -1, -10):
        if(turn%2==0):
            print(positions[y],"|",positions[y-1],"|",positions[y-2],"|",positions[y-3],"|",positions[y-4],"|",positions[y-5],"|",positions[y-6],"|",positions[y-7],"|",positions[y-8],"|",positions[y-9])
            print("-----------------------------------------------------------------------")
            turn-=1
        else: 
            print(positions[y-9],"|",positions[y-8],"|",positions[y-7],"|",positions[y-5],"|",positions[y-4],"|",positions[y-3],"|",positions[y-2],"|",positions[y-1],"|",positions[y])
            print("-----------------------------------------------------------------------")
            turn+=1
def ladderandsnake():
    print("LADDERS\n 3-24\n 14-42\n 30-86\n 37-57\n 50-96\n 66-74\n")
    print("SNAKES\n 95-18\n 77-45\n 60-28\n 34-10\n 20-2\n")
    
    
def create_new_board():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def print_board(board):
    print(
        f"""
 {board[0][0]} | {board[0][1]} | {board[0][2]}
-----------
 {board[1][0]} | {board[1][1]} | {board[1][2]}
-----------
 {board[2][0]} | {board[2][1]} | {board[2][2]}
"""
    )