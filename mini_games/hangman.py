# Hangman game
# getting familiar with user defined function

import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)  # get a random word form word list
    while '-' in word or ' ' in word:  # if a word contains '-' or space, get another word
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # get each letter in  word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # guessed letters from the user

    lives = 7  # number of guesses
    # if not all letters have been guessed or player have not run out of life, keep playing
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, "lives left\n" "Letters used: ",
              ' '.join(used_letters))  # put on a single string all letters used separated by space
        # a ternary expression that evaluates whether letter is in the used_letters list
        # for each letter in 'word' check if it is in 'used_letter' list, if it is, add it to 'word_list' else add '-'
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))  # ie. (W - R D)
        # getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:  # check if letter haven't been used
            used_letters.add(user_letter)  # if used, add to used_letter
            if user_letter in word_letters:  # if a letter is in the generated word
                word_letters.remove(user_letter)  # remove the letter in the generated word
                print('')

            else:
                lives = lives - 1  # if it's a wrong guess, deduct a life
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print("\nYour have already used that letter. Guess another letter.")

        else:
            print("\n That is not a valid letter.")

    if lives == 0:
        print("You died. The word was: ", word)
    else:
        print("Yay! You guessed the word: ", word)


"""It Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module. For most 
practical purposes, you can think of the conditional block that you open with if __name__ == "__main__" as a way to 
store code that should only run when your file is executed as a script"""
if __name__ == '__main__':
    hangman()
