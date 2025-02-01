# Prompt: Write a function that takes an ordered list of numbers (a list where the elements are in order
# from smallest to largest) and another number. The function decides whether or not
# the given number is inside the list and returns (then prints) an appropriate boolean.


def OrderList():
    order = input("Enter Numbers: ").split()
    new = list(map(int, order))
    new.sort()

    return new

new = OrderList()
print(new)

def main():

    check_list = int(input("Is this number in the list: "))

    if check_list not in new:
        print("False")
    else:
        print("True")
main()
