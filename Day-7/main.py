import random

word_list = ["ardvark", "baboon", "camel"]

choose_word = random.choice(word_list)

guess = (input("Guess a letter: ")).lower()

for letter in choose_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
