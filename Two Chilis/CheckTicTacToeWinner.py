# Prompt: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any.


# check player 1
def check_win_player1(board, player1):

    # check rows
    for row in board:
        if all(cell == player1 for cell in row):
            return True

    # check columsns
    for colum in range(3):
        if all(board[row][colum] == player1 for row in range(3)):
            return True

    # check diagonals
    if all(board[i][i] == player1 for i in range(3)):
        return True

    if all(board[i][3 - 1 - i] == player1 for i in range(3)):
        return True

    return False


# check player 2
def check_win_player2(board, player2):
    for row in board:
        if all(cell == player2 for cell in row):
            return True

    for colum in range(3):
        if all(board[row][colum] == player2 for row in range(3)):
            return True

    if all(board[i][i] == player2 for i in range(3)):
        return True

    if all(board[i][3 - 1 - i] == player2 for i in range(3)):
        return True

    return False

game_board = [[1, 2, 0],
	          [2, 1, 0],
	          [2, 1, 2]]


if check_win_player1(game_board, 1):
    print("Player 1 wins")
elif check_win_player2(game_board, 2):
    print("Player 2 wins")
else:
    print("Draw")
