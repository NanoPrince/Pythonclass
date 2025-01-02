import random
import string
from wordlist import words

def get_word(words):
    lucky_word = random.choice(words) # Randomly choose from the list
    while '-' in words or '' in words:
        lucky_word = random.choice(words)

    return lucky_word

def hangman():
    lucky_word = get_word(words)
    word_letter = set(words) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    #introducing  lives count
    live = 6


    # getting the user input
    while len(word_letter) > 0:
        # letters used
        #'.join(["a", "b", "ab"]) --> 'a, b, cd'
        print("You have', lives 'lives left and you have used these letters: ",''. join(used_letters))

        #what is the current word (ie W- R D)
        word_list = [letter if letter in used_letters else '-' for letter in words]
        print('current word: ',''.join(word_list))
        user_letter = input("Guess a letter: ").capitalize
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter: 
                word_letter.remove(user_letter)

        elif user_letter in used_letters:
            print('character already used, try another one!')
        else:
            lives = live - 1 # remove 1 life if wrong
            print('invalid character')
    # Gets here when the len(word_letters) == 0
    if lives == 0:
        print('You died, sorry the word was' )
    
    print("you guessed the word', words '!!")

hangman()