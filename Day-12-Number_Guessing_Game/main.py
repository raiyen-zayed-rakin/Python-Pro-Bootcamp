
import art
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")


def game(game_mode):
    guess = randint(1,100)
    print(guess)
    user_guess = 0
    while guess != user_guess or game_mode != 0:
        print(f"You have {game_mode} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == guess:
            print(f"You got it! The answer was {user_guess}")
        elif guess > user_guess:
            print("Too low")
            print("Try again")
            game_mode -= 1
        else:
            print("Too high")
            print("Try again")
            game_mode -= 1
        if game_mode == 0:
            print("you have ran out of guesses, You have lost.")
            return


if mode == "easy":
    game(EASY_LEVEL_TURNS)
elif mode == "hard":
    game(HARD_LEVEL_TURNS)
else:
    print("Wrong input")

