# Prompt: Take two lists, and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.


list1 = list(map(int, input("Enter numbers for a list: ").split()))
list2 = list(map(int, input("Enter numbers for a list: ").split()))
new_list = []

for i in list1:
    if i in list2 and i not in new_list:
       new_list.append(i)
new_list = list(tuple(new_list))
print(new_list)
            
