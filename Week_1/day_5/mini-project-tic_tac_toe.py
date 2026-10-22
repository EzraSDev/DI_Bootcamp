def display_board(grid):
    for i, row in enumerate(grid):
        print(" " + " | ".join(row))
        if i< 2:
            print("---+---+---")

     
def check_if_used(board, row, col):
    if board[row][col] != " " :
        return False
    else:
        return True


def horizontal_input():
    while True:
        turn = input("Please choose left, middle or right:")
        if  turn.lower() == "left":
            col = 0
        elif turn.lower() == "middle":
            col = 1
        elif turn.lower() == "right":
            col = 2
        else:
            print("Please enter only the available words")
            continue
            
        return col



def player_input(board):
        while  True:
            turn =input("Please choose where to put your tile Top, middle or bottom:")
            if turn.lower() == "top":
                row = 0
                col=horizontal_input()
            elif turn.lower() == "middle":
                col=horizontal_input()
                row = 1
            elif turn.lower() == "bottom":
                col = horizontal_input()
                row = 2
            else:
                print("Please enter only the available words")
                continue
            
            if not check_if_used(board, row, col): 
                print("This move was not valid, try again!")
            else:
                return row, col


def place_tile(board,row, col, turn):
    
        board[row][col] = turn
    


def next_player(turn):
    if turn =="X":
         turn = "O"
    else:
        turn = "X"
    
    return turn



def check_if_win(board, mark):
    for row in board:
        if row.count(mark) == 3:
            return True

    for c in range(3):
        if board[0][c] == mark and board[1][c] == mark and board[2][c] == mark:
            return True

    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True

    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True

    return False
        
        
        

def play():
    turn = "X"
    has_won = False
    board = [[" " for _ in range(3)]for _ in range(3)]
    while has_won == False:
        display_board(board)
        row,col =player_input(board)
        place_tile(board,row,col,turn)
        has_won = check_if_win(board, turn)
#         check_if_tie()
        turn = next_player(turn)

play()


