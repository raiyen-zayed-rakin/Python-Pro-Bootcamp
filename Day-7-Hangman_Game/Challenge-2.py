import random
import hangman_art
import hangman_words

print(hangman_art.logo3)

choose_word = random.choice(hangman_words.word_list)
lives = 6

# test purpose
# print(f"Psst, the solution is {choose_word}")

display = []

for _ in choose_word:
    display.append("_")

print(display)
end_of_game = False
while not end_of_game:
    guess = (input("Guess a letter: ")).lower()
    if guess in display:
        print(f"You have already guessed {guess}!")

    for position in range(len(choose_word)):
        if choose_word[position] == guess:
            display[position] = choose_word[position]

    if guess not in choose_word:
        print(f"You have already guessed {guess} which is not in word, you lose a live.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(hangman_art.stages[lives])