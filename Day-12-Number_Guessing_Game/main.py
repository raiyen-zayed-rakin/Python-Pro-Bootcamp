
import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")


def game(game_mode):
    my_nums = []
    for number in range(1, 101):
        my_nums.append(number)
    guess = random.choice(my_nums)

    while game_mode != 0:
        print(f"You have {game_mode} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == guess:
            print(f"You got it! The answer was {user_guess}")
        elif guess - user_guess >= 10:
            print("Too low")
            print("Try again")
            game_mode -= 1
        else:
            print("Too high")
            print("Try again")
            game_mode -= 1


if mode == "easy":
    game(10)
elif mode == "hard":
    game(5)
else:
    print("Wrong input")

