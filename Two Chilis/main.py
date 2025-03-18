# Prompt: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any.

# Prompt 2: asking the user for a coordinate of where they want to place their piece.

game = [[" " for _ in range(3)] for _ in range(3)]

player1 = '✘'
player2 = '⭕'

# function for player 1 input
def player1_input(game):
    # prompt the player to enter a position
    print("Player 1 goes first as ✘: ")


    # if the choice is not in the options they need to go asagain

    while True:

        try:
            # have the player enter coordinates to a position they want to placce the x
            player1_row = int(input("Enter row you want to place ✘: "))
            player1_column = int(input("Enter row you want to place ✘: "))

            # checking the range of the 2d matrix
            if not (0 <= player1_row < 3 and 0 <= player1_column < 3):
                print("Not an option try again")
                continue

            # check if that position has already been occupied
            if game[player1_row][player1_column] != " ":
                print("Position is taken")
                continue

            # place an x where there is no occupation
            game[player1_row][player1_column] = player1
            break

        except ValueError:
            print("Invalid input")




def player2_input(game):

    # prompt the second user to put in the coordinates
    print("Player 2 goes next as ⭕ :")



    while True:


        # check to see if the position is occupied
        try:
            # have the user put in the coordinates
            player2_row = int(input("Enter the row yyou want to place ⭕: "))
            player2_column = int(input("Enter the colun you want to place ⭕: "))

            if not (0 <= player2_row < 3 and 0 <= player2_column < 3):
                print("Invalid")
                continue

            # check to see if the corrdinates are in range
            if  game[player2_row][player2_column] != " ":
                print("Position is taken")
                continue

            # place the ⭕ where there is no occupied positon
            game[player2_row][player2_column] = player2
            break

        except ValueError:
            print("Invalid Input")

player1_input(game)
player2_input(game)

