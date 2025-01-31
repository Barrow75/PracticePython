# Prompt: Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old

# Extras:
#
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message
# Print out that many copies of the previous message on separate lines.

# Solution One
def name_age():
    name = input("What is your name: ")
    age = int(input("what is your age: "))
    current_year = int(input("Enter the current year: "))
    turn_100 = (current_year + 100) - age
    print(f"Your name is {name} and you are currently {age}, in the year {turn_100} you will be 100 years old")

    display = int(input("How many times would you like for it to be printed out? "))
    for i in range(display):
        print(f"Your name is {name} and you are currently {age}, in the year {turn_100} you will be 100 years old")

name_age()


# Solution 2 with datetime modle to get current year
from datetime import date


def name_age(name, age):

    return f"{name} {age}"

input_name = input("Enter your name: ")
input_age = int(input("Enter your age: "))

def main():
    today = date.today()
    year = today.year
    print(name_age(input_name, input_age))
    turn_100 = (year + 100) - input_age
    print(name_age(f"Your name is {input_name} and", f"your age is {input_age}. In {turn_100} you will be "
                                                     f"100 years old"))

    display = int(input("How many times would you like for it to be printed out? "))
    for i in range(display):
        print(name_age(f"Your name is {input_name} and", f"your age is {input_age}. In {turn_100} you will be "
                                                         f"100 years old"))

main()


