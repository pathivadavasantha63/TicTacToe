# Tic Tac Toe Game

board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(player):
    win_conditions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True

    return False


def board_full():
    return " " not in board


player = "X"

while True:

    print_board()

    try:
        move = int(input(f"Player {player}, choose position (1-9): "))

        if move < 1 or move > 9:
            print("Choose between 1 and 9.")
            continue

        if board[move-1] != " ":
            print("Position already taken.")
            continue

        board[move-1] = player

        if check_winner(player):
            print_board()
            print(f"Player {player} Wins!")
            break

        if board_full():
            print_board()
            print("Match Draw!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"

    except ValueError:
        print("Please enter a valid number.")