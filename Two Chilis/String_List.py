# Prompt: Ask the user for a string and print out whether this string is a palindrome or not


palindrome = input("Enter a word to see if it is a palindrome: ")
new =  list(palindrome)
print(new)

reverse = new[::-1]
print(reverse)

if new == reverse:
    print("This is a palindrome")
else:
    print("Not a palindrome")
