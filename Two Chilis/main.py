# Prompt: the task is to write a function that picks a random word from a list of words
# Prompt 2: write the logic that asks a player to guess a letter and displays letters in the clue word that
# were guessed correctly

import random


def randomWord():

    # open the existing file
    with open('SOWPODS.txt', 'r') as file:
        # read the contents in the file
        contents_of_file =  file.readlines()

        # pick a random word from the file
        #random_word = random.choice(contents_of_file).strip()
        return random.choice(contents_of_file).strip()

        # print out the random word
        #print(random_word)



def main():
    word = randomWord()
    print(word)
    # number of guesses of a word (6 times)
    #number_of_guesses = 6

    # lives to keep track of the guesses
    lives_remaining = 6

    # print out _ for the ammount of letters in the current random work
    letters_in_word = ["_"]* len(word) # this inside the while loop resets the correct letters

    # keep track of wrong letters
    guessed_letters = []

    while True:
        # print out _ for the ammount of letters in the current random work
        # letters_in_word = ["_"]* len(word) # this inside the while loop resets the correct letters
        print(letters_in_word)

        # user input for the letters of the word
        user_input = input("Enter a letter you think is in the word: ")

        # check to see if the whole word has been guessed
        if user_input == word:
            print(f"The word was {word}! You have guessed the word correctly! YOU WIN!!!")
            break

        # check to see if the letter is in the word or not
        # if a letter is not in the word take away a life

        if user_input not in word:
            #number_of_guesses -= 1
            lives_remaining -= 1
            print(f"WRONG!! Number of Lives Remaining: {lives_remaining}")


        # if a letter is in the word, don't take away a life
        elif user_input in word:
            # number_of_guesses += 0
            lives_remaining += 0
            print(f"Correct Letter!! Number of Lives Remaining: {lives_remaining}")

        # make sure not to guess the same letter again
        if user_input in guessed_letters:
            print("Letter has already been guessed. Try Again!! \n")
            continue
        guessed_letters.append(user_input)
        print("Guessed Letters:", guessed_letters)

        # reveal the correct letters in the correct position in the word
        for index in range(len(word)):
            if word[index] == user_input:
                letters_in_word[index] = user_input
        print("\nWord: " +" ".join(letters_in_word))



        # ends the game if the lives/guesses are out
        if lives_remaining <= 0:
            print("There are no more lives or guesses remaining. GAME OVER!!!")
            break

main()

