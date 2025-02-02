# Implement a function that takes as input three variables,
# and returns the largest of the three. Do this without using the Python max() function!



def MaxOfThree():
    number1= int(input("Eneter a number: "))
    number2 = int(input("Eneter a second number: "))
    number3 = int(input("Eneter a third number: "))

    if number1 > number2 and number1 > number3:
        print(f"{number1} is the largest")

    elif number2 > number1 and number2 > number3:
        print(f"{number2} is the largest")

    elif number3 > number1 and number3 > number2:
        print(f"{number3} is the largest")

    elif number1 == number2 == number3:
        print(f"{number1}, {number2}, and {number3} are all equal")

MaxOfThree()


# Solution 2

def MaxOfThree(num1, num2, num3):

    return num1, num2, num3

user_input = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))
user_input3 = int(input("Enter third number: "))


def main():
    if user_input > user_input2 and user_input > user_input3:
        print(f"{user_input} is the largest")

    elif user_input2 > user_input and user_input2 > user_input3:
        print(f"{user_input2} is the largest")

    elif user_input3 > user_input and user_input3 > user_input2:
        print(f"{user_input3} is the largest")

    elif user_input == user_input2 == user_input3:
        print(f"{user_input}, {user_input2}, and {user_input3} are all equal")

main()



