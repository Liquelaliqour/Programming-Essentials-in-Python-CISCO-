board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9],
]

def enter_move(board):
    value = int(input("Enter your move: "))
    for i in range(3):
        for j in range(3):
            if value == board[i][j]:
                board[i][j] = "O"
enter_move(board)
print(board)
