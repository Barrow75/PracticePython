# Prompt: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def EvenOdd(number1, number2):
    return  number1, number2

number1_input = int(input("Enter a number: "))
number2_input = int(input("Enter another number: "))

def main():
    if number1_input % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

    if number1_input % 4 == 0:
        print("This number is a multiple of 4")
    else:
        print("Number is not a multiple of 4")

    if number1_input % number2_input == 0:
        print(f"{number1_input} divides evenly in {number2_input}")
    else:
        print(f"{number1_input} does not divide evenly in {number2_input}")

main()
