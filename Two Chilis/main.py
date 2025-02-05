# Prompt: Take a list, and write a program that prints out all the elements of the list that are less than 5.


new_list = list(map(int, input("Enter numbers for a list: ").split()))
five_less = []

for elements in new_list:
    if elements <= 5:
        five_less.append(elements)
print(five_less)
