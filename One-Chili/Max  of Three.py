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




