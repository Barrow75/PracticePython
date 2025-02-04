# Prompt: For this exercise, we will keep track of when our friend’s birthdays are,
# and be able to find that information based on their name.
# Create a dictionary (in your file) of names and birthdays.
# When you run your program, it should ask the user to enter a name, and return the birthday of that person to them.



print("Welcome to the birthday party dictionary")

birthday = {
    "Friend_1" : {
        "name" : "Jimmy",
        "Day"  : 13,
        "Month": "January",
        "Year" : 1957
    },
    "Friend_2" : {
        "name" : "Jeff",
        "Day"  : 16,
        "Month": "December",
        "Year" : 2004

    },
    "Friend_3" : {
        "name" : "Rex",
        "Day"  : 25,
        "Month": "May",
        "Year" : 1945
    }

}

def check_birthday():
    user = input("Whos birthday would you like to lookup: ")
    found = False
    for info in birthday.values():
        if info["name"] == user:
                print(f"{info['name']}'s birthday is on {info['Month']}/{info['Day']}/{info['Year']}")
                found = True

    if not found:
        print("Does not exist")



check_birthday()
