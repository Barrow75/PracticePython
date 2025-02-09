# Prompt: Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.



new_list = list(map(int, input("Enter numbers for a list: ").split()))
#print(new_list)

even_nums = [x for x in new_list if x % 2 == 0]
print(even_nums)