# Prompt: modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.


import csv

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

# add a new friend to the dictionary
add_friend = input("Would you like to add another friend? Yes or No: ")

if add_friend == 'yes':
    name = input("Enter friends name: ")
    day = int(input("Enter day of birth: "))
    month = input("Enter month of bithday: ")
    year = int(input("Enter birth year: "))

    next_friend = f"Friend_{len(birthday) + 1}"

    birthday[next_friend] = {
        "name": name,
        "Day": day,
        "Month": month,
        "Year": year
    }

dictionary_lookup = ["Friends", "name", "Day", "Month", "Year"]


with open("Birthday_Dictionary.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames= dictionary_lookup)
    writer.writeheader()

    for key, info in birthday.items():
        row = {"Friends": key}
        row.update(info)
        writer.writerow(row)



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