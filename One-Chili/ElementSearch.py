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


# Solution 2
def OrderList():
    order = input("Enter Numbers: ").split()
    new = list(map(int, order))
    new.sort()

    return new

new = OrderList()
print(new)

def BinarySearch(new):

    check_list = int(input("Is this number in the list: "))
    start_index = 0
    end_index = len(new) - 1

    while True:

        if start_index > end_index:
            return -1

        half_list = (end_index + start_index) // 2

        if check_list == new[int(half_list)]:
            return half_list

        elif check_list > new[int(half_list)]:
            start_index = half_list + 1
        else:
            start_index = half_list - 1



result = BinarySearch(new)
print(result)
