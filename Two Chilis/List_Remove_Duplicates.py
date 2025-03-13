# Prompt: Write a program that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates.



def Duplicates():

    user_list = list(map(int, input("Enter numbers for a list: ").split()))
    print(f"List with duplicates:", user_list)
    remove_duplicate = set(user_list)
    back_to_list = list(remove_duplicate)
    print(f"List without duplicates:", back_to_list)
Duplicates()


# Version 2

def new_function(back_to_list):

    return back_to_list

user_list = list(map(int, input("Enter numbers for a list: ").split()))
print(f"List with duplicates:", user_list)

remove_duplicate = set(user_list)
back_to_list = list(remove_duplicate)

def main():
    result = new_function(back_to_list)
    print(f"List without duplicates:", result)

main()
