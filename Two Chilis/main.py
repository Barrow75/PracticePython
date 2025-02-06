# Prompt: Create a program that asks the user for a number and then prints out a list of all the divisors of
# that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number


user_input = int(input("Enter a number to get its divisors: "))

x = range(2,20)

for element in x:
    if  element % user_input  == 0:
        print(element)