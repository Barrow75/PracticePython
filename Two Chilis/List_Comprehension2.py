# Prompt: Take two lists, and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.



new_list = list(map(int, input("Enter numbers for a list: ").split()))
#print(new_list)
new_list2 = list(map(int, input("Enter numbers for a list: ").split()))

common = list(set([i for i in new_list if i in new_list2]))

print(common)
