def display_board(grid):
    for i, row in enumerate(grid):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")


def check_if_used(board, row, col):
    return board[row][col] == " "


def horizontal_input():
    while True:
        answer = input("Please choose left, middle or right: ")
        if answer.lower() == "left":
            return 0
        elif answer.lower() == "middle":
            return 1
        elif answer.lower() == "right":
            return 2
        else:
            print("Please enter only the available words")


def player_input(board):
    while True:
        answer = input("Please choose where to put your tile Top, middle or bottom: ")
        if answer.lower() == "top":
            row = 0
        elif answer.lower() == "middle":
            row = 1
        elif answer.lower() == "bottom":
            row = 2
        else:
            print("Please enter only the available words")
            continue

        col = horizontal_input()

        if check_if_used(board, row, col):
            return row, col
        print("This move was not valid, try again!")


def place_tile(board, row, col, player):
    board[row][col] = player


def next_player(player):
    return "O" if player == "X" else "X"


def check_if_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for c in range(3):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def check_if_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def play():
    player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        display_board(board)
        row, col = player_input(board)
        place_tile(board, row, col, player)

        if check_if_win(board, player):
            display_board(board)
            print(f"Congratulations {player}, you won!")
            break
        elif check_if_tie(board):
            display_board(board)
            print("Game over! It's a tie.")
            break

        player = next_player(player)


play()