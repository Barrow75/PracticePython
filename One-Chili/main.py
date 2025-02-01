# Prompt: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

def numberList():
    list1 = input("Enter numbers for a list: ").split()
    return list1

this_list = numberList()
print(this_list)

def main():
    print([this_list[0], this_list[-1]])

main()
