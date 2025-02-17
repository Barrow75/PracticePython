# Prompt: Write a program that asks the user how many Fibonnaci numbers to generate and then generates them


def fibonacci():

    user_input = int(input("How many Fibonacci numbers would you like: "))

    num1, num2 = 0, 1
    fib = []

    for i in range(user_input):
        fib.append(num1)
        num1, num2 = num2, num1 + num2
    print(fib)
fibonacci()
