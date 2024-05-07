def welcome ():
    print("Welcome to players")
    print("In this game you will have the opportunity to play this classical game called Snakes and ladder") #Explain them the rules of the game
    print("The rules are simple:")
    print("The number of players is two.") 
    print("The first one who arrives at the 100 place, wins. The two players will throw the dice, the one who gets the biggest number, will start the game.")
    print("If you find a snake, you will fall. On the other hand, you will go upstairs if you find a ladder.")

welcome()

import random

def throw_dice():
    return random.randint(1, 6)

def climb(x):
    ladder_dict = {5: 17, 38: 71, 40: 53, 67: 80}
    return ladder_dict.get(x, x)

def fall(y):
    snake_dict = {96: 10, 70: 50, 45: 36, 21: 19}
    return snake_dict.get(y, y)

def move_player(player_position, move):
    new_position = player_position + move
    new_position = climb(new_position)
    new_position = fall(new_position)
    return new_position if new_position <= 100 else player_position

def print_board(pos_player_1, pos_player_2):
    board = [" " for _ in range(101)]
    board[pos_player_1] = "X"
    board[pos_player_2] = "O"

    for i in range(10):
        row = board[i * 10: (i + 1) * 10]
        print(" | ".join(str(cell).rjust(2) for cell in row))
        if i < 9:
            print("-" * 39)

def main():
    player_1 = throw_dice()
    player_2 = throw_dice()

    print("Player 1 rolled:", player_1)
    print("Player 2 rolled:", player_2)

    if player_1 > player_2:
        print("Player 1 starts the game!")
        current_player = "X"
    elif player_2 > player_1:
        print("Player 2 starts the game!")
        current_player = "O"
    else:
        print("It's a tie! Roll the dice again.")
        return

    pos_player_1 = 0
    pos_player_2 = 0

    while True:
        input("Press Enter to roll the dice...")
        roll = throw_dice()
        print(f"{current_player} rolled a {roll}")

        if current_player == "X":
            pos_player_1 = move_player(pos_player_1, roll)
            print(f"Player 1's position: {pos_player_1}")
            print_board(pos_player_1, pos_player_2)
            if pos_player_1 == 100:
                print("Congratulations Player 1! You reached position 100 and won!")
                break
            current_player = "O"
        else:
            pos_player_2 = move_player(pos_player_2, roll)
            print(f"Player 2's position: {pos_player_2}")
            print_board(pos_player_1, pos_player_2)
            if pos_player_2 == 100:
                print("Congratulations Player 2! You reached position 100 and won!")
                break
            current_player = "X"

if __name__ == "__main__":
    main()

