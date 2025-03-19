# Prompt: the task is to write a function that picks a random word from a list of words


import random


def randomWord():

    # open the existing file
    with open('SOWPODS.txt', 'r') as file:
        # read the contents in the file
        contents_of_file =  file.readlines()

        # pick a random word from the file
        random_word = random.choice(contents_of_file).strip()

        # print out the random word
        print(random_word)

randomWord()



