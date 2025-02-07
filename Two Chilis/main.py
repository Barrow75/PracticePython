# Prompt: Take two lists, and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.


palindrome = input("Enter a word to see if it is a palindrome: ")
new =  list(palindrome)
print(new)

reverse = new[::-1]
print(reverse)

if new == reverse:
    print("This is a palindrome")
else:
    print("Not a palindrome")