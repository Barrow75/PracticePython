# Prompt: Ask the user what size game board they want to draw, and draw it for them to the screen
# using Python’s print statement.

def GameBoardSize(size_input_length, size_input_width ):



    return  size_input_length, size_input_width

size_input_length = int(input("Enter the size length of the gameboard: "))
size_input_width = int(input("Enter the size width of the gameboard: "))






def main():

    length, width = GameBoardSize( size_input_length, size_input_width)

    #board_height = '|'
    #board_width = '-'

    for row in range(length):
        print("--" * width + "-------")
        print("|" + "   |" * width)
    print("--" * width + "-------")



main()
