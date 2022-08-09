"""def victory_for(board, sign):
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" or :
        print("You won!")
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("You won!")
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
         print("You won!")
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
         print("You won!")
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
         print("You won!")
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
         print("You won!")
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
         print("You won!")
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
         print("You won!")
    elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("You lost!")
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("You lost!")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
         print("You lost!")
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
         print("You lost!")
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
         print("You lost!")
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
         print("You lost!")
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
         print("You lost!")
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
         print("You lost!")"""

def victory(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_list = ["X", "X", "X"]
    o_list = ["O", "O", "O"]

    for row in board:
        if row == x_list:
            print("You lost!")
            return True
        elif row == o_list:
            print("You won!")
            return True

    for i in range(3):
        vertical = []
        for j in range(3):
            vertical.append(board[j][i])
        if vertical == x_list:
            print("You lost!")
            return True
        elif vertical == o_list:
            print("You won!")
            return True
    diagonal = []
    for i in range(3):
        diagonal.append(board[i][i])
        if diagonal == x_list:
            print("You lost!")
            return True
        elif diagonal == o_list:
            print("You won!")
            return True
    
    diagonal = []
    for i in range(3):
        diagonal.append(board[i][2-i])
        if diagonal == x_list:
            print("You lost!")
            return True
        elif diagonal == o_list:
            print("You won!")
            return True
    return False
