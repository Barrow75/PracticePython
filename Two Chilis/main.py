# Prompt: refactoring an existing code snippet into using functions.

"""
Refactor this code
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")

"""



def boardsize():
    length = int(input("What length do you want the board?: "))
    width = int(input("What width do you want the board?: "))
    return length, width


def printboard(length, width):
    for row in range(length):
        print(" ---" * width)
        print("|   " * width + "|")
    print(" ---" * width)


def main():

    print("Generate a game board")
    length, width = boardsize()
    printboard(length, width)


main()